import random
def card_dealer(num_cards):
    cards = []
    for i in range(num_cards):
        cards.append(random.randint(1,10))
    return cards
def hitting(players_hand):
    new_card = random.randint(1,10)
    players_hand.append(new_card)
    return players_hand
def bot_choice(bot_cards):
    choice = random.randint(1,2)
    if choice == 1:
        return hitting(bot_cards)
    elif choice == 2:
        return bot_cards
def check_winning(my_cards,bot_cards):
    if sum(my_cards) == 21:
        print("you win")
    elif sum(my_cards) >21:
        print("you lose")
    elif sum(my_cards) <21 and sum(my_cards)>sum(bot_cards):
        print("you win")
    elif sum(my_cards) <21 and sum(my_cards)<sum(bot_cards):
        print("you lose")
my_cards = card_dealer(num_cards=2)
bot_cards = card_dealer(num_cards=2)
end_of_game = False

while end_of_game == False:
   start = str(input("do you want to play blackjack: "))
   if start =="y":
     print(f"your cards are:  {my_cards} ")
     print(f"the first card of the bot is: {bot_cards[0]}")
     hit_or_stay = False
     while not hit_or_stay:
         start2 = str(input("do you want to hit or stay: "))
         if start2 == "hit":
             my_cards = hitting(my_cards)
             print(f"your new cards are {my_cards}")
             bot_cards = bot_choice(bot_cards)
             print(f"thebot's cards are {bot_cards}")
         elif start2 == "stay":
             bot_cards = bot_choice(bot_cards)
             check_winning(my_cards, bot_cards)
             hit_or_stay = True
     my_cards = card_dealer(num_cards=2)  # Reset player cards
     bot_cards = card_dealer(num_cards=2)  # Reset bot cards
   elif start == "n":
        end_of_game = True











