import numpy as np
import pandas as pd

with open("./b_lovely_landscapes.txt") as f:
    N = f.readline()
    imgs = []
    res = []
    for i, line in enumerate(f):
    	t, _, *tags = line.split()
    	imgs.append((i, tags, t))


actual = imgs[0]
res[0] = 0
while len(imgs) > 0:
	posibles = [img for img in imgs if imgs[0] != actual[0]]  
	list(lambda x: (puntuacion()))

    #     vlist.append(tuple(map(lambda x: int(x),line.split()+[i])))
    #     i=i+1
    # fl = list(map(lambda x: int(x),f.readline().split()))



with open("./result.txt","w+") as fw:
	fw.write(str(len(res))+"\n")
	for r in res:
		fw.write(str(r)+"\n")
    # for i in range(0,nc):
    #     strres = ""
    #     for j in range(0,len(result[i])):
    #         strres = strres+" "+str(result[i][j])
    #     fw.write(str(len(result[i]))+strres+"\n")
