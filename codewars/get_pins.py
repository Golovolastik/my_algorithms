#  He noted the PIN 1357, but he also said, 
# it is possible that each of the digits he saw could actually be
# another adjacent digit (horizontally or vertically, but not diagonally).
#  E.g. instead of the 1 it could also be the 2 or 4. 
#  And instead of the 5 it could also be the 2, 4, 6 or 8.
#  Can you help us to find all those variations?
#  It would be nice to have a function, 
# that returns an array of all variations for an observed PIN
# with a length of 1 to 8 digits.

def get_pins(observed):
    import numpy as np
    keypad = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9],
                  [np.NaN, 0, np.NaN]])
    expectations = []
    possible_numbers = {}
    def find_possible_numbers():
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
        return arr
    def combinate(arr):
        n = len(arr)
        combinations = []

        # to keep track of next element 
        # in each of the n arrays
        indices = [0 for i in range(n)]
        
        while (1):
            combination = []

            # prcurrent combination
            for i in range(n):
                combination.append(arr[i][indices[i]])
            combinations.append(combination)

            # find the rightmost array that has more
            # elements left after the current element
            # in that array
            next = n - 1
            while (next >= 0 and
                (indices[next] + 1 >= len(arr[next]))):
                next-=1

            # no such array is found so no more
            # combinations left
            if (next < 0):
                return combinations

            # if found move to next element in that
            # array
            indices[next] += 1

            # for all arrays to the right of this
            # array current index again points to
            # first element
            for i in range(next + 1, n):
                indices[i] = 0
    def create_string(arr):
        result = []
        for combo in arr:
            combination = ""
            for number in combo:
                combination += str(number)
            result.append(combination)
        return result
    array = find_possible_numbers()
    array = combinate(array)
    array = sorted(create_string(array))
    return array

PIN = '07'
print(get_pins(PIN))