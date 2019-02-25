#!/usr/bin/python

## Mihir Patel
## 2/25/19
## A program that determines if a directory 
## exists.
## File : does_dir_exist.py
## Version : Python2

import os

#################################################################
def main():
#################################################################
    if os.path.isdir('/tmp'):
        print "Directory exists."
    else:
        print "Directory does not exists."
# main()

if __name__ == "__main__":
    main()

