from random import randint

WIDTH = 800
HEIGHT = 800

TITLE = "Shoot the Fruit"

apple = Actor("apple")

def draw():
    screen.clear()
    apple.draw()

def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Good shot")
        place_apple()
    else:
        print("You missed")
        quit()

place_apple()
