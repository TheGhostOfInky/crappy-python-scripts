# -*- coding: utf-8 -*-
import sys
fname = sys.argv[1]
file = open (fname, "r", encoding="utf-8")
links = open ("apidownl.txt","a")
for line in file:
    field1 = line.split("/comments/")        
    field2 = field1[1]
    field3 = field2.split("/")
    field4 = field3[0]
    field5 = "https://api.reddit.com/api/info/?id=t3_"+field4
    name = field4+".json"
    links.write(field5)
    links.write(";")
    links.write(name)
    links.write ("\n")
links.close()
