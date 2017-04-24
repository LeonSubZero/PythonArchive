"""Flavio Leon
4.18.2017
target.py
Program that draws an archery target made of several circles layered over each
other. Each one same width of the radius of yellow circle.

Input:none from user except to quit.
Process: Layout canvas size 400x400. Use coords 6,6,6,6. Create several circles
with centerpoint of 0,0.
Output: Layered circles displayed.


"""

from graphics import *

def main():
    #create window introducting the app
    win=GraphWin("Archery Target...",400,400)
    win.setCoords(-6,-6,6,6)

    aCircle=Circle(Point(0,0),5)
    aCircle.setFill("white")
    aCircle.draw(win)

    aCircle=Circle(Point(0,0),4)
    aCircle.setFill("black")
    aCircle.draw(win)

    aCircle=Circle(Point(0,0),3)
    aCircle.setFill("blue")
    aCircle.draw(win)

    aCircle=Circle(Point(0,0),2)
    aCircle.setFill("red")
    aCircle.draw(win)


    aCircle=Circle(Point(0,0),1)
    aCircle.setFill("yellow")
    aCircle.draw(win)

    message = Text(Point(0,-5.5), "Click to quit")
    message.draw(win)

    #message.setText("Click to quit")
    win.getMouse()
    
    win.close()


main()
