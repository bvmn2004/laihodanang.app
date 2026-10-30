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
    await sendCommand('Input.enable');

    console.log("\n================ CARD CLICK NAVIGATION TESTS ================");

    // Test 1: Physical mouse click on the image of the first service card (ô tô)
    await sendCommand('Runtime.evaluate', {
      expression: `
        document.documentElement.style.scrollBehavior = 'auto';
        document.querySelector('a.service-card[href="/dich-vu/lai-xe-ho-o-to/"]').scrollIntoView({ block: 'center' });
      `
    });

    await new Promise(r => setTimeout(r, 100));

    const cardInfo = await sendCommand('Runtime.evaluate', {
      expression: `
        (() => {
          const card = document.querySelector('a.service-card[href="/dich-vu/lai-xe-ho-o-to/"]');
          const img = card.querySelector('.service-card-img');
          const rect = img.getBoundingClientRect();
          return {
            x: Math.round(rect.left + rect.width / 2),
            y: Math.round(rect.top + rect.height / 2),
            href: card.getAttribute('href')
          };
        })()
      `,
      returnByValue: true
    });

    const info = cardInfo.result.value;
    console.log(`Clicking image inside service card at (${info.x}, ${info.y}) -> Target ${info.href}...`);

    await sendCommand('Input.dispatchMouseEvent', {
      type: 'mousePressed',
      x: info.x,
      y: info.y,
      button: 'left',
      clickCount: 1
    });
    await sendCommand('Input.dispatchMouseEvent', {
      type: 'mouseReleased',
      x: info.x,
      y: info.y,
      button: 'left',
      clickCount: 1
    });

    await new Promise(r => setTimeout(r, 600));

    let navRes = await sendCommand('Runtime.evaluate', {
      expression: 'window.location.pathname',
      returnByValue: true
    });

    let currentPath = navRes.result.value;
    console.log(`Test 1 (Service Card Image Click): Pathname is ${currentPath} -> ${currentPath === '/dich-vu/lai-xe-ho-o-to/' ? '✅ PASS' : '❌ FAIL'}`);

    // Return to home
    await sendCommand('Page.navigate', { url: 'http://localhost:8080/' });
    await new Promise(r => setTimeout(r, 500));

    // Test 2: Click on the description text of a blog card
    await sendCommand('Runtime.evaluate', {
      expression: `
        document.documentElement.style.scrollBehavior = 'auto';
        document.querySelector('a.blog-card[href="/blog/lai-xe-ho-la-gi/"]').scrollIntoView({ block: 'center' });
      `
    });
    await new Promise(r => setTimeout(r, 100));

    const blogInfo = await sendCommand('Runtime.evaluate', {
      expression: `
        (() => {
          const card = document.querySelector('a.blog-card[href="/blog/lai-xe-ho-la-gi/"]');
          const desc = card.querySelector('.blog-card-desc');
          const rect = desc.getBoundingClientRect();
          return {
            x: Math.round(rect.left + rect.width / 2),
            y: Math.round(rect.top + rect.height / 2),
            href: card.getAttribute('href')
          };
        })()
      `,
      returnByValue: true
    });

    const bInfo = blogInfo.result.value;
    console.log(`Clicking description inside blog card at (${bInfo.x}, ${bInfo.y}) -> Target ${bInfo.href}...`);

    await sendCommand('Input.dispatchMouseEvent', {
      type: 'mousePressed',
      x: bInfo.x,
      y: bInfo.y,
      button: 'left',
      clickCount: 1
    });
    await sendCommand('Input.dispatchMouseEvent', {
      type: 'mouseReleased',
      x: bInfo.x,
      y: bInfo.y,
      button: 'left',
      clickCount: 1
    });

    await new Promise(r => setTimeout(r, 600));

    navRes = await sendCommand('Runtime.evaluate', {
      expression: 'window.location.pathname',
      returnByValue: true
    });

    currentPath = navRes.result.value;
    console.log(`Test 2 (Blog Card Description Click): Pathname is ${currentPath} -> ${currentPath === '/blog/lai-xe-ho-la-gi/' ? '✅ PASS' : '❌ FAIL'}`);

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
