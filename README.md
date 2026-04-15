<div align="center">

# 🐍 FastMCP Python REPL Server

**Give any AI assistant the power to execute Python — via MCP.**

[![Made with FastMCP](https://img.shields.io/badge/Made%20with-FastMCP-blueviolet?style=for-the-badge)](https://github.com/jlowin/fastmcp)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)](https://python.org)
[![Deploy on Render](https://img.shields.io/badge/Deploy-Render-46E3B7?style=for-the-badge&logo=render)](https://render.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

</div>

---

## ✨ What Is This?

A **production-ready MCP (Model Context Protocol) server** that exposes a Python REPL as an AI tool.

Plug it into **Claude**, **Cursor**, or any MCP-compatible AI — and watch it execute real Python code on demand.

```
You / AI Agent  →  MCP Tool Call  →  This Server  →  Live Python Output  →  Back to AI
```

> 🔴 **Live Demo:** This server is actively running and connected to Claude.ai as a custom tool.

---

## 🚀 Features

- ⚡ **One tool, infinite power** — `run_python` executes any Python code and returns output
- 🌐 **Cloud-ready** — deploy to Render, Railway, or any platform in minutes
- 🔌 **Plug & Play** — works with Claude, Cursor, and any MCP-compatible client
- 🧰 **Built on FastMCP** — the fastest way to build MCP servers in Python
- 📦 **Minimal setup** — 3 dependencies, ~10 lines of core code

---

## 🛠️ Quick Start

### 1. Clone & Install
```bash
git clone https://github.com/Pokemon455/fastmcp-python-repl-server.git
cd fastmcp-python-repl-server
pip install -r requirements.txt
```

### 2. Run Locally
```bash
python main.py
```
Server starts at: `http://localhost:10000/mcp`

### 3. Connect to Claude Desktop
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "python-repl": {
      "url": "http://localhost:10000/mcp",
      "transport": "streamable-http"
    }
  }
}
```

---

## ☁️ Deploy on Render (Free)

1. Fork this repo
2. Go to [render.com](https://render.com) → New Web Service
3. Connect your GitHub repo
4. Set start command: `python main.py`
5. Done! Your MCP server is live 🎉

---

## 📦 Tech Stack

| Package | Purpose |
|---|---|
| [`fastmcp`](https://github.com/jlowin/fastmcp) | MCP server framework |
| [`langchain-experimental`](https://github.com/langchain-ai/langchain) | Python REPL execution |
| [`uvicorn`](https://www.uvicorn.org/) | Lightning-fast ASGI server |

---

## 🔧 MCP Tool Reference

### `run_python(code: str) → str`
Executes any Python code string and returns the output.

**Example:**
```python
# Input
code = "print(sum([1, 2, 3, 4, 5]))"

# Output
"15"
```

---

## 🗺️ Roadmap

- [x] Python REPL via MCP
- [x] Render/Railway deployment support
- [ ] API key authentication
- [ ] Sandboxed execution environment
- [ ] Support for file I/O & pip installs
- [ ] Docker support

---

## 🤝 Contributing

PRs are welcome! If you have ideas to make this better — open an issue or submit a pull request.

---

## 👤 Author

**Pokemon455** — AI/ML & MCP Developer
🔗 [GitHub](https://github.com/Pokemon455)

---

<div align="center">

⭐ **If this saved you time, drop a star — it keeps the project alive!** ⭐

</div>
