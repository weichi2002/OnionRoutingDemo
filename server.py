import socket
import json

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 5000
server_socket.bind(('127.0.0.1', port))
server_socket.listen(5)
# print(f"server listening on port {port}")




while True:

    conn, addr = server_socket.accept()
    data = conn.recv(1024).decode('utf-8')
    onion = json.loads(data)
    onion = onion[1:]
    print(f"Server received: {onion[0]}")
    
    
    onion = onion[1:]

    conn.close()


    sock_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock_client.sendto(b"Aye Matey", ("127.0.0.1", onion[0]))

    
