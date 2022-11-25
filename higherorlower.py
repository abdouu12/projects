import random
def rand(x,y):
    a = random.randint(x,y)
    return a
x = int(input("choose the first end of the guessing bounder: "))
y = int(input("choose the second end of the guessing bounder: "))
secretnumber = rand(x,y)
guesses = int(input("how many guesses would you like to have: "))
while True:
    choice = int(input("guess the number: "))
    if choice >= y or choice <= x:
        print("out of bounderies")
        continue
    elif guesses == 0:
        print(f"out of guesses \n the correct number was  {secretnumber}")
        break
    elif choice < secretnumber:
        print(f" guess higher \n you have {guesses} guesses left")
        guesses = guesses - 1

    elif choice > secretnumber:
        guesses = guesses - 1
        print(f"guess lower \n you have {guesses} guesses left")

    elif choice == secretnumber:
     print(f"the number {secretnumber} was guessed correctly ")
     break


BOT CODE :

import random
def rand(x , y):
    a = random.randint(x, y)
    return a

def bot_guess(x,y):
 x = int(input("choose the first end of the guessing bounder: "))
 y = int(input("choose the second end of the guessing bounder: "))
 secretnumber = rand(x, y)
 botchoice = rand(x, y)

 while True:


     if botchoice == secretnumber:
         print(f"the bot has won \n the correct number was {secretnumber}")
         break

     elif botchoice > secretnumber:
         botchoice = botchoice - 1

     elif botchoice < secretnumber:
         botchoice = botchoice + 1


bot_guess(1,10)
