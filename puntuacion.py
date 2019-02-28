import numpy as np 

def puntuation(tags_1,tags_2):
	i = np.intersect1d(tags_1,tags_2)
	r1 = np.setdiff1d(tags_1,i)
	r2 = np.setdiff1d(tags_2,i)
	return min(i.size,r1.size,r2.size)

with open(file) as f:
    N = f.readline()
    imgs = {}
    res = []
    v = None
    for i, line in enumerate(f):
    	t, _, *tags = line.split()
    	if t == 'V':
    		if v is None:
    			v = (i, tags, -2)
    			continue
    		else:
    			tags = np.union1d(v[1], tags)
    			imgs[i] = (i, tags, v[0])
    			v = None
    	else:
    		imgs[i] = (i, tags, -1)
    	for t in tags:
    		if t in dictags:
    			dictags[t].append(i)
    		else:
    			dictags[t] = [i]


with open("./output/result_d.txt","w+") as fw:
	fw.write(str(len(res))+"\n")
	for r in res.keys():
		if (imgs[r][2] >= 0):
			fw.write(str(r)+" "+str(imgs[r][2])+"\n")
		else:
			fw.write(str(r)+"\n")