# -*- coding: utf-8 -*-
import sys
fname = sys.argv[1]
links = open (fname,"r")
pshell = open ("downloader.ps1","a")
pshell.write ("mkdir JSON")
pshell.write ("\n")
for line in links:
    field = line.split(";")
    url = field[0]
    name = field[1]
    pshell.write ("Invoke-WebRequest ")
    pshell.write ('\"')
    pshell.write (url)
    pshell.write ('\"')
    pshell.write ('-OutFile .\\JSON\\')
    pshell.write (name)
