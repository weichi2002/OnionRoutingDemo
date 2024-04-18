import sys
import subprocess
import signal
import os


def main(n, delay):
    
    portNumber = 3000
    commands = [
        #add the routers here
        ['python3', 'server.py'],
        ['python3', 'dclient.py', str(n)],
    ]
    
    for _ in range(n):
        portNumber+=1
        cmd = ['python3', "router.py", str(portNumber), str(delay)]
        commands.insert(0, cmd)
        
        
    for cmd in commands:
        
        # try:
        #     p = subprocess.Popen(cmd, start_new_session=True)
        #     p.wait(timeout=timeout_s)
        # except subprocess.TimeoutExpired:
        #     print(f'Timeout for {cmd} ({timeout_s}s) expired', file=sys.stderr)
        #     print('Terminating the whole process group...', file=sys.stderr)
        #     os.killpg(os.getpgid(p.pid), signal.SIGTERM)
        subprocess.Popen(cmd)
        
    if input() == "kill":
        os.system("pkill -9 python3")


    
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("usage: python3 dynamic_demo.py <# of routers has to be less than 150> <possible delay>")
        exit(1)
    main(int(sys.argv[1]), int(sys.argv[2]))