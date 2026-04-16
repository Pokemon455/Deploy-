# server.py
import os
from fastmcp import FastMCP                                    # MCP server framework
from langchain_experimental.tools.python.tool import PythonREPLTool  # Python code executor

# ─── MCP Server Initialization ───────────────────────────────────────────────
# Creates an MCP server instance with the given name.
# This name appears in the AI's tool list when connected.
mcp = FastMCP("Prod MCP")

# ─── Python REPL Tool Setup ──────────────────────────────────────────────────
# PythonREPLTool from LangChain runs Python code in a local REPL environment.
# It captures stdout/stderr and returns the result as a string.
python_tool = PythonREPLTool()

# ─── MCP Tool Definition ─────────────────────────────────────────────────────
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
    return str(python_tool.invoke(code))

# ─── Server Entry Point ───────────────────────────────────────────────────────
if __name__ == "__main__":
    # Read PORT from environment variable (set automatically by Render/Railway).
    # Falls back to 10000 for local development.
    port = int(os.getenv("PORT", 10000))

    # Start the MCP server with Streamable-HTTP transport.
    # - host="0.0.0.0"  → accept connections from any IP (required for cloud)
    # - path="/mcp"      → MCP endpoint URL path
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=port,
        path="/mcp"
    )
