natureblank = Actor('character')
natureblank.pos = 100, 150

WIDTH = 500
HEIGHT = 300

def draw():
    screen.fill((100, 0 ,0))
    natureblank.draw()

def update():
    natureblank.left = natureblank.left + 2
    if natureblank.left > WIDTH:
        natureblank.right = 0

