from socket import *
import threading
import time
import sys
time.sleep(10)
def recv():
	while True:
		s=socket(AF_INET,SOCK_STREAM)
		s.connect((sys.argv[1] ,5747))
		s1=''
		while True:
			msg=(s.recv(8).decode('utf-8'))
			s1+=msg
			if len(msg)<=0:
				s.close()
				print(s1)
				break
def send():
	s=socket(AF_INET,SOCK_STREAM)
	s.bind((gethostname(),5743))
	s.listen(5)
	while True:
		s1=input('>>>')
		conn,addr=s.accept()
		conn.send(bytes(s1.encode('utf-8')))
		conn.close()

t1=threading.Thread(target=recv)
t1.start()
t2=threading.Thread(target=send)
t2.start()
