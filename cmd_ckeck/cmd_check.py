import os



def check(cmd):
	path=''
	found=0
	status = os.system('echo $PATH >path.txt')
	if status == 0:
		f =open('path.txt','r')
		path = f.read()
		f.close()
	# cmd=input("enter command : ")

	path = path.split(':')	

	for i in path:
		try:
			if cmd in os.listdir(i):
				# print('Command found')
				print(i)
				found=1
				break
				
		except:
			pass		 



	if found==0:
		return'Command not found'
	else:
		return'Command found'



# print("Hello")
# print(check())		