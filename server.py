# first of all import the socket library
import socket
import json

# next create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 4000
server_socket.bind(('127.0.0.1', port))

# put the socket into listening mode
server_socket.listen(5)
print(f"server listening on port {port}")



# a forever loop until we interrupt it or
# an error occurs
while True:

    # Establish connection with client.
    conn, addr = server_socket.accept()
    data = conn.recv(1024).decode('utf-8')
    onion = json.loads(data)
    onion = onion[1:]
    print("=" * 100)
    print(f"Message: {onion[0]}")
    onion = onion[1:]

    conn.close()


    sock_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock_client.sendto(b"Roger that! TO INFINITY AND BEYOND", ("127.0.0.1", onion[0]))
    print("Server response sent")
    print("=" * 100)

    
    # Create a client socket to send data elsewhere
    # client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client_socket.connect(('127.0.0.1', onion[0]))
    # client_socket.send(b'Roger, permission granted')
    # client_socket.close()
    
