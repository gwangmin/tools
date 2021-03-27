import sock

HOST = '127.0.0.1'
PORT = sock.TEST_PORT


s = sock.sock('udp', log=True)

while True:
    s.send(input('input: '), HOST, PORT)
    print('server: ' + s.recvfrom()[0])

s.close()
