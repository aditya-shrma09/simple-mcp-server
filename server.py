from mcp.server.fastmcp import FastMCP

import socket
host = "127.0.0.1"
port = 5000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen()
print("Server is listening...")

conn, addr = s.accept()

print("Connected by", addr)

data = conn.recv(1024)
print("Received:", data.decode())

conn.sendall(b"Hello Client!")



# mcp =  FastMCP("calculator")

# def add(a:int,b:int)->int:
#     """Add two integers."""
#     return int(a)+int(b)
# def subtract(a:int,b:int)->int:
#     """subtract two integers."""
#     return int(a)-int(b)
# def multiply(a:int,b:int)->int:
#     """multiply two integers."""
#     return int(a)*int(b)
# def divide(a:int,b:int):
#     """divide two integers."""
#     if b==0:
#         raise ValueError("b cannot be 0")
#     return int(a)/int(b)
# def power(a:int,b:int)->int:
#     """to use when raising one integer to power of another integer"""
#     return a**b

# mcp.tool()(power)
# mcp.tool()(add)
# mcp.tool()(multiply)

# mcp.tool()(subtract)
# mcp.tool()(divide)
# if __name__ != "__main__":
#     mcp.run()

conn.close()
s.close()