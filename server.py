from mcp.server.fastmcp import FastMCP

mcp =  FastMCP("demo")

def add(a:int,b:int)->int:
    return int(a)+int(b)
def subtract(a:int,b:int)->int:
    return int(a)-int(b)
def multiply(a:int,b:int)->int:
    return int(a)*int(b)
def divide(a:int,b:int)->int:
    return int(a)/int(b)

mcp.tool()(add)
mcp.tool()(multiply)

mcp.tool()(subtract)
mcp.tool()(divide)
if __name__ == "__main__":
    mcp.run()
