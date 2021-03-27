import sock

HOST = ''
PORT = sock.TEST_PORT


s = sock.sock('udp', log=True)
s.bind(HOST, PORT)

while True:
    msg, addr = s.recvfrom()
    s.send(msg, addr[0], addr[1])

s.close()
