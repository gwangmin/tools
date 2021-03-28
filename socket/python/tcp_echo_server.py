'''
sock.py example
'''

import sock

HOST = ''
PORT = 8322


serveSock = sock.sock('tcp', log=True)
serveSock.bind(HOST, PORT)
serveSock.listen()
s, addr = serveSock.accept()

while True:
    s.send(s.recv_with_delimiter('\n'))

s.close()
serveSock.close()