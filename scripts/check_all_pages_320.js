const { spawn } = require('child_process');
const http = require('http');

const EDGE_PATH = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe";
const PORT = 9222;

const PAGES = [
  '/',
  '/dich-vu/',
  '/khu-vuc/',
  '/blog/',
  '/bang-gia/',
  '/gioi-thieu/',
  '/lien-he/',
  '/dich-vu/lai-xe-ho-o-to/',
  '/khu-vuc/hai-chau/',
  '/blog/lai-xe-ho-la-gi/'
];

async function main() {
  const edge = spawn(EDGE_PATH, [
    `--remote-debugging-port=${PORT}`,
    '--headless',
    '--disable-gpu',
    'http://localhost:8080/'
  ]);

  await new Promise(r => setTimeout(r, 1500));

  try {
    const listData = await fetchJson(`http://127.0.0.1:${PORT}/json`);
    const pageTarget = listData.find(t => t.type === 'page');
    const ws = new WebSocket(pageTarget.webSocketDebuggerUrl);
    await new Promise(r => ws.onopen = r);

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

    await sendCommand('Page.enable');
    await sendCommand('Emulation.setDeviceMetricsOverride', {
      width: 320,
      height: 800,
      deviceScaleFactor: 1,
      mobile: true
    });

    console.log("\nTesting 320px width across key pages:");
    for (const p of PAGES) {
      await sendCommand('Page.navigate', { url: `http://localhost:8080${p}` });
      await new Promise(r => setTimeout(r, 400));
      await sendCommand('Emulation.setDeviceMetricsOverride', {
        width: 320,
        height: 800,
        deviceScaleFactor: 1,
        mobile: true
      });
      await new Promise(r => setTimeout(r, 200));

      const evalRes = await sendCommand('Runtime.evaluate', {
        expression: `
          (() => {
            const doc = document.documentElement;
            const body = document.body;
            return {
              scrollWidth: Math.max(doc.scrollWidth, body.scrollWidth),
              innerWidth: window.innerWidth
            };
          })()
        `,
        returnByValue: true
      });

      const res = evalRes.result.value;
      const status = res.scrollWidth <= res.innerWidth ? '✅ PASS' : '❌ FAIL';
      console.log(`[${status}] Page: ${p.padEnd(28, ' ')} | Inner: ${res.innerWidth}px | Scroll: ${res.scrollWidth}px`);
    }

    ws.close();
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
