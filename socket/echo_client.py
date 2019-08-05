'''
sock.py example
'''

import sock

# Settings
port = 8080


s = sock.sock('tcp')
s.connect('127.0.0.1',port)
while True:
    s.send(input('input: '))
    s.recv()
s.close()

