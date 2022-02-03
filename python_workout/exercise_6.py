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
