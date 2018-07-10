xCoordinate = 50
speedx = 2
speedy = 2
yCoordinate = 50
red = random(255)
green = random(255)
blue = random(255)

def setup():
    size(400, 500)

    
def draw():
    background(0)
    global xCoordinate, speedx, yCoordinate, speedy, red, green, blue
    xCoordinate += speedx
    yCoordinate += speedy
    if xCoordinate >= 385 or xCoordinate <= 15:
        speedx = -speedx
        red = random(250)
        green = random(250)
        blue = random(250)
    if yCoordinate >= 485 or yCoordinate <= 15:
        speedy = -speedy
        red = random(250)
        green = random(250)
        blue = random(250)
    fill(red, green, blue)
    ellipse(xCoordinate, yCoordinate, 30, 30)
