# 🐍 Python REPL MCP Server

A production-ready **MCP (Model Context Protocol) server** that exposes a Python REPL tool — allowing AI assistants like Claude to execute Python code remotely.

---

## ⚙️ How It Works

This server uses **FastMCP** + **LangChain** to create an MCP-compatible endpoint.  
When called, it runs any Python code and returns the output — making it perfect for AI tool use.

```
Claude / AI Agent  →  MCP Tool Call  →  This Server  →  Python Output
```

---

## 🚀 Run Locally

```bash
pip install -r requirements.txt
python main.py
```

Server starts at: `http://0.0.0.0:10000/mcp`

---

## ☁️ Deploy on Render

1. Push this repo to GitHub
2. Create a new **Web Service** on [Render](https://render.com)
3. Set start command: `python main.py`
4. Set env var `PORT` if needed (default: `10000`)

---

## 📦 Requirements

| Package | Purpose |
|---|---|
| `fastmcp` | MCP server framework |
| `langchain-experimental` | Python REPL tool |
| `uvicorn` | ASGI server |

---

## 🛠️ MCP Tool Exposed

### `run_python`
- **Input:** `code` (string) — any valid Python code
- **Output:** Execution result as string

---

## 👤 Author

**Pokemon455** — AI/ML & MCP Developer  
Built with ❤️ using FastMCP + LangChain
