import random

# random

#print(help(random))

low = 1
high = 20

number = random.randint(low, high)                       # imtinai

print(number)

# print(random.random())                                   # nuo 0 iki 1  - 16 skaitmenu po kablelio
options = ["Rock", "Paper", "Scissors"]
print(random.choice(options))

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
random.shuffle(cards)
print(cards)