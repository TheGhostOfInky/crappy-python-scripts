# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 02:22:23 2020

@author: TheGhostOfInky
"""
import sys
fname = sys.argv[1]
links = open (fname,"r")
wget = open ("downloader.sh","a")
for line in links:
    field = line.split(";")
    url = field[0]
    nam = field [1]
    name = nam[:-1]
    wget.write ("wget")
    wget.write (" -O ")
    wget.write (name)
    wget.write (' ')
    wget.write (url)
    wget.write ("\n")
    