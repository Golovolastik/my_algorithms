def strange_math(n, k):
	return sorted([str(x) for x in range(1, n+1)]).index(str(k)) + 1

print(strange_math(11, 2))