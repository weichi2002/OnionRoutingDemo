
# Import socket module
import socket
import json
import random

#list of server ports
#random list





onion = [3001, 3002, 3003, 3004, 3005]
random.shuffle(onion)
            #server      #message                             #client
onion.extend([4000, "Houston, permission to land to on mars!", 4001])

#in order
# onion = [3001, 3002, 3003, 3004, 3005, 4000, "Houston, permission to land to on mars!", 4001]

print(f"Onion packet: {onion}")
data = json.dumps(onion)
 

#send the onion packet to the router
client_socket = socket.socket()
client_socket.connect(('127.0.0.1', onion[0]))
client_socket.send(data.encode('utf-8'))
client_socket.close()


#receive the message back from the server
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 4001))
data, addr = sock.recvfrom(1024)
print(f"Received: {data.decode('utf-8')}")
 

