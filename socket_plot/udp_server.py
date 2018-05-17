#!/usr/bin/python3

from socket import socket , AF_INET,SOCK_DGRAM



X=[]      ## Hi
Y=[]	  ## Hello



def server():
	host = '127.0.0.1'
	port = 9000

	s=socket(AF_INET,SOCK_DGRAM)
	s.bind((host,port))

	print("Server started : ")

	dataset=[]
	raw_data=[]
	count=1

	while True:
		
		data,addr = s.recvfrom(1024)
		

		data=data.decode('utf-8')
		print("msg : "+ data)
		dataset = data.split()
		

		keys = list(set(dataset))

		values={'hello':0,'hi':0}

		for i in keys: 
			values[i]=data.count(i)

		raw_data.append(values)	

		if count>4:
			count=0
			# print("Take a break" )
			# print(raw_data)
			# time.sleep(10)
			break

		count+=1	
		
	



	for i in raw_data:
		# for j in i:
		# print(list(i.values())[0])
		# print(list(i.values())[1])
		# x.append(list(i.values())[0])
		# y.append(list(i.values())[1])
		X.append(i['hi'])
		Y.append(i['hello'])

	# print('Hi : ',sep=' ')
	# print(X)
	# print("*****************")
	# print('Hello : ',sep=' ')
	# print(Y)
	s.close()
