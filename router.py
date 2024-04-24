import socket
import json
import sys
import random
import time


port = int(sys.argv[1])
delay = int(sys.argv[2])
random_delay = random.random() * delay
# print("random delay ", random_delay)


#initalize socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', port))
server_socket.listen(5) 
# print("Socket listening on port ", port)

while True:
    # Accept incoming connections
    conn, addr = server_socket.accept()
    
    # Receive data from the client
    data = conn.recv(1024).decode('utf-8')
    onion = json.loads(data)
    print(f"ROUTER {port} received the onion packet, sending to ROUTER {onion[1]} next")
    onion = onion[1:]
    conn.close()
    
    #simulate delay
    time.sleep(random_delay)
    
    # Create a client socket to send data elsewhere
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', onion[0]))
    tempData = json.dumps(onion)
    client_socket.send(tempData.encode('utf-8'))
    client_socket.close()
    
