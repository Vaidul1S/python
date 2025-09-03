import turtle
import time
import random
import math

WIDTH, HEIGHT = 800, 600
COLORS = ['red', 'blue', 'green', 'white', 'pink', 'purple', 'lime', 'yellow', 'cyan', 'orange']

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

def make_snail():
    points = []
    scale = 0.7
    a, r = 0, 2
    for i in range(50):
        x = r * math.cos(math.radians(a))
        y = r * math.sin(math.radians(a))
        points.append((x * scale, y * scale))
        a += 20
        r += 0.5 * scale
    
    xs, ys = zip(*points)
    cx = (max(xs) + min(xs)) / 2
    cy = (max(ys) + min(ys)) / 2
    snail = tuple((x - cx, y - cy) for x, y in points)        
        
    turtle.register_shape("snail", snail)


    
def create_racers(colors):
    make_snail()
    turtles = []
    spacingX = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)        
        racer.shape('snail')
        racer.left(90)
        racer.penup()   
        racer.setpos(-WIDTH//2 + (i + 1) * spacingX, -HEIGHT//2 + 30)
        racer.pendown()
        turtles.append(racer)
    return turtles

def race(colors):
    turtles = create_racers(colors)
    
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT//2 - 30:
                return colors[turtles.index(racer)]

def init_screen():
    screen = turtle.Screen()
    root = screen._root 
    root.attributes('-topmost', True)
    root.update()
    root.attributes('-topmost', False)

    screen.bgcolor('black')
    screen.setup(WIDTH, HEIGHT)
    screen.title('Snail race!')

racers = get_number_of_competitors()
init_screen()
random.shuffle(COLORS)
colors = COLORS[:racers]


winner = race(colors)
print("\n🏁 And the winner is: " + winner.capitalize() + '!!! 🏁\n')
time.sleep(3)

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
