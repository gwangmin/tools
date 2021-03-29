'''
sock.py example
'''

import sock

HOST = ''
PORT = 8322


servSock = sock.sock('tcp', log=True)
servSock.bind(HOST, PORT)
servSock.listen()
s, addr = servSock.accept()

while True:
    s.send(s.recv_with_delimiter('\n'))
    #s.send(s.recv_fixed_length(3))

s.close()
servSock.close()
