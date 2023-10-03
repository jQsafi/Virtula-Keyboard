import socket

import pyautogui

# Set up a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 12345))
server_socket.listen(1)

print("Server listening...")

# Accept incoming connections
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address}")

while True:
    command = client_socket.recv(1024).decode()
    if not command:
        break
    if command == "move_cursor":
        # Receive coordinates (x, y)
        x, y = map(int, client_socket.recv(1024).decode().split(","))
        # Move the cursor
        pyautogui.moveTo(x, y)

client_socket.close()
server_socket.close()
