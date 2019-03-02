#
#   Authors: Sergio Izquierdo Barranco and Julia Guerrero Viu - c2.py team
#   Date: 28/02/2019
#   Description: Code used to solve Hash Code contest from Google, Online Qualification Round. 
#                Total number of points obtained: 866.508
#

import numpy as np
from tqdm import tqdm

def puntuation(tags_1,tags_2):
	i = np.intersect1d(tags_1,tags_2)
	r1 = np.setdiff1d(tags_1,i)
	r2 = np.setdiff1d(tags_2,i)
	return min(i.size,r1.size,r2.size)

dictags = {}
file_input = './input/b_lovely_landscapes.txt'
file_output = './output/result_b.txt'

with open(file_input) as f:
    N = int(f.readline())
    imgs = {} # for each image store: id, list of tags, id of pair image (in case of vertical image, -1 if horizontal)
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

        # create inverse index: dictionary with tags and their list of images    
    	for t in tags:
    		if t in dictags:
    			dictags[t].append(i)
    		else:
    			dictags[t] = [i]

res = {}
last = None
for i in imgs.keys():
	if i in imgs:
		res[i] = 1
		last = i
		break

# avoid to use a sample if possible (just for eficiency)
num_samples = 50000000000000000

while len(res) < len(imgs):
	# print(len(imgs), len(res))
	for tag in imgs[last][1]:
		if len(dictags[tag]) > num_samples:
			posibles = [imgs[i] for i in np.random.choice(dictags[tag], num_samples, False) if not i in res]
		else:
			posibles = [imgs[i] for i in dictags[tag] if not i in res]

		if len(posibles) > 0:
			break


	if len(posibles) == 0:
		for i, v in imgs.items():
			if i not in res:
				posibles = [v]
				break

	if len(posibles) == 0:
		break

	last = max(posibles, key=lambda x: puntuation(imgs[last][1], x[1]))[0]
	res[last] = 1


with open(file_output,"w+") as fw:
	fw.write(str(len(res))+"\n")
	for r in res.keys():
		if (imgs[r][2] >= 0):
            # vertical pair of images
			fw.write(str(r)+" "+str(imgs[r][2])+"\n")
		else:
            # horizontal image
			fw.write(str(r)+"\n")