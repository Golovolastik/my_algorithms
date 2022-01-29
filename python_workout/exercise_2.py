#sum function
def mysum(*numbers):
	result = 0
	for number in numbers:
		result += number
	return result

print(mysum(10, 20, 30, 40))

#arithmetic mean
def average(*numbers):
	result = 0
	for number in numbers:
		result += number
	avg = result / len(numbers)
	return avg

print(average(10, 20, 30, 40))

#the shortest word, the length of the longest word, and the average word length
def str_analyzing(*words):
	shortest = len(words[0])
	longest = 0
	total_len = 0
	avg_len = 0
	for word in words:
		if len(word) < shortest:
			shortest = len(word)
		if len(word) > longest:
			longest = len(word)
		total_len += len(word)
	avg_len = total_len / len(words)
	return (shortest, longest, avg_len)

print(str_analyzing("Hello", "World", "Earth", "People", "Children"))

#Sum the objects that either are integers or can be turned into integers
def last_func(*objects):
	result = 0
	for obj in objects:
		try:
			result += int(obj)
		except:
			pass
	return result

print(last_func(1, 2, "Hello", "4", "5", "World"))

