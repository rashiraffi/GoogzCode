import numpy as np
f = open('ImageData.txt')
triplets=f.read().split()
for i in range(0,len(triplets)): triplets[i]=triplets[i].split(',')
A=np.array(triplets, dtype=np.uint8)
print(A)