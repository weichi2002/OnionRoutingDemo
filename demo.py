import os
import subprocess

# Define the commands to run


if __name__ == "__main__":
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
        
        # Add more server commands as needed

 