const { spawn } = require('child_process');
const http = require('http');

const EDGE_PATH = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe";
const PORT = 9222;

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
      width: 1440,
      height: 900,
      deviceScaleFactor: 1,
      mobile: false
    });

    console.log("\n================ FLOATING CONTACT CLICKS AUDIT ================");

    const evalRes = await sendCommand('Runtime.evaluate', {
      expression: `
        (() => {
          const fc = document.getElementById('floating-contact');
          const fb = fc.querySelector('.fb-btn');
          const zalo = fc.querySelector('.zalo-btn');
          const call = fc.querySelector('.call-btn');
          const zaloImg = zalo.querySelector('img');

          return {
            fbHref: fb.getAttribute('href'),
            fbTarget: fb.getAttribute('target'),
            fbRel: fb.getAttribute('rel'),
            fbAria: fb.getAttribute('aria-label'),
            zaloHref: zalo.getAttribute('href'),
            zaloTarget: zalo.getAttribute('target'),
            zaloRel: zalo.getAttribute('rel'),
            zaloAria: zalo.getAttribute('aria-label'),
            zaloImgSrc: zaloImg.getAttribute('src'),
            zaloImgNaturalWidth: zaloImg.naturalWidth,
            callHref: call.getAttribute('href'),
            callAria: call.getAttribute('aria-label')
          };
        })()
      `,
      returnByValue: true
    });

    const info = evalRes.result.value;
    console.log("Floating contact element inspection:", JSON.stringify(info, null, 2));

    const fbOk = info.fbHref === "https://www.facebook.com/laixehodanang247/" && info.fbTarget === "_blank" && info.fbRel.includes("noopener");
    const zaloOk = info.zaloHref === "https://zalo.me/0985666044" && info.zaloTarget === "_blank" && info.zaloRel.includes("noopener") && info.zaloImgSrc === "/assets/images/zalo-icon.svg";
    const callOk = info.callHref === "tel:0985666044";

    console.log(`Facebook Button Check: ${fbOk ? '✅ PASS' : '❌ FAIL'}`);
    console.log(`Zalo Button Check:     ${zaloOk ? '✅ PASS' : '❌ FAIL'}`);
    console.log(`Call Button Check:     ${callOk ? '✅ PASS' : '❌ FAIL'}`);

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

