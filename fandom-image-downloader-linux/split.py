# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 01:13:34 2020

@author: TheGhostOfInky
"""
import sys
fname = sys.argv[1]
file = open (fname, "r", encoding='utf-8')
links = open ("links.txt","a")
for line in file:
    field1 = line.split("<li><a href=")
    num = len(field1)
    one = 1
    if num > one:        
        field3 = field1[1]
        field4 = field3.split("class=")
        field5 = field4[0]
        field6 = field5[:-2]
        field7 = field6[1:]
        field8 = field7+"&format=original"
        field9 = field8.split("/images/")
        field10 = field9[1]
        field11 = field10.split("/revision/")
        field12 = field11[0]
        field13 = field12[5:]
        links.write(field8)
        links.write(";")
        links.write(field13)
        links.write ("\n")
links.close()
