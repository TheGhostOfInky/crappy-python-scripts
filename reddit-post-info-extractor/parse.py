# -*- coding: utf-8 -*-
import json, sys
finaldata = open ("finaldata.txt","a", encoding="utf-8")
fname = sys.argv[1]
with open(fname,'r', encoding="utf-8") as f:
    data = json.load(f)
data1 = (data["data"])
child = (data1["children"])
child1 = child[0]
data2 = (child1["data"])
title = (data2["title"])
upv = (data2["ups"])
upvotes = str(upv)
author = (data2["author"])
slink = (data2["permalink"])
flink = "https://www.reddit.com"+slink
finaldata.write(author)
finaldata.write(";")
finaldata.write(title)
finaldata.write(";")
finaldata.write(flink)
finaldata.write(";")
finaldata.write(upvotes)
finaldata.write("\n")