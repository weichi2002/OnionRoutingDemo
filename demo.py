import sys
import subprocess
import os


def main(n, delay):
    
    portNumber = 3000
    commands = [
        #add the routers here
        ['python3', 'server.py'],
        ['python3', 'client.py', str(n)],
    ]
    
    for _ in range(n):
        portNumber+=1
        cmd = ['python3', "router.py", str(portNumber), str(delay)]
        commands.insert(0, cmd)
        
        
    for cmd in commands:
        subprocess.Popen(cmd)
        
    print(f"Type \"kill\" to terminate the process") #somehow the subprocess will keep running even if you kill the current process
    if input() == "kill":
        os.system("pkill -9 python3")


    
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("usage: python3 demo.py <# of routers *less than 150> <delay>")
        exit(1)
    main(int(sys.argv[1]), int(sys.argv[2]))