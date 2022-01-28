def guessing_game():
       from random import randint
       print("Guess the number between 0 and 100")
       print("You have 5 attempts")
       number = randint(0, 101)
       count = 0
       while True:
              answ = int(input("Enter the answer: "))
              count += 1
              if answ < number:
                     print("Too small")
              if answ > number:
                     print("Too big")
              if answ == number:
                     print("You are right")
                     break
              if count == 5:
                     print(f"All attempts was used. Guessed number was {number}")
                     break
guessing_game()