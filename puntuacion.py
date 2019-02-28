import numpy as np 

def puntuation(tags_1,tags_2):
	i = np.intersect1d(tags_1,tags_2)
	r1 = np.setdiff1d(tags_1,i)
	r2 = np.setdiff1d(tags_2,i)
	return min(i.size,r1.size,r2.size)
