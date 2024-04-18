
import subprocess

#This is a central function that runs all of the routers, client, and server
#Have to run pkill -9 python3 after every run to clear the process


if __name__ == "__main__":
    
    #make more routers
    server_commands = [
    ['python3', 'server.py'],
    ['python3', 'r1.py'],
    ['python3', 'r2.py'],
    ['python3', 'r3.py'],
    ['python3', 'r4.py'],
    ['python3', 'r5.py'],
    ['python3', 'client.py'],
    ]
    
    server_processes = []
    for cmd in server_commands:
        process = subprocess.Popen(cmd)
        server_processes.append(process)
    
    
        
        
