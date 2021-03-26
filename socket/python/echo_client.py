'''
sock.py example
'''

import sock

port = sock.TEST_PORT


s = sock.sock('tcp', log=True)
s.connect('127.0.0.1', port)

while True:
    s.send(input('input: ') + '\n')
    print(s.recv_with_delimiter('\n'))

s.close()
