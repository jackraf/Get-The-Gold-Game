import random
from graphics import *
import time
import math
import random


def main():
    win, circlelistx,circlelisty,reccy,goldCoin = gameSetUp()
    player = createPlayer(win)
    playGame(win,circlelistx,circlelisty,player,reccy,goldCoin)




def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)
    return circle

def createPlayer(win):
    player = drawCircle(win,Point(50,250),10,"red")
    return player
def distanceBetweenPoints(x1,x2,y1,y2):
    distance = math.sqrt(((x1- y1) ** 2) + ((x2 - y2) ** 2))
    return distance

def moveAll(shapeList,dx,dy):
    for shape in shapeList:
        shape.move(dx,dy)

def checkGameOver(player,circlelistx,circlelisty,reccy):
    if player.getCenter().getX() in range(0,75) and player.getCenter().getY() in range(225,300):
        return False
    else:
        for circle in circlelistx:
            if distanceBetweenPoints(player.getCenter().getX(),player.getCenter().getY(), circle.getCenter().getX(), circle.getCenter().getY()) < player.getRadius() + circle.getRadius():

                return True
        for circle in circlelisty:
            if distanceBetweenPoints(player.getCenter().getX(),player.getCenter().getY(), circle.getCenter().getX(), circle.getCenter().getY()) < player.getRadius() + circle.getRadius():
                return True



def checkGoldCoin(player, goldCoin):
    if distanceBetweenPoints(player.getCenter().getX(),player.getCenter().getY(), goldCoin.getCenter().getX(), goldCoin.getCenter().getY()) < player.getRadius() + goldCoin.getRadius():
        return True
def gameSetUp():
    win = GraphWin("title",1080,500)
    randomlist = []
    randomlisty = []
    randomradius = []

    for i in range(0,10):
        randomcentre = Point(1000,random.randint(0,500))
        randomcentrey = Point(random.randint(0,1000),0)
        randomlisty.append(randomcentrey)
        randomlist.append(randomcentre)
        randomradii = random.randint(10,50)

        randomradius.append(randomradii)

    goldCoin = drawCircle(win, randomlist[0],20,"gold")
    circle1 = drawCircle(win,randomlist[0], randomradius[0], "black")
    circle2 = drawCircle(win, randomlist[1], randomradius[1],"black")
    circle3 = drawCircle(win, randomlist[2], randomradius[2],"black")
    circle4 = drawCircle(win,randomlist[3],randomradius[3],"black")
    circle5 = drawCircle(win, randomlist[4],randomradius[4],"black")
    circle6 = drawCircle(win, randomlisty[0],randomradius[5],"black")
    circle7 = drawCircle(win, randomlisty[1], randomradius[6],"black")
    circle8 = drawCircle(win, randomlisty[2], randomradius[7],"black")
    circle9 = drawCircle(win, randomlisty[3], randomradius[8],"black")
    circle10 = drawCircle(win, randomlisty[4],randomradius[9],"black")

    circlelistx = [circle1, circle2, circle3, circle4,circle5]
    circlelisty = [circle6,circle7,circle8,circle9,circle10]
    reccy = Rectangle(Point(0,225),Point(75,300))
    reccy.setFill("red")
    reccy.draw(win)
    return win, circlelistx,circlelisty,reccy,goldCoin


def playGame(win,circlelistx,circlelisty,player,reccy,goldCoin):
    x = -5
    y = 5
    pointScore = 0
    scoreBoard = Text(Point(990,25),str(pointScore))
    scoreBoard.setSize(30)
    scoreBoard.draw(win)
    while True:
        time.sleep(0.000025)
        randomint = random.randint(-1,1)
        moveAll(circlelistx, x, randomint)
        moveAll(circlelisty, randomint,y)

        checkPlayerMove(win,player)

        if checkGoldCoin(player,goldCoin):
            goldCoin.undraw()
            goldCoin = drawCircle(win, Point(random.randint(10,1000),random.randint(10,500)),20,"gold")
            pointScore += 1
            scoreBoard.undraw()
            scoreBoard = Text(Point(990,25),str(pointScore))
            scoreBoard.setSize(25)
            scoreBoard.draw(win)

        if checkGameOver(player,circlelistx,circlelisty,reccy):
            txt = Text(Point(250,250),"Game Over")
            txt.draw(win)
            time.sleep(2)
            win.close()

        if int(circlelistx[0].getCenter().getX()) < 0 or int(circlelistx[0].getCenter().getX()) > 1080:
            x = -x
        if int(circlelisty[0].getCenter().getY()) < 0 or int(circlelisty[0].getCenter().getY())>520:
            y = -y


def checkPlayerMove(win, player):
    key = win.checkKey()
    if key == "8":
        player.move(0,-10)
    elif key == "5":
        player.move(0, 10)
    elif key == "9":
        player.move(5,-5)
    elif key == "6":
        player.move(10,0)
    elif key == "3":
        player.move(5,5)
    elif key == "4":
        player.move(-10,0)
    elif key == "1":
        player.move(-5,5)
    elif key == "7":
        player.move(-5,-5)





main()
