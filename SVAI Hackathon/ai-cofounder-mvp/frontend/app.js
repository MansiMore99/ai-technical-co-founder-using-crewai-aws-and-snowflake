
const chat = document.getElementById('chat');
const input = document.getElementById('msg');
const send = document.getElementById('send');
const API = 'http://localhost:8080/chat';

function addBubble(text, who='user'){
  const div = document.createElement('div');
  div.className = 'bubble ' + who;
  div.textContent = text;
  chat.appendChild(div);
  chat.scrollTop = chat.scrollHeight;
}

async function ask(){
  const q = input.value.trim();
  if(!q) return;
  addBubble(q, 'user');
  input.value='';
  addBubble('…thinking', 'bot');
  try {
    const res = await fetch(API, {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({message: q})
    });
    const data = await res.json();
    chat.lastChild.textContent = data.reply || '(no reply)';
  } catch (e) {
    chat.lastChild.textContent = 'Error: ' + e.message;
  }
}

send.addEventListener('click', ask);
input.addEventListener('keydown', (e)=>{ if(e.key==='Enter') ask(); });

// Welcome message
addBubble("Hi! I’m your AI co‑founder. Ask me anything about your business.", 'bot');
