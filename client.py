
# Import socket module
import socket
import json
import random

#list of possible routers
onion = [3001, 3002, 3003, 3004, 3005]

#randomly choose the order
random.shuffle(onion)

#construct the onion packet
                #server      #message                          #client
onion.extend([4000, "Houston, permission to land to on mars!", 4001])



 

#send the onion packet to the router using client socket
client_socket = socket.socket()
client_socket.connect(('127.0.0.1', onion[0]))

data = json.dumps(onion)
client_socket.send(data.encode('utf-8'))

print("\n" + "=" * 100)
print(f"Client sent the onion packet: {onion}")
print("=" * 100)

client_socket.close()


#receive the message back from the server
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 4001))
data, addr = sock.recvfrom(1024)
print(f"Client received: {data.decode('utf-8')}")
 

