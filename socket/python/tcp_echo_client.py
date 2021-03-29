'''
sock.py example
'''

import sock

HOST = '127.0.0.1'
PORT = 8322


s = sock.sock('tcp', log=True)
s.connect(HOST, PORT)

while True:
    s.send(input('input: ') + '\n') # input() doesn't contain '\n'
    print(s.recv_with_delimiter('\n'))
    #print(s.recv_fixed_length(3))

s.close()
