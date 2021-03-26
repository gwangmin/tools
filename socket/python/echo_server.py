'''
sock.py example
'''

import sock

port = sock.TEST_PORT


serveSock = sock.sock('tcp', log=True)
serveSock.bind('', port)
serveSock.listen()
s, addr = serveSock.accept()

while True:
    s.send(s.recv_with_delimiter('\n'))

s.close()
serveSock.close()
