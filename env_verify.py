#!/usr/bin/env python
import os

os.system("echo $PYTHONPATH")

test1 = os.path.exists("/home/pi/python_modules/serial_utils.py")

if test1:
    print("serial_utils.py is in ~/python_modules <-- bad")
else:
    print("serial_utils.py is not in ~/python_modules <-- good")


test2 = os.path.exists("/home/pi/SBR_git/serial_utils.py")
    
if test2:
    print("serial_utils.py is in ~/SBR_git <-- good")
else:
    print("serial_utils.py is not in ~/SBR_git <-- bad")
