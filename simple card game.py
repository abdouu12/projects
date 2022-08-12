import random


def rand(x, y):
    a = random.randint(x,y)
    return a
x =['2','3','4','5','6','7','8','9','10','J','Q','K','A']
cards = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 12,
    "A": 14
}
userinput = int(input("how many cards do you want dealt: "))
mydeck = []
botlist = []
round = userinput
pointsJ= 0
pointsS = 0
for i in range(0, userinput):
    a = rand(0, 12)
    mydeck.append(x[a])
for i in range(0, userinput):
    a = rand(0, 12)
    botlist.append(x[a])

print("your deck is ", mydeck)
for i in range(1, round + 1):
    mychoice = str(input("choose your card: "))
    botchoice = botlist[0]
    if mychoice > botchoice:
        mydeck.remove(mychoice)
        botlist.remove(botchoice)
        print("in the", i, "round ", mychoice, "beats", botchoice, " and you gets 1 point")
        print("your deck is updated to", mydeck)
        pointsS = pointsS + 1

    elif mychoice < botchoice:
        mydeck.remove(mychoice)
        botlist.remove(botchoice)
        print("in the", i, "round ", botchoice, "beats", mychoice, " and bot gets 1 point")
        print("your deck is updated to", mydeck)
        pointsJ = pointsJ + 1

    elif mydeck == botchoice:
        mydeck.remove(mychoice)
        botlist.remove(botchoice)
        print("in the", i, "round ", botchoice, "ties", mychoice, " and no one gets a point")
        print("your deck is updated to", mydeck)

    elif i == round:
     print("game over")
     break
if pointsS > pointsJ:
    print("your points: ", pointsS, "bot points: ", pointsJ)
    print("you win")
elif pointsS < pointsJ:
    print("your points: ", pointsS, "bot points: ", pointsJ)
    print("bot wins")
elif pointsS == pointsJ:
    print("your points: ", pointsS, "bot points: ", pointsJ)
    print("its a tie")
















