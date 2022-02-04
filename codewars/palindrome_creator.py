string = "blabla"

def create_palindrome(str):
    n = 0
    while str[n:] != str[n:][::-1]:
    	n += 1
    return str + str[:n][::-1]

print(create_palindrome(string))