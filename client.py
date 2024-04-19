
# Import socket module
import socket
import json
import random
import sys

#list of possible routers
n = int(sys.argv[1])

onion = []
for i in range(1, n+1):
    onion.append(3000 + i)
    
#randomly choose the order
random.shuffle(onion)

#construct the onion packet
                #server      #message                          #client
onion.extend([5000, "What did the pirate say when he turned 80?", 5001])


#send the onion packet to the router using client socket
client_socket = socket.socket()
client_socket.connect(('127.0.0.1', onion[0]))

data = json.dumps(onion)
client_socket.send(data.encode('utf-8'))

print(f"Client sent the onion packet: {onion}")

client_socket.close()


#receive the message back from the server
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 5001))
data, addr = sock.recvfrom(1024)
print(f"Client received: {data.decode('utf-8')}")
 

