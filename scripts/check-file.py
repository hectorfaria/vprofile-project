#!/usr/bin/python3
import os

path = '/tmp/Testfile.txt'

if os.path.isdir(path):
    print(f"{path} is a directory")
elif os.path.isfile(path):
    print(f"{path} is a file")
elif os.path.islink(path):
    print(f"{path} is a link")
else:
    print(f"{path} is an unsupported file")