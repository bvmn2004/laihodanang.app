const { spawn } = require('child_process');
const http = require('http');

const EDGE_PATH = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe";
const PORT = 9222;

const VIEWPORTS = [320, 375, 390, 430, 768, 820, 1024, 1280, 1366, 1440, 1920];

async function main() {
  console.log("Launching Edge headless with remote debugging port 9222...");
  const edge = spawn(EDGE_PATH, [
    `--remote-debugging-port=${PORT}`,
    '--headless',
    '--disable-gpu',
    '--no-first-run',
    '--no-default-browser-check',
    'http://localhost:8080/'
  ]);

  await new Promise(r => setTimeout(r, 2000));

  try {
    const listData = await fetchJson(`http://127.0.0.1:${PORT}/json`);
    const pageTarget = listData.find(t => t.type === 'page');
    if (!pageTarget) {
      console.error("No page target found");
      edge.kill();
      return;
    }

    const wsUrl = pageTarget.webSocketDebuggerUrl;
    const ws = new WebSocket(wsUrl);

    await new Promise((resolve, reject) => {
      ws.onopen = resolve;
      ws.onerror = reject;
    });

    let msgId = 1;
    function sendCommand(method, params = {}) {
      return new Promise((resolve) => {
        const id = msgId++;
        const handler = (evt) => {
          const res = JSON.parse(evt.data);
          if (res.id === id) {
            ws.removeEventListener('message', handler);
            resolve(res.result);
          }
        };
        ws.addEventListener('message', handler);
        ws.send(JSON.stringify({ id, method, params }));
      });
    }

    // Enable Page
    await sendCommand('Page.enable');
    await sendCommand('DOM.enable');

    console.log("\n================ VIEWPORT DOM & OVERFLOW AUDIT ================");
    for (const w of VIEWPORTS) {
      const h = (w >= 1024) ? 800 : (w >= 768 ? 1024 : 800);
      await sendCommand('Emulation.setDeviceMetricsOverride', {
        width: w,
        height: h,
        deviceScaleFactor: 1,
        mobile: w < 1024
      });

      // Wait a moment for layout reflow
      await new Promise(r => setTimeout(r, 100));

      const evalRes = await sendCommand('Runtime.evaluate', {
        expression: `
          (() => {
            const body = document.body;
            const doc = document.documentElement;
            const header = document.querySelector('.site-header');
            const menuLinks = Array.from(document.querySelectorAll('.nav-link'));
            const hotline = document.querySelector('.hotline-num');
            const scrollWidth = Math.max(doc.scrollWidth, body.scrollWidth);
            const innerWidth = window.innerWidth;
            const hasHorizontalOverflow = scrollWidth > innerWidth;
            
            const wrapDetails = menuLinks.map(l => {
              // Get the text node rects
              const textNode = Array.from(l.childNodes).find(n => n.nodeType === 3 && n.textContent.trim().length > 0) || l.querySelector('span');
              let rects = 1;
              let actualTextHeight = 0;
              if (textNode) {
                const range = document.createRange();
                range.selectNodeContents(textNode);
                const rectList = range.getClientRects();
                rects = rectList.length;
                actualTextHeight = range.getBoundingClientRect().height;
              }
              const lh = parseFloat(window.getComputedStyle(l).lineHeight) || 20;
              return {
                text: l.textContent.replace(/\\s+/g, ' ').trim(),
                lh,
                actualTextHeight,
                rects,
                wraps: rects > 1
              };
            });
            const menuWraps = wrapDetails.some(d => d.wraps);
            
            return {
              viewport: innerWidth,
              scrollWidth: scrollWidth,
              overflow: hasHorizontalOverflow,
              headerHeight: header ? header.offsetHeight : 0,
              menuWraps: menuWraps,
              wrapDetails: wrapDetails,
              hotlineText: hotline ? hotline.textContent.trim() : null
            };
          })()
        `,
        returnByValue: true
      });

      const data = evalRes.result.value;
      const status = (!data.overflow && !data.menuWraps) ? 'PASS' : 'FAIL';
      console.log(`[${status}] Viewport ${w}px -> Inner: ${data.viewport}px, Scroll: ${data.scrollWidth}px, Overflow: ${data.overflow}, HeaderHeight: ${data.headerHeight}px, MenuWraps: ${data.menuWraps}`);
      if (w === 1440) {
        console.log("Wrap details at 1440px:", JSON.stringify(data.wrapDetails, null, 2));
      }
    }
    console.log("=================================================================\n");

    ws.close();
  } catch (err) {
    console.error("Error during CDP testing:", err.message);
  } finally {
    edge.kill();
  }
}

function fetchJson(url) {
  return new Promise((resolve, reject) => {
    http.get(url, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => resolve(JSON.parse(data)));
    }).on('error', reject);
  });
}

main();
