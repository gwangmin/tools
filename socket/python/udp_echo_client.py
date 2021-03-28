import sock

HOST = '127.0.0.1'
PORT = 8322


s = sock.sock('udp', log=True)

while True:
    s.send(input('input: '), HOST, PORT)
    print('server: ' + s.recvfrom()[0])

s.close()
