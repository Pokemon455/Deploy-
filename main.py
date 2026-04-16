# server.py
# ─────────────────────────────────────────────────────────────────────────────
# This is the main entry point of the FastMCP Python REPL Server.
# It sets up an MCP (Model Context Protocol) server that exposes a single tool:
# `run_python` — which lets any connected AI (like Claude) execute Python code
# on this server and receive the output in real time.
# ─────────────────────────────────────────────────────────────────────────────

import os  # Used to read environment variables like PORT (set by Render/Railway)

from fastmcp import FastMCP
# FastMCP is a Python framework for building MCP servers quickly.
# It handles the MCP protocol, tool registration, and HTTP transport automatically.

from langchain_experimental.tools.python.tool import PythonREPLTool
# PythonREPLTool is a LangChain utility that runs Python code in a live REPL.
# It executes the code string, captures the output (stdout/stderr), and returns it.


# ─── MCP Server Initialization ───────────────────────────────────────────────
# FastMCP("Prod MCP") creates a new MCP server instance.
# "Prod MCP" is the server name — this is what appears in the AI's tool panel
# when Claude or another MCP client connects to this server.
mcp = FastMCP("Prod MCP")


# ─── Python REPL Tool Setup ──────────────────────────────────────────────────
# Create a single instance of PythonREPLTool.
# This instance is reused for every tool call — it maintains a persistent
# Python session, so variables defined in one call are available in the next.
python_tool = PythonREPLTool()


# ─── MCP Tool Definition ─────────────────────────────────────────────────────
# @mcp.tool() registers the function below as an MCP tool.
# Once registered, any connected AI can call `run_python` by name,
# pass Python code as input, and receive the output as a string.
@mcp.tool()
def run_python(code: str) -> str:
    """
    Execute Python code and return the output.

    This tool allows any connected AI assistant to run Python code
    on this server and get back the result instantly.

    Args:
        code (str): Valid Python code to execute.

    Returns:
        str: Output of the executed code (stdout/stderr).

    Example:
        Input:  "print(sum([1, 2, 3]))"
        Output: "6"
    """
    # python_tool.invoke(code) runs the code string in the REPL
    # and returns the output. We wrap it in str() to ensure it's always a string.
    return str(python_tool.invoke(code))


# ─── Server Entry Point ───────────────────────────────────────────────────────
if __name__ == "__main__":
    # os.getenv("PORT") reads the PORT environment variable.
    # Cloud platforms like Render and Railway set this automatically.
    # If not set (e.g. running locally), it defaults to port 10000.
    port = int(os.getenv("PORT", 10000))

    # mcp.run() starts the MCP server with the given configuration:
    #
    # transport="streamable-http"
    #   → Uses HTTP as the communication protocol between AI and server.
    #     "Streamable" means responses can be streamed back in chunks.
    #
    # host="0.0.0.0"
    #   → Listens on all network interfaces (required for cloud deployment).
    #     Using "localhost" would only work locally, not on Render/Railway.
    #
    # port=port
    #   → The port number to listen on (from env variable or default 10000).
    #
    # path="/mcp"
    #   → The URL path where the MCP endpoint is available.
    #     Full URL example: https://your-app.onrender.com/mcp
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=port,
        path="/mcp"
    )
