import sock

HOST = ''
PORT = 8322


s = sock.sock('udp', log=True)
s.bind(HOST, PORT)

while True:
    msg, addr = s.recvfrom()
    s.send(msg, addr[0], addr[1])

s.close()
