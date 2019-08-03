'''
Socket wrapper.


How to use socket

Server
1. Create sock().
2. Call bind().
3. Call listen().
4. Call accept().
5. Communication.
6. Call close().

Client
1. Create sock().
2. Call connect().
3. Communication.
4. Call close().
'''

from socket import *


class sock(object):
    '''
    Create TCP or UDP socket and print log.
    '''
	def __init__(self,type_='tcp'):
        '''
        Initializer
        
        type: (Optional) socket type. 'tcp' or 'udp'. Default 'tcp'.
        '''
		self.type = type_
		if type_ == 'tcp':
			self.sock = socket(AF_INET,SOCK_STREAM)
			print('[*] Create TCP socket')
		elif type_ == 'udp':
			self.sock = socket(AF_INET,SOCK_DGRAM)
			print('[*] Create UDP socket')
            
	def bind(self,ip,port):
        '''
        Binding socket to specified address and print log.
        
        ip: Local ip. string.
        port: Local port. int.
        '''
		self.sock.bind((ip, port))
		print('[*] Binding '+ip+':'+str(port))
        
	def listen(self,backlog=3):
        '''
        Listen and print log.
        
        backlog: (Optional) backlog queue size. Default 3.
        '''
		self.sock.listen(backlog)
		print('[*] Listen with backlog queue '+str(backlog))
        
	def accept(self):
        '''
        Accept and print log.
        '''
		client_sock, addr = self.sock.accept()
		print('[*] Accepted',str(addr))
		return client_sock, addr
    
	def connect(self,ip,port):
        '''
        Connect to specified address and print log.
        
        ip: Remote ip. string.
        port: Remote port. int.
        '''
		addr = (ip, port)
		try:
			self.sock.connect(addr)
			print('[*] Connected '+ip+':'+str(port))
		except:
			print('[!] Connection to '+ip+':'+str(port)+' failed')
        
	def send(self,msg,ip=None,port=None):
        '''
        Send message and print log.
        If UDP, require addr.
        
        ip: (udp) Remote ip. string
        port: (udp) Remote port. int
        '''
		if self.type == 'tcp':
			try:
				self.sock.send(msg)
				print('[*] Send: '+msg)
			except:
				print('[!] send() error')
		elif self.type == 'udp':
			addr = (ip,port)
			try:
				self.sock.sendto(msg,addr)
				print('[*] Send: '+msg+' to '+str(addr))
			except:
				print('[!] send() error')
                
	def recv(self,buf_size=1024):
        '''
        Receive data and return. print log.
        
        buf_size: (Optional) Buffer size. Default 1024.
        '''
		if self.type == 'tcp':
			try:
				data = self.sock.recv(buf_size)
				print('[*] Receive:',data)
				return data
			except:
				print('[!] recv() error')
		elif self.type == 'udp':
			try:
				data = self.sock.recvfrom(buf_size)
				print('[*] Receive:',data)
				return data
			except:
				print('[!] recv() error')
                
	def close(self):
        '''
        Close socket and print log.
        '''
		self.sock.close()
		print('[*] Close socket')
        
