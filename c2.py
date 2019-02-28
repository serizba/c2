import numpy as np
from tqdm import tqdm
def puntuation(tags_1,tags_2):
	i = np.intersect1d(tags_1,tags_2)
	r1 = np.setdiff1d(tags_1,i)
	r2 = np.setdiff1d(tags_2,i)
	return min(i.size,r1.size,r2.size)

dictags = {}

# #file = './input/b_lovely_landscapes.txt'
# file = "./input/c_memorable_moments.txt"
# with open(file) as f:
#     N = f.readline()
#     imgs = []
#     res = []
#     v = None
#     for i, line in enumerate(f):
#     	t, _, *tags = line.split()
#     	if t == 'V':
#     		if v is None:
#     			v = (i, tags, -2)
#     			continue
#     		else:
#     			tags = np.union1d(v[1], tags)
#     			imgs.append((i, tags, v[0]))
#     			v = None
#     	else:
#     		imgs.append((i, tags, -1))
#     	for t in tags:
#     		if t in dictags:
#     			dictags[t].append(i)
#     		else:
#     			dictags[t] = [i]
    
#file = './input/b_lovely_landscapes.txt'
#file = "./input/c_memorable_moments.txt"
#file = './input/d_pet_pictures.txt'
file = './input/e_shiny_selfies.txt'
# with open(file) as f:
#     N = f.readline()
#     imgs = []
#     res = []
#     v = None
#     for i, line in enumerate(f):
#     	t, _, *tags = line.split()
#     	if t == 'V':
#     		if v is None:
#     			v = (i, tags, -2)
#     			imgs.append([None])
#     			continue
#     		else:
#     			tags = np.union1d(v[1], tags)
#     			imgs.append((i, tags, v[0]))
#     			v = None
#     	else:
#     		imgs.append((i, tags, -1))
#     	for t in tags:
#     		if t in dictags:
#     			dictags[t].append(i)
#     		else:
#     			dictags[t] = [i]

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

res = {}
last = None
for i in range(len(imgs)):
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
		if len(dictags[tag]) > 200:
			posibles = [imgs[i] for i in np.random.choice(dictags[tag], 200, False) if not i in res]
		else:
			posibles = [imgs[i] for i in dictags[tag] if not i in res]
		#posibles = np.random.choice(np.array(posibles), 200, False)
		#posibles = [imgs[i] for i in posibles]
		#print(len(posibles))
		if len(posibles) > 0:
			break



	if len(posibles) == 0:
		for i, v in imgs.items():
			if and i not in res:
				posibles = [v]
				break

	if len(posibles) == 0:
		break

	#if (len(res) / 100 == 0):
	#print(len(imgs), len(posibles))

	last = max(list(map(lambda x: (puntuation(imgs[last][1], x[1]), x[0]), posibles)), key=lambda x: x[0])
	#print(last)
	last = last[1]
	res[last] = 1



# res.append(0)
# while len(imgs) > 0:
# 	posibles = [img for img in imgs if not imgs[0] in res]
# 	#print("caca")  
# 	best = list(sorted(list(map(lambda x: (puntuation(imgs[res[-1]][1], x[1]), x[0]), posibles)), key=lambda x: x[0]))[0][1]
# 	print(best)
# 	res.append(best)
    #     vlist.append(tuple(map(lambda x: int(x),line.split()+[i])))
    #     i=i+1
    # fl = list(map(lambda x: int(x),f.readline().split()))

# P = np.ones((10000, 10000), dtype=int) * -1
# P[:,0] = 0
# S = np.zeros((10000, 10000), dtype=int)
# S[:,0] = np.arange(10000)

# for i in tqdm(range(1,10000)):
# 	for j in range(1,i+1):
# 		anyadir = P[i-1,j-10] + puntuation(imgs[S[i-1, j-1]][1], imgs[i][1])
# 		noany = P[i-1, j]
# 		P[i,j] = max(anyadir, noany)
# 		if anyadir > noany:
# 			S[i,j] = i
# 		else:
# 			S[i,j] = S[i-1, j]

# print(i)

# Reconstruir


with open("./output/resulte.txt","w+") as fw:
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
