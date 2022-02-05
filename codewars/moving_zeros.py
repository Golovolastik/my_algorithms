def move_zeros(list):
	for number in list:
		if number == 0:
			list.remove(number)
			list.append(number)
	return list

print(move_zeros([1,2,3,0,4,0,5]))