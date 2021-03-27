'''
sock.py example
'''

import sock

HOST = '127.0.0.1'
PORT = sock.TEST_PORT


s = sock.sock('tcp', log=True)
s.connect(HOST, PORT)

while True:
    s.send(input('input: ') + '\n') # input() doesn't contain '\n'
    print(s.recv_with_delimiter('\n'))

s.close()
