#
#   Authors: Sergio Izquierdo Barranco and Julia Guerrero Viu - c2.py team
#   Date: 28/02/2019
#   Description: Code used to solve Hash Code contest from Google, Online Qualification Round. 
#                Total number of points obtained: 866.508
#

import numpy as np
from collections import defaultdict
from tqdm import tqdm
import sys

# Score of two list of images
def score(tags_1,tags_2):
	i = np.intersect1d(tags_1,tags_2)
	r1 = np.setdiff1d(tags_1,i)
	r2 = np.setdiff1d(tags_2,i)
	return min(i.size,r1.size,r2.size)


file_input = sys.argv[1]
file_output = sys.argv[2]
# Dictionary storing images {id_image : (id_image, tags_image, vertical_pair)}
imgs = {}
# Dictionary storing tags {tag_id : [id_image]}
tags = defaultdict(list)

# Read and parse input file
with open(file_input) as f:
	# Ignore first line
    f.readline()

    v = None
    for i, line in enumerate(f):
    	t, _, *img_tags = line.split()
    	if t == 'V':
    		if v is None:
    			v = (i, img_tags, -2)
    			continue
    		else:
    			img_tags = np.union1d(v[1], img_tags)
    			imgs[i] = (i, img_tags, v[0])
    			v = None
    	else:
    		imgs[i] = (i, img_tags, -1)
    	for t in img_tags:
    		tags[t].append(i)


# Set with the images of the result (with order)
res = set()
# Last processed image
last = next(iter(imgs))
res.add(last)

# avoid to use a sample if possible (just for eficiency)
num_samples = 500

pbar = tqdm(total=len(imgs))
while len(res) < len(imgs):

	# Search images that share tags with last
	for tag in imgs[last][1]:
		if len(tags[tag]) > num_samples:
			posibles = [imgs[i] for i in np.random.choice(tags[tag], num_samples, False) if not i in res]
		else:
			posibles = [imgs[i] for i in tags[tag] if not i in res]

		if posibles:
			break
	else:
		# If no images sharing tags are found get next image
		try:
			posibles = next(i for i, v in imgs.items() if i not in res)
			print(len(posibles))
		except:
			break

	# Image with higher score with last
	last = max(posibles, key=lambda x: score(imgs[last][1], x[1]))[0]
	res.add(last)

	pbar.update(1)

pbar.close()

#  Write the result
with open(file_output,"w+") as fw:
	fw.write(str(len(res))+"\n")
	for r in res:
		if (imgs[r][2] >= 0):
            # vertical pair of images
			fw.write(str(r)+" "+str(imgs[r][2])+"\n")
		else:
            # horizontal image
			fw.write(str(r)+"\n")