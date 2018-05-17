#!/usr/bin/python3

from socket import socket , AF_INET,SOCK_DGRAM
import time


def main():
	

	server=('127.0.0.1',9000)


	s = socket(AF_INET,SOCK_DGRAM)

	# s.bind((host,port))
	

	count = 0

	

	while True:
		
	
		count+=1

		if count>5:
			count=0
			print("Take a short break" )
			time.sleep(5)
			
			



		msg = input("Client : ")

		
		
		s.sendto(msg.encode('utf-8'),server)

			

	s.close()
	

if __name__ == '__main__':
	main()		