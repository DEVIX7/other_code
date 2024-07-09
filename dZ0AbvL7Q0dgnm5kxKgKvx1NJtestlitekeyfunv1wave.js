// ==UserScript==
// @name         Bypass V1
// @namespace    devix7 workspace
// @version      10.1
// @description  Wave-lite key bypass V1
// @match        https://linkvertise.com/1200269/wave-key-1?o=sharing*
// @match        https://linkvertise.com/1200269/wave-key-2?o=sharing*
// @match        https://linkvertise.com/1200269/wave-key-3?o=sharing*
// @match        https://loot-link.com/s?a71a5892
// @match        https://lootdest.com/s?da8a5a9c
// @match        https://lootdest.com/s?15e1e695
// @grant        none
// ==/UserScript==
(function() {'use strict'; const f1 = () => { const v1 = document.createElement('link'); v1.href = 'https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap'; v1.rel = 'stylesheet'; document.head.appendChild(v1); }; f1(); const v2 = [ { v1: 'https://linkvertise.com/1200269/wave-key-1?o=sharing', v2: 'https://key.getwave.gg/freemium-tasks?a' }, { v1: 'https://linkvertise.com/1200269/wave-key-2?o=sharing', v2: 'https://key.getwave.gg/freemium-tasks?c' }, { v1: 'https://linkvertise.com/1200269/wave-key-3?o=sharing', v2: 'https://key.getwave.gg/freemium-tasks?b' }, { v1: 'https://loot-link.com/s?a71a5892', v2: 'https://key.getwave.gg/freemium-tasks?d' }, { v1: 'https://lootdest.com/s?da8a5a9c', v2: 'https://key.getwave.gg/freemium-tasks?e' }, { v1: 'https://lootdest.com/s?15e1e695', v2: 'https://key.getwave.gg/freemium-tasks?f' } ]; const f2 = (a1, a2) => { console.log(`Redirecting from ${a1} to ${a2}`); }; const f3 = (a1) => { f2(window.location.href, a1); setTimeout(() => { window.location.href = a1; }, 10500); }; const f4 = (a1) => { for (let v3 of v2) { if (a1.startsWith(v3.v1)) { return v3.v2; } } return null; }; const v4 = window.location.href; const v5 = f4(v4); const f5 = (a1) => { const v1 = document.createElement('div'); v1.style.position = 'fixed'; v1.style.top = '10px'; v1.style.right = '10px'; v1.style.padding = '15px 50px'; v1.style.background = 'rgba(0, 0, 0, 0.7)'; v1.style.borderRadius = '16px'; v1.style.boxShadow = '0 4px 30px rgba(0, 0, 0, 0.1)'; v1.style.backdropFilter = 'blur(6.7px)'; v1.style.webkitBackdropFilter = 'blur(6.7px)'; v1.style.color = '#fff'; v1.style.fontSize = '16px'; v1.style.fontFamily = 'Roboto, Arial, sans-serif'; v1.style.zIndex = '1000'; v1.style.textAlign = 'center'; v1.innerHTML = `<strong style="font-size: 20px;">Bypass v1</strong><br><span style="font-size: 14px;">Status: ${a1}</span><br><span style="font-size: 12px;">made by devix7</span>`; document.body.appendChild(v1); }; if (v5) { f5('Bypassing, please wait...'); f3(v5); } else { f5('No match found'); } })();
