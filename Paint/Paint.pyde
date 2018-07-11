def setup():
    size(600, 400)
    line(100, 0, 100, 400)
    line(50, 0, 50, 400)
    line(0, 50, 100, 50)
    line(0, 100, 100, 100)
    line(0, 150, 100, 150)
    line(0, 200, 100, 200)
    line(0, 250, 100, 250)
    line(0, 300, 100, 300)
    line(0, 350, 100, 350)
    fill(0, 0, 255)
    rect(10, 10, 30, 30)
    fill(0, 100, 0)
    rect(60, 10, 30, 30)
    fill(255, 0, 0)
    rect(10, 60, 30, 30)
    fill(0)
    text("random", 55, 75)
    text("color", 63, 87)
    fill(255, 285, 15)
    rect(10, 110, 30, 30)
    fill(104, 34, 139)
    rect(60, 110, 30, 30)
    noFill()
    ellipse(25, 325, 30, 30)
    rect(60, 310, 30, 30)
    
def draw():

    if mousePressed and mouseX > 100 and pmouseX > 100:
        line(pmouseX, pmouseY, mouseX, mouseY)
        
def mouseClicked():
    if (mouseX >= 0 and mouseX <= 50) and (mouseY >= 0 and mouseY <= 50):
        stroke(0, 0, 255)
    if (mouseX >= 50 and mouseX <= 100) and (mouseY >= 0 and mouseY <= 50):
        stroke(0, 100, 0)
    if (mouseX >= 0 and mouseX <= 50) and (mouseY >= 50 and mouseY <= 100):
        stroke(255, 0, 0)
    if (mouseX >= 50 and mouseX <= 100) and (mouseY >= 50 and mouseY <= 100):
        stroke(random(255), random(255), random(255))
    if (mouseX >= 0 and mouseX <= 50) and (mouseY >= 100 and mouseY <= 150):
        stroke(255, 285, 15)
    if (mouseX >= 50 and mouseX <= 100) and (mouseY >= 100 and mouseY <= 150):
        stroke(104, 34, 139)
        
    
    if (mouseX >= 0 and mouseX <= 50) and (mouseY >= 300 and mouseY <= 350):
        if mousePressed and mouseX > 100:
            ellipse(mouseX, mouseY, 50, 50)
