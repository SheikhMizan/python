#!/usr/bin/env python3

import subprocess

#subprocess.run(["date"])

#subprocess.run(["sleep", "2"])

#result= subprocess.run(["ls", "this_file_not_exist"])

#print(result.returncode)

# std out
#result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
#print(result.returncode)
#print(result.stdout)
#print(result.stdout.decode().split())


#std error
result = subprocess.run(["rm", "doesn_not_exist"], capture_output=True)
print(result.returncode)
print(result.stderr)
print(result.stderr.decode().split())