'''
Python tcp, udp socket wrapper.
provide log feature
distinct tcp data end
handle data is bytes or string
but not exception handling because of debugging


How to use socket

Server
1. Create sock().
2. Call bind(), listen(), accept().
3. Communication.
4. Call close().

Client
1. Create sock().
2. Call connect().
3. Communication.
4. Call close().
'''

from socket import socket
from socket import AF_INET, SOCK_STREAM, SOCK_DGRAM

class sock(object):
    '''
    tcp, udp socket wrapper

    features:
        - log
        - distinct tcp data end
        - handle data is bytes or string

    methods:
        - __init__(type, log=True, copy=None)
        - bind(host, port)
        - listen(backlog=3)
        - accept()
        - connect(host, port)
        - send(msg, host=None, port=None)
        - recv_fixed_length(length, byte=False)
        - recv_with_delimiter(delimiter, byte=False)
        - recvfrom(bufsize=1024, byte=False)
        - close()
    '''
    def __init__(self, type_='tcp', log=True, copy=None):
        '''
        Initializer
        
        type_: (Optional) Socket type or python socket. 'tcp' or 'udp'. Default 'tcp'.
        log: (Optional) whether print log. default True
        copy: (Optional) if not None, copy(copy creator, for accept method).
        '''
        self.type = type_
        self.log = log
        # copy creator
        if not copy is None:
            self.sock = copy
            return
        if type_ == 'tcp':
            self.sock = socket(AF_INET,SOCK_STREAM)
            print('[*] Create TCP socket')
        elif type_ == 'udp':
            self.sock = socket(AF_INET,SOCK_DGRAM)
            print('[*] Create UDP socket')
        else:
            raise Exception('Only tcp, udp')

    def bind(self, host, port):
        '''
        Binding socket to specified address and print log.
        
        ip: host name or IPv4 addr. string.
        port: port. int.
        '''
        self.sock.bind((host, port))
        if self.log:
            print('[*] Binding ' + host + ':' + str(port))
        
    def listen(self, backlog=3):
        '''
        Listen and print log.
        
        backlog: (Optional) backlog queue size. Default 3.
        '''
        self.sock.listen(backlog)
        if self.log:
            print('[*] Listen with backlog queue ' + str(backlog))
        
    def accept(self):
        '''
        Accept and print log.

        return (sock obj, addr)
        '''
        client_sock, addr = self.sock.accept()
        client_sock = sock('tcp', log=self.log, copy=client_sock)
        if self.log:
            print('[*] Accepted ' + str(addr))
        return client_sock, addr
    
    def connect(self, host, port):
        '''
        Connect to specified address and print log.
        
        host: host name or ipv4 addr. string.
        port: Remote port. int.
        '''
        self.sock.connect((host, port))
        if self.log:
            print('[*] Connected ' + host + ':' + str(port))
            
    def send(self, msg, host=None, port=None):
        '''
        Send message and print log.
        If UDP, require addr.
        
        msg: Message. string or bytes
        host: (udp) remote host. string
        port: (udp) remote port. int
        '''
        if isinstance(msg, str):
            msg = msg.encode()
        # if tcp
        if self.type == 'tcp':
            self.sock.sendall(msg)# sendall arg: bytes, not str
            if self.log:
                print('[*] Send: ' + str(msg))
        # if udp
        elif self.type == 'udp':
            addr = (host, port)
            self.sock.sendto(msg, addr)
            if self.log:
                print('[*] Send: ' + str(addr) + '; ' + str(msg))

    def recv_fixed_length(self, length, byte=False):
        '''
        Receive fixed length data and print log

        length: data length (unit: bytes)
        byte: (Optional) whether - return type is bytes. default False(str)

        Return: received data
        '''
        if not self.type == 'tcp':
            raise Exception('recv_fixed_length is only for tcp')

        buf = b''
        for _ in range(length):
            buf += self.sock.recv(1)
        if not byte:
            buf = buf.decode()
        if self.log:
            print('[*] Recv: ' + str(buf))
        return buf

    def recv_with_delimiter(self, delimiter, byte=False):
        '''
        Receive data and print log.
        
        delimiter: this param represents data end.
        byte: (Optional) whether - return type is bytes. default False(str)

        Return: received data(contains delimiter)
        '''
        if not self.type == 'tcp':
            raise Exception('recv_with_delimiter is only for tcp')
        
        if isinstance(delimiter, str):
            delimiter = delimiter.encode()
        buf = b''
        while True:
            buf += self.sock.recv(1)
            if buf.endswith(delimiter):
                break
        if not byte:
            buf = buf.decode()
        if self.log:
            print('[*] Recv: ' + str(buf))
        return buf

    def recvfrom(self, bufsize=1024, byte=False):
        '''
        Receive data and print log.
        
        bufsize: (Optional) buffer size. default 1024
        byte: (Optional) whether - return type is bytes. default False(str)

        Return: received string, addr pair
        '''
        if not self.type == 'udp':
            raise Exception('recvfrom is only for udp')

        bytes_, addr = self.sock.recvfrom(bufsize)
        if not byte:
            data = bytes_.decode()
        if self.log:
            print('[*] Recvfrom: ' + str(addr) + '; ' + str(data))
        return data, addr
                
    def close(self):
        '''
        Close socket and print log.
        '''
        self.sock.close()
        if self.log:
            print('[*] Close socket')


