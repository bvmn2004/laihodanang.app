const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');
const path = require('path');

const EDGE_PATH = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe";
const PORT = 9222;

const VIEWPORTS = [320, 360, 375, 390, 393, 414, 430, 768, 820, 1024, 1280, 1366, 1440, 1920];

const SCREENSHOT_DIR = path.resolve(__dirname, '..', 'research', 'screenshots');
if (!fs.existsSync(SCREENSHOT_DIR)) {
  fs.mkdirSync(SCREENSHOT_DIR, { recursive: true });
}

async function main() {
  console.log("Launching Edge headless on port 9222...");
  const edge = spawn(EDGE_PATH, [
    `--remote-debugging-port=${PORT}`,
    '--headless',
    '--disable-gpu',
    '--no-first-run',
    '--no-default-browser-check',
    'http://localhost:8080/'
  ]);

  await new Promise(r => setTimeout(r, 2000));

  let overallPass = true;

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

    await sendCommand('Page.enable');
    await sendCommand('DOM.enable');

    console.log("\n================ 14 VIEWPORT THOROUGH AUDIT ================");

    for (const w of VIEWPORTS) {
      const h = (w >= 1024) ? 800 : (w >= 768 ? 1024 : 800);
      await sendCommand('Emulation.setDeviceMetricsOverride', {
        width: w,
        height: h,
        deviceScaleFactor: 1,
        mobile: w < 1024
      });

      // Wait a moment for layout reflow
      await new Promise(r => setTimeout(r, 150));

      const evalRes = await sendCommand('Runtime.evaluate', {
        expression: `
          (() => {
            const body = document.body;
            const doc = document.documentElement;
            const header = document.querySelector('.site-header');
            const topBar = document.querySelector('.top-bar');
            const callBtn = document.querySelector('.btn-header-call');
            const zaloBtn = document.querySelector('.btn-header-zalo');
            const hamburger = document.querySelector('.mobile-menu-toggle');
            const brandTitle = document.querySelector('.brand-title');
            const stickyBar = document.querySelector('.mobile-sticky-bar');
            const stickyCall = stickyBar ? stickyBar.querySelector('.call-btn') : null;
            const stickyZalo = stickyBar ? stickyBar.querySelector('.zalo-btn') : null;

            const scrollWidth = Math.max(doc.scrollWidth, body.scrollWidth);
            const innerWidth = window.innerWidth;
            const hasHorizontalOverflow = scrollWidth > innerWidth;

            // Check header elements
            const topBarDisplay = topBar ? window.getComputedStyle(topBar).display : 'none';
            const callBtnDisplay = callBtn ? window.getComputedStyle(callBtn).display : 'none';
            const zaloBtnDisplay = zaloBtn ? window.getComputedStyle(zaloBtn).display : 'none';
            const hamburgerDisplay = hamburger ? window.getComputedStyle(hamburger).display : 'none';
            const hamburgerRect = hamburger ? hamburger.getBoundingClientRect() : null;

            // Check sticky bar
            const stickyDisplay = stickyBar ? window.getComputedStyle(stickyBar).display : 'none';
            const stickyCallRect = stickyCall ? stickyCall.getBoundingClientRect() : null;
            const stickyZaloRect = stickyZalo ? stickyZalo.getBoundingClientRect() : null;

            // Check menu wraps on desktop
            const menuLinks = Array.from(document.querySelectorAll('.site-nav .nav-link'));
            const wrapDetails = menuLinks.map(l => {
              const textNode = Array.from(l.childNodes).find(n => n.nodeType === 3 && n.textContent.trim().length > 0) || l.querySelector('span');
              let rects = 1;
              if (textNode) {
                const range = document.createRange();
                range.selectNodeContents(textNode);
                rects = range.getClientRects().length;
              }
              return { text: l.textContent.replace(/\\s+/g, ' ').trim(), rects };
            });
            const menuWraps = wrapDetails.some(d => d.rects > 1);

            // Check cards on page
            const serviceCards = Array.from(document.querySelectorAll('.service-card'));
            const blogCards = Array.from(document.querySelectorAll('.blog-card'));
            const allCardsAreAnchors = [...serviceCards, ...blogCards].every(c => c.tagName === 'A' && c.getAttribute('href'));

            // Check floating contact
            const fc = document.getElementById('floating-contact');
            const fcFb = fc ? fc.querySelector('.fb-btn') : null;
            const fcZalo = fc ? fc.querySelector('.zalo-btn') : null;
            const fcCall = fc ? fc.querySelector('.call-btn') : null;
            const fcRect = fc ? fc.getBoundingClientRect() : null;

            return {
              viewport: innerWidth,
              scrollWidth: scrollWidth,
              overflow: hasHorizontalOverflow,
              headerHeight: header ? header.offsetHeight : 0,
              topBarDisplay: topBarDisplay,
              callBtnDisplay: callBtnDisplay,
              zaloBtnDisplay: zaloBtnDisplay,
              hamburgerDisplay: hamburgerDisplay,
              hamburgerTouchSize: hamburgerRect ? { w: Math.round(hamburgerRect.width), h: Math.round(hamburgerRect.height) } : null,
              stickyDisplay: stickyDisplay,
              stickyCallTarget: stickyCallRect ? { w: Math.round(stickyCallRect.width), h: Math.round(stickyCallRect.height), href: stickyCall.getAttribute('href') } : null,
              stickyZaloTarget: stickyZaloRect ? { w: Math.round(stickyZaloRect.width), h: Math.round(stickyZaloRect.height), href: stickyZalo.getAttribute('href') } : null,
              menuWraps: menuWraps,
              totalServiceCards: serviceCards.length,
              totalBlogCards: blogCards.length,
              allCardsAreAnchors: allCardsAreAnchors,
              hasFloatingContact: !!fc,
              fcFbDisplay: fcFb ? window.getComputedStyle(fcFb).display : 'none',
              fcZaloDisplay: fcZalo ? window.getComputedStyle(fcZalo).display : 'none',
              fcCallDisplay: fcCall ? window.getComputedStyle(fcCall).display : 'none',
              fcBottom: fcRect ? window.innerHeight - fcRect.bottom : 0
            };
          })()
        `,
        returnByValue: true
      });

      const d = evalRes.result.value;

      // Evaluation rules
      let passed = true;
      const issues = [];

      if (d.overflow) {
        passed = false;
        issues.push(`Horizontal overflow detected: scrollWidth (${d.scrollWidth}px) > viewport (${d.viewport}px)`);
      }

      if (w < 768) {
        // Mobile rules
        if (d.topBarDisplay !== 'none') {
          passed = false;
          issues.push(`Top bar is not hidden on mobile (display: ${d.topBarDisplay})`);
        }
        if (d.callBtnDisplay !== 'none' || d.zaloBtnDisplay !== 'none') {
          passed = false;
          issues.push(`Header CTA buttons must be hidden on mobile to avoid overcrowding`);
        }
        if (!d.hamburgerTouchSize || d.hamburgerTouchSize.w < 44 || d.hamburgerTouchSize.h < 44) {
          passed = false;
          issues.push(`Hamburger touch size too small: ${JSON.stringify(d.hamburgerTouchSize)}`);
        }
        if (d.stickyDisplay === 'none') {
          passed = false;
          issues.push(`Sticky bottom contact bar must be visible on mobile`);
        }
        if (d.stickyCallTarget && (d.stickyCallTarget.h < 44 || !d.stickyCallTarget.href.startsWith('tel:'))) {
          passed = false;
          issues.push(`Sticky call button issue: ${JSON.stringify(d.stickyCallTarget)}`);
        }
        if (d.stickyZaloTarget && (d.stickyZaloTarget.h < 44 || !d.stickyZaloTarget.href.includes('zalo.me'))) {
          passed = false;
          issues.push(`Sticky Zalo button issue: ${JSON.stringify(d.stickyZaloTarget)}`);
        }
      } else if (w >= 1024) {
        // Desktop rules
        if (d.menuWraps) {
          passed = false;
          issues.push(`Menu text wrapped onto multiple lines`);
        }
        if (d.hamburgerDisplay !== 'none') {
          passed = false;
          issues.push(`Hamburger menu should be hidden on desktop`);
        }
      }

      if (!d.allCardsAreAnchors) {
        passed = false;
        issues.push(`Not all cards are <a> tags with href`);
      }

      if (!d.hasFloatingContact) {
        passed = false;
        issues.push(`Floating contact #floating-contact is missing`);
      } else {
        if (w < 768) {
          if (d.fcFbDisplay === 'none') {
            passed = false;
            issues.push(`Floating Facebook button should be visible on mobile`);
          }
          if (d.fcZaloDisplay !== 'none' || d.fcCallDisplay !== 'none') {
            passed = false;
            issues.push(`Floating Zalo/Call buttons should be hidden on mobile to avoid duplicating sticky bar`);
          }
        } else {
          if (d.fcFbDisplay === 'none' || d.fcZaloDisplay === 'none' || d.fcCallDisplay === 'none') {
            passed = false;
            issues.push(`All 3 floating buttons (FB, Zalo, Call) must be visible on tablet & desktop`);
          }
        }
      }

      if (!passed) overallPass = false;

      // Take screenshot
      const ssRes = await sendCommand('Page.captureScreenshot', {
        format: 'png',
        clip: {
          x: 0,
          y: 0,
          width: w,
          height: h,
          scale: 1
        }
      });

      if (ssRes && ssRes.data) {
        const filePath = path.join(SCREENSHOT_DIR, `viewport_${w}px.png`);
        fs.writeFileSync(filePath, Buffer.from(ssRes.data, 'base64'));
      }

      const statusBadge = passed ? '✅ PASS' : '❌ FAIL';
      console.log(`[${statusBadge}] Viewport ${w.toString().padStart(4, ' ')}px | Scroll: ${d.scrollWidth}px | Hdr: ${d.headerHeight}px | Cards: ${d.totalServiceCards} svc + ${d.totalBlogCards} blog | Screenshot saved`);
      if (issues.length > 0) {
        issues.forEach(iss => console.log(`       ⚠️  Issue: ${iss}`));
      }
    }

    console.log("============================================================\n");
    if (overallPass) {
      console.log("🎉 ALL 14 VIEWPORTS PASSED PERFECTLY WITH ZERO ISSUES! 🎉\n");
    } else {
      console.log("❌ SOME VIEWPORTS FAILED. REVIEW ISSUES ABOVE. ❌\n");
    }

    ws.close();
  } catch (err) {
    console.error("Error during testing:", err);
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

