"""FastAPI backend."""
from __future__ import annotations

from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from .storage import Storage

app = FastAPI(title="TG Knowledge Base", version="1.0.0")
_storage: Storage | None = None


def get_storage() -> Storage:
    global _storage
    if _storage is None:
        _storage = Storage()
    return _storage


@app.get("/api/stats")
def stats():
    return get_storage().stats()


@app.get("/api/search")
def search(q: str = Query(...), limit: int = 50):
    return {"results": get_storage().search(q, limit=limit)}


@app.get("/", response_class=HTMLResponse)
def index():
    return """<!DOCTYPE html>
<html lang="zh"><head><meta charset="utf-8"><title>TG 知识库</title>
<style>
body{font-family:system-ui;background:#0b0f19;color:#e6e9ef;margin:0;padding:2rem}
h1{color:#7dd3fc} input{padding:.6rem 1rem;border-radius:8px;border:1px solid #334;width:60%;background:#111827;color:#fff}
button{padding:.6rem 1.2rem;border-radius:8px;border:none;background:#3b82f6;color:#fff;cursor:pointer}
.card{background:#111827;border:1px solid #1f2937;border-radius:12px;padding:1rem;margin:.6rem 0}
.meta{color:#9ca3af;font-size:.85rem}
</style></head><body>
<h1>🧠 TG 知识库</h1>
<p class="meta">全文搜索 Telegram 消息</p>
<input id="q" placeholder="输入关键词..." onkeydown="if(event.key==='Enter')go()">
<button onclick="go()">搜索</button>
<div id="res"></div>
<script>
async function go(){const q=document.getElementById('q').value;
const r=await fetch('/api/search?q='+encodeURIComponent(q));const d=await r.json();
document.getElementById('res').innerHTML=d.results.map(x=>`<div class="card"><div class="meta">${x.date} · ${x.sender_name||''} · ${x.chat_title||''}</div><div>${x.text}</div></div>`).join('');}
fetch('/api/stats').then(r=>r.json()).then(d=>{document.querySelector('p.meta').textContent=`${d.total_messages} 条消息 · ${d.chats} 个聊天`;});
</script></body></html>"""
