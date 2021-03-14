#  He noted the PIN 1357, but he also said, 
# it is possible that each of the digits he saw could actually be
# another adjacent digit (horizontally or vertically, but not diagonally).
#  E.g. instead of the 1 it could also be the 2 or 4. 
#  And instead of the 5 it could also be the 2, 4, 6 or 8.
#  Can you help us to find all those variations?
#  It would be nice to have a function, 
# that returns an array of all variations for an observed PIN
# with a length of 1 to 8 digits.

import numpy as np
keypad = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9],
                   [np.NaN, 0, np.NaN]])

def get_pins(observed):
    expectations = []
    possible_numbers = {}
    for pos, number in enumerate(observed):
        possible_numbers[pos] = []
        result = np.where(keypad == int(number))
        x, y = result[-1][0], result[0][0]
        possible_numbers[pos].append((int(number)))
        if x < 2:
            try:
                number1 = keypad[y][x+1]
                possible_numbers[pos].append((int(number1)))
            except:
                pass
        if x > 0:
            try:
                number2 = keypad[y][x-1]
                possible_numbers[pos].append((int(number2)))
            except:
                pass
        if y < 3:
            try:
                number3 = keypad[y+1][x]
                possible_numbers[pos].append((int(number3)))
            except:
                pass
        if y > 0:
            try:
                number4 = keypad[y-1][x]
                possible_numbers[pos].append((int(number4)))
            except:
                pass
    arr = [possible_numbers[idx] for idx in range(len(possible_numbers))]
    combined_array = np.array(np.meshgrid(arr)).T.reshape(-1, len(arr))

    return 'hello' 

PIN = '87'
print(keypad)
print(get_pins(PIN))