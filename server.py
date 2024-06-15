import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a address and port
server_socket.bind(("localhost", 12345))

# Listen for incoming connections
server_socket.listen(1)

print("Server started. Waiting for connections...")

# Accept an incoming connection
connection, address = server_socket.accept()
print("Connected by", address)

while True:
    # Receive message from client
    message = connection.recv(1024).decode()
    print("Received message:", message)

    # Send response back to client
    response = input("Server: ")
    connection.sendall(response.encode())

    # Check if client wants to exit
    if message.lower() == "exit":
        break

# Close the connection
connection.close()