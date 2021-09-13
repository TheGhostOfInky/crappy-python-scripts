# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 02:22:23 2020

@author: TheGhostOfInky
"""
import sys
fname = sys.argv[1]
links = open (fname,"r")
pshell = open ("downloader.ps1","a")
for line in links:
    field = line.split(";")
    url = field[0]
    name = field[1]
    pshell.write ("Invoke-WebRequest ")
    pshell.write ('\"')
    pshell.write (url)
    pshell.write ('\"')
    pshell.write (" -OutFile ")
    pshell.write (name)
