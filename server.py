import socket
import os

s = socket.socket()
s.bind(('localhost', 8000))
s.listen(5)
print("Server listening on port 8000...")

c, addr = s.accept()
print(f"Connection from {addr}")

while True:
    hostname = c.recv(1024).decode('utf-8')
    if not hostname or hostname.lower() == 'exit':
        print("Client disconnected.")
        break

    try:
        # Use system ping command
        response = os.popen(f"ping -n 4 {hostname}").read()  # Use -c 4 for Linux/Mac
        c.send(response.encode('utf-8'))
    except Exception as e:
        c.send(f"Ping failed: {e}".encode('utf-8'))

c.close()