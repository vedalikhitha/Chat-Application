import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(("localhost", 12345))

print("Connected to server. Type 'exit' to quit.")

while True:
    # Send message to server
    message = input("Client: ")
    client_socket.sendall(message.encode())

    # Receive response from server
    response = client_socket.recv(1024).decode()
    print("Server:", response)

    # Check if server wants to exit
    if response.lower() == "exit":
        break

# Close the connection
client_socket.close()