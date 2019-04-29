import numpy as np
np.save('alphabets',np.array(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']))
data = np.load('alphabets.npy')
print(data)
print(len(data))