import socket
import json

# Create the server socket outside the loop
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 3001
server_socket.bind(('127.0.0.1', port))
server_socket.listen(5) 
print("Socket listening on port ", port)

while True:
    # Accept incoming connections
    conn, addr = server_socket.accept()
    
    # Receive data from the client
    data = conn.recv(1024).decode('utf-8')
    onion = json.loads(data)
    onion = onion[1:]
    print(onion)
    conn.close()
    
    # Create a client socket to send data elsewhere
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', onion[0]))
    tempData = json.dumps(onion)
    client_socket.send(tempData.encode('utf-8'))
    client_socket.close()
    
