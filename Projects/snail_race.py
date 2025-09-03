import turtle
import time
import random

WIDTH, HEIGHT = 800, 600
COLORS = ['red', 'blue', 'green', 'black', 'pink', 'purple', 'lime', 'yellow', 'cyan', 'orange']

def get_number_of_competitors():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric, try again!")
            continue
        if 2 <= racers <= 10:
            return racers
        else:
            print("Racers number is out of range (2-10)!")

def create_racers(colors):
    turtles = []
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos()
        racer.pendown()
        turtles.append(racer)





def init_screen():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Snail race!')

racers = get_number_of_competitors()
init_screen()
random.shuffle(COLORS)
colors = COLORS[:racers]
create_racers(colors)


# racer = turtle.Turtle()
# racer.speed(1)
# racer.penup()
# racer.shape('turtle')
# racer.color('green')
# racer.forward(100)
# racer.left(90)
# racer.forward(100)
# racer.right(-135)
# racer.forward(300)
# time.sleep(5)
