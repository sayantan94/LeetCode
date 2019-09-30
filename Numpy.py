import numpy as np 
# Printing random indices
rand_idx = np.random.choice(4, 4)
print (rand_idx)
print (rand_idx.shape)

a = np.arange(10)
print (a)
print (a[rand_idx])

test = [1,2,4,5]
y = []
y_train_folds = [ y_train[range_split[i]] for i in range(num_folds)]