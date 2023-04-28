#!/usr/bin/env python3
#name = input("Please Enter your name: ")

#print("Hello, " + name)

#sudo chmod 777 script.py

import sys
import os
#print(sys.argv)


filename = sys.argv[1]

if not os.path.exists(filename):
	with open(filename, 'w') as f:
		f.write("#!/usr/bin/env python3 \n")
else:
	print("ERRROR, this file {} already exists tho!".format(filename))
	sys.exit(1)		
