const http = require('http');

const PORT = 9222;

async function checkNavLinks() {
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

  const evalRes = await sendCommand('Runtime.evaluate', {
    expression: `
      (() => {
        const links = Array.from(document.querySelectorAll('.nav-link'));
        return links.map(l => ({
          text: l.textContent.replace(/\\s+/g, ' ').trim(),
          offsetWidth: l.offsetWidth,
          offsetHeight: l.offsetHeight,
          lineHeight: window.getComputedStyle(l).lineHeight,
          fontSize: window.getComputedStyle(l).fontSize,
          padding: window.getComputedStyle(l).padding,
          rects: l.getClientRects().length
        }));
      })()
    `,
    returnByValue: true
  });

  console.log("Nav links metrics at 1920px:");
  console.log(evalRes.result.value);
  ws.close();
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

checkNavLinks();

