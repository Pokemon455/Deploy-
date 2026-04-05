# server.py
import os
from  fastmcp import FastMCP
from langchain_experimental.tools.python.tool import PythonREPLTool

mcp = FastMCP("Prod MCP")

python_tool = PythonREPLTool()

@mcp.tool()
def run_python(code: str) -> str:
    return str(python_tool.invoke(code))

if __name__ == "__main__":
    # env se port lega (Render/Railway compatible)
    port = int(os.getenv("PORT", 10000))
    
    mcp.run(
    transport="streamable-http",
    host="0.0.0.0",
    port=port
)