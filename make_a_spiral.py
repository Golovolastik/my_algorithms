# Your task, is to create a NxN spiral with a given size.

import numpy as np

def spiralsize(size):
	import numpy as np
	array = np.zeros((size, size), dtype=int)
	flag = True
	while flag:
		array[0] = 1
		array[:, -1] = 1
		flag = False
	# array[0] = 1
	# array[:, -1] = 1
	# array[-1] = 1
	# array[0+2:, 0] = 1
	# array[0+2, :-1-1] = 1
	# array[0+2:-2, -1-2] = 1
	return array

print(spiralsize(6))

#array = np.random.randint(size=(5, 5), low=0, high=9)
#print(array)
#print(array[0])
#print(array[0][0])
#print(array[:, -1])