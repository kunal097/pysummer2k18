#!/usr/bin/python3


import udp_server
import time


import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib import style

style.use('dark_background')

while True:

	udp_server.server()

	x1 = np.array(udp_server.X )
	y1 = np.array(udp_server.Y )
	# print(x1)

	plt.scatter(x1,y1,color='g',linewidths=1)
	plt.xlabel('Hi')
	plt.ylabel('Hello')
	plt.scatter(x1,y1)

	print("Analysing")

	plt.show()
	
	
	plt.close()
