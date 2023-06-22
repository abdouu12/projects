import random

def bot_choice(a):
    a = random.randint(1,2)
    if a == 1:
        return a
    elif a == 2:
        return a

cards = [random.randint(1,10), random.randint(1,10)]
bot_cards = [random.randint(1,10), random.randint(1,10)]
end_of_BJ = False
end_of_hit = False
while end_of_BJ is False:
    yes_or_no = str(input("do you want to play black jack? y/n  "))

    if yes_or_no == "y":
     print("your card are", cards)
     print("the bot's first card is: ", bot_cards[0])
     while end_of_hit is False:
         hit = str(input("do you want to hit or stay: "))
         if hit == "hit":
              cards.append(random.randint(1,10))
              print("your new cards are: ",cards)
              if bot_choice(50)== 1:
                  bot_cards.append(random.randint(1,10))
              elif bot_choice(50)== 2:
                  bot_cards = bot_cards

              continue
         elif hit == "stay":
             print("your final cards are: ", cards)
             if bot_choice(50) == 1:
                 bot_cards.append(random.randint(1, 10))
             elif bot_choice(50) == 2:
                 bot_cards = bot_cards
             print("bot's final cars are" , bot_cards)

             if sum(cards)>21:
                 print("you lost")
             elif sum(cards)<21 and sum(cards)>sum(bot_cards):
                 print("you win")
             else:
                   print("you win")
         end_of_hit = True

    elif yes_or_no == "n":
        end_of_BJ = True

























