'''
sock.py example
'''

import sock


# Settings
port = 8080


serveSock = sock.sock('tcp')
serveSock.bind('127.0.0.1',port)
serveSock.listen()
s,addr = serveSock.accept()

while True:
    s.send(s.recv())
serveSock.close()
s.close()

