"""CLI entrypoint."""
from __future__ import annotations

import typer
from rich.console import Console

app = typer.Typer(help="TG Knowledge Base")
console = Console()


@app.command()
def stats(db: str = "./data/tgkb.db"):
    from .storage import Storage
    s = Storage(db)
    console.print(s.stats())
    s.close()


@app.command()
def search(query: str, db: str = "./data/tgkb.db", limit: int = 20):
    from .storage import Storage
    s = Storage(db)
    for r in s.search(query, limit=limit):
        console.print(f"[cyan]{r['date']}[/] {r['sender_name']}: {r['text'][:120]}")
    s.close()


@app.command()
def serve(host: str = "0.0.0.0", port: int = 8080, db: str = "./data/tgkb.db"):
    import uvicorn
    from . import api
    from .storage import Storage
    api._storage = Storage(db)
    console.print(f"Starting server on http://{host}:{port}")
    uvicorn.run(api.app, host=host, port=port)


@app.command()
def collect(chat: str, limit: int = 10000, db: str = "./data/tgkb.db"):
    import os, asyncio
    from dotenv import load_dotenv
    load_dotenv()
    api_id = int(os.getenv("API_ID", "0"))
    api_hash = os.getenv("API_HASH", "")
    from .collector import collect as _collect
    from .storage import Storage
    s = Storage(db)
    async def run():
        n = 0
        async for m in _collect(chat, limit=limit, api_id=api_id, api_hash=api_hash):
            s.upsert(m)
            n += 1
        console.print(f"Imported {n} messages")
        s.close()
    asyncio.run(run())


def main():
    app()


if __name__ == "__main__":
    main()
