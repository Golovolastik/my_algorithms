def battle(player1, player2):
	output = {'player1': [], 'player2': []}
	temp = 0
	if len(player1) > len(player2):
		temp = len(player2)
	else:
		temp = len(player1)
	for i in range(temp):
		if player1[i][0] < player2[i][1]:
			output['player2'].append(player2[i])
	for i in range(temp):
		if player2[i][0] < player1[i][1]:
			output['player1'].append(player1[i])
	if len(player1) > len(player2):
		for i in range(len(player2), len(player1)):
			output['player1'].append(player1[i])
	elif len(player2) > len(player1):
			output['player1'].append(player1[i])

	return output

player1 = [[1, 1], [2, 1], [2, 2], [5, 5]]
player2 = [[1, 2], [1, 2], [3, 3]]

print(battle(player1, player2))