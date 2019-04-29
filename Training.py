from glob import glob
import cv2
import numpy as np
import matplotlib.pyplot as plt
data = np.load('traindata/training.npy')
ltrs=[None]*len(data)
noofele=[None]*len(data)
weight=[None]*len(data)
for l in range(0,len(data)):
	#abc='traindata/A*.png'
	img_names = glob(data[l])
	suma = np.zeros([20,13], dtype =np.int)
	noim=0
	for d in img_names:
		img = cv2.imread(d,cv2.IMREAD_GRAYSCALE)
		r = 13.0 / img.shape[1]	
		dim = (13, int(img.shape[0] * r))	 
		train = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
		im = np.array(train)
		for i in range(im.shape[0]):
			for j in range (im.shape[1]):
				if im[i,j] < 255:
					im[i,j]=1
				else:
					im[i,j]=0
				suma[i,j]=im[i,j]+suma[i,j]				
	
		noim=noim+1
	#THIS SHOULD WORK
	ltrs[l]=suma 
	unique, counts = np.unique(suma,return_counts=True)
	dict(zip(unique, counts))
	rev=counts[::-1]
	#print(rev)
	#print(noim)
	elecount=[None]*noim
	for k in range(0,noim):
		elecount[k] = rev[k] 	
	#THIS SHOULD WORK
	idk=0
	for w in range(0,noim):
		idk=idk+elecount[w]*(noim-w)
	weight[l]=idk
	noofele[l]=elecount   ##i want to put elecount in 26 arrays
	#print (suma)       # store this in model file. calc prediction
	#print(elecount)  #store this in model file. This will identify the character A
################################################################################
print("THE TRAINING MODEL IS CREATED")
np.save('modellt',ltrs)
np.save('modelcnt',noofele)
np.save('var',noim)
np.save('weight',weight)


