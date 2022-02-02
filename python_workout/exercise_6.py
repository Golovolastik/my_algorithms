def pig_latin_sentence(sent):
	words = sent.split()
	output = []
	vovel = ('a', 'e', 'i', 'o', 'u')
	for word in sent.split():
		if word[0] in vovel:
			output.append(f"{word}way")
		else:
			output.append(f"{word[1:]}{word[0].lower()}ay")
	return " ".join(output)

print(pig_latin_sentence('this is a test translation'))

#additional exercise
def bla_bla(list):
	print(len(list))
	temp = []
	output = [[]]*len(list)
	print(output)
	for string in list:
		temp.append(string.split())
		temp
	for i, string in enumerate(list):
		output[i].append(temp[i])
	print(output)

print(bla_bla(['abc def ghi','jkl mno pqr','stu vwx yz']))