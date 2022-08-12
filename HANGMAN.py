import random
from testing import stages
wordlist = ["restaurant", "received", "good", "reviews", "expectations", "high", "although", "tasty", "reminded", "pulled", "salad", "house", "german", "street"]
chosenword = random.choice(wordlist)
display = []
print(f"the secret word is {chosenword} ")
for i in range(len(chosenword)):
    display += "_"
print(display)
wordlength = len(chosenword)
endofgame = False
lives = 6
while not endofgame:
   guess = input("pick a letter: ").lower()
   if guess in display:
     print(f"the letter {guess} has already been guessed")
   for position in range(wordlength):

       #to check if the guess is in the chosenword we loop through each letter using the for loop with range of lenth of
       #chosenword
     if chosenword[position] == guess:
         display[position] = guess
   #to keep track of the player's lives
   if guess not in chosenword:
       lives -= 1
       print(f"the letter {guess} is not in the chosen word")
       print(stages[lives])
       if lives == 0:
           print("you lose")
           endofgame = True


   print(f"{''.join(display)}")
   if "_" not in display:
       print("you win")
       endofgame = True
