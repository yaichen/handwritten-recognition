import numpy as np
np.save('training',np.array(['traindata/A*.png','traindata/B*.png','traindata/C*.png','traindata/D*.png','traindata/E*.png','traindata/F*.png','traindata/G*.png','traindata/H*.png','traindata/I*.png','traindata/J*.png','traindata/K*.png','traindata/L*.png','traindata/M*.png','traindata/N*.png','traindata/O*.png','traindata/P*.png','traindata/Q*.png','traindata/R*.png','traindata/S*.png','traindata/T*.png','traindata/U*.png','traindata/V*.png','traindata/W*.png','traindata/X*.png','traindata/Y*.png','traindata/Z*.png']))
data = np.load('training.npy')
print(data)
print(len(data))