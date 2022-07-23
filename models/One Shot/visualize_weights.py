from numpy import savetxt  # Save as human readable
import numpy as np  # Define the info to extract
import h5py
keys = []
with h5py.File("middle_model_v1.h5", 'r') as f:  # open file
    f.visit(keys.append)  # append all keys to list
    for key in keys:
        if ':' in key:  # contains data if ':' in key
            print(f[key].name)

f = h5py.File("middle_model_v1.h5", 'r')

group = f[key]
b4 = group['/dense/dense/bias:0'][:]
k4 = group['/dense/dense/kernel:0'][:]
K4 = np.transpose(np.array(k4))  # Process

f.close()  # Close key

savetxt('b4.csv', b4, delimiter=',')
savetxt('w4.csv', K4, delimiter=',')

# print(keys)
