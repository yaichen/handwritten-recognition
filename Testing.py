#test part
import cv2
import numpy as np
import sys
ltrs = np.load('modellt.npy')
noofele = np.load('modelcnt.npy')
#noim = np.load('var.npy')	
noim= 5
alpha = np.load('alphabets.npy')
test = cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE)
dis = cv2.imread(sys.argv[1],-1)
#test=cv2.imread('testdata/test.png',cv2.IMREAD_GRAYSCALE)
r = 13.0 / test.shape[1]
dim = (13, int(test.shape[0] * r))	 
imtest = cv2.resize(test, dim, interpolation = cv2.INTER_AREA)
sub = np.zeros([20,13], dtype =np.int)
lol=[None]*len(alpha)

for l in range(0,len(alpha)):
	imt=np.array(imtest)
	suma=ltrs[l]
	for i in range(imt.shape[0]):
		for j in range(imt.shape[1]):
			if imt[i,j] < 255:
				imt[i,j]=noim
			else:
				imt[i,j]=0
			sub[i,j]=suma[i,j]-imt[i,j]		
	#print (imtc)
	#print (imt.shape, imt.dtype)
	ttelecount = [None] * noim
	for c in range(0,noim):
		newcount=0
		for i in range(imt.shape[0]):
			for j in range(imt.shape[1]):
				if sub[i,j]== (noim-c):	
					newcount=newcount+1
		ttelecount[c]=newcount
	#unique, counts = np.unique(sub,return_counts=True)
	#dict(zip(unique, counts))
	#telecount = [None] * noim
	#rev=counts[::-1]
	#for k in range(0,noim):
	#	telecount[k]=rev[k]


	#i need to subtract telecount from elecount
	#print(noofele[l]) #print(counts)
	#print(ttelecount) #need this for operations
	print (suma)
	#print (count5,count4,count3,count2,count1)
	#print (count5*5+count4*4+count3*3+count2*2+count1)
	print (sub)
	elecount=noofele[l]
	modcount=[None]*noim
	for m in range(0,noim):
		modcount[m]=(elecount[m]-ttelecount[m])*(noim-m)
	print (modcount)
	lol[l]=sum(modcount)
	print(lol[l])
	 #i need this for alll 26 letters

answer = lol.index(max(lol))
print ("The Model predicts the Letter to be :", alpha[answer])
cv2.imshow('Prediction',imtest)
#print (tcount5,tcount4,tcount3,tcount2,tcount1)
#final=((count5-tcount5)*5) + ((count4-tcount4)*4)+((count3-tcount3)*3)+((count2-tcount2)*2)+(count1-tcount1)
#print (final)	
cv2.putText(dis,alpha[answer],(90,195),2,2,(200,120,155),7,cv2.LINE_AA)
cv2.imshow('test character',dis)

cv2.waitKey(0)
cv2.destroyAllWindows()