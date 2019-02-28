import numpy as np
#import pandas as pd

def puntuation(tags_1,tags_2):
    i = np.intersect1d(tags_1,tags_2)
    r1 = np.setdiff1d(tags_1,i)
    r2 = np.setdiff1d(tags_2,i)
    #print(tags_1,tags_2)
    #print('--------------------------------')
    return min(i.size,r1.size,r2.size)


with open("./input/b_lovely_landscapes.txt") as f:
    N = f.readline()
    imgs = []
    res = []
    for i, line in enumerate(f):
    	t, _, *tags = line.split()
    	imgs.append((i, tags, t))
    	#res.append(i)


    #     vlist.append(tuple(map(lambda x: int(x),line.split()+[i])))
    #     i=i+1
    # fl = list(map(lambda x: int(x),f.readline().split()))
param = 2

used = [0]
res.append(0)
while len(res) < len(imgs)-param:
    ran = np.random.choice(np.setdiff1d(list(range(len(imgs))),res),param,False)
    print(ran)
    posibles = []
    for i in ran:
        posibles.append(imgs[i])
    best = list(sorted(list(map(lambda x: (puntuation(imgs[res[-1]][1], x[1]), x[0]), posibles)), key=lambda x: x[0]))
    res.append(best[0][1])
    print(best[0])
    print('---------')


with open("./output/result.txt","w+") as fw:
	fw.write(str(len(res))+"\n")
	#for r in np.random.choice(res,len(res),False):
	#	fw.write(str(r)+"\n")
    # for i in range(0,nc):
    #     strres = ""
    #     for j in range(0,len(result[i])):
    #         strres = strres+" "+str(result[i][j])
    #     fw.write(str(len(result[i]))+strres+"\n")

