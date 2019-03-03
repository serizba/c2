import numpy as np
from tqdm import tqdm

def puntuation(tags_1,tags_2):
	i = np.intersect1d(tags_1,tags_2)
	r1 = np.setdiff1d(tags_1,i)
	r2 = np.setdiff1d(tags_2,i)
	return min(i.size,r1.size,r2.size)



file = './input/newdae'
# Dictionary storing images {id_image : (id_image, tags_image, vertical_pair)}
imgs = {}
# Dictionary storing tags {tag_id : [id_image]}
tags = defaultdict(list)

# Read and parse input file
with open(file) as f:
	# Ignore first line
    f.readline()
    v = None
    for i, line in enumerate(f):
    	t, _, *tags_img = line.split()
    	if t == 'V':
    		if v is None:
    			v = (i+N, tags, -2)
    			continue
    		else:
    			tags = np.union1d(v[1], tags)
    			imgs[i] = (i, tags, v[0])
    			v = None
    	else:
    		imgs[i] = (i, tags, -1)
    	for t in tags:
    			dictags[t].append(i)

res = {}
last = None
for i in imgs.keys():
	if i in imgs:
		res[i] = 1
		last = i
		break



while len(res) < len(imgs):
	print(len(imgs), len(res))
	for tag in imgs[last][1]:
		# for i in dictags[tag]:
		# 	print(i, len(imgs))
		# print('caca')
		if len(dictags[tag]) > 1000:
			posibles = [imgs[i] for i in np.random.choice(dictags[tag], 1000, False) if not i in res]
		else:
			posibles = [imgs[i] for i in dictags[tag] if not i in res]
		#posibles = np.random.choice(np.array(posibles), 200, False)
		#posibles = [imgs[i] for i in posibles]
		#print(len(posibles))
		if len(posibles) > 0:
			break



	if len(posibles) == 0:
		for i, v in imgs.items():
			if i not in res:
				posibles = [v]
				break

	if len(posibles) == 0:
		break

	#if (len(res) / 100 == 0):
	#print(len(imgs), len(posibles))

	last = max(posibles, key=lambda x: puntuation(imgs[last][1], x[1]))[0]
	#print(last)
	#last = last[1]
	res[last] = 1

with open("./output/result-ae.txt","w+") as fw:
	fw.write(str(len(res))+"\n")
	for r in res.keys():
		if (imgs[r][2] >= 0):
			fw.write(str(r)+" "+str(imgs[r][2])+"\n")
		else:
			fw.write(str(r)+"\n")
    # for i in range(0,nc):
    #     strres = ""
    #     for j in range(0,len(result[i])):
    #         strres = strres+" "+str(result[i][j])
    #     fw.write(str(len(result[i]))+strres+"\n")
