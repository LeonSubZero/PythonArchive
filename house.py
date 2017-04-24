"""
Flavio Leon
4.19.2017
house.py
Program that allows the user to draw simple house using five mouse clicks.

input: five mouse clicks staggered.
process:    1.Prompt user 2 clicks for house rect. Rectangle(P1,P2)
            2.Prompt user for 1 click draw door. Door should be 1/5 width of house frame.
            3.Prompt user for 1 click to draw window. Window half the size of door.
            4.Prompt user for roof peak to draw roof poly. Polygon(p1,p2,p3)
            5.Display house.
            6.Prompt to click it and quit it.
            
output: display house

"""
from graphics import *

def main():
    #create window 
    win=GraphWin("Design a house...",500,500)
    win.setCoords(0,0,10,10)

    #Prompt for 2 clicks for house
    message = Text(Point(5,0.2), "Click on top left and then bottom right.")
    message.draw(win)
    

    #get mouse
    topLeft=win.getMouse()
    topLeft.draw(win)

    bottomRight=win.getMouse()
    bottomRight.draw(win)

    #validate correct coords to prevent house from appearing upside down.
    while topLeft.getY()<bottomRight.getY():
        

        
        topLeft.undraw()
        bottomRight.undraw()
        message.undraw()
        message = Text(Point(5,0.5), "Error..Click on top left and then bottom right.")
        message.draw(win)
        topLeft=win.getMouse()
        topLeft.draw(win)

        bottomRight=win.getMouse()
        bottomRight.draw(win)
       
    #draw house using "Functional Decomposition" 
    LilHouseonPrarie(topLeft,bottomRight,win)        

    #Prompt for 1 click for door.
    message.undraw()
    message = Text(Point(2,0.2), "Click one point for door")
    message.draw(win)

    doorW=topLeft.getX()-bottomRight.getX()
    doorW=abs(doorW)/5
    
    CenterDoor=win.getMouse()
    drXleft=CenterDoor.getX()-doorW/2
    drXright=CenterDoor.getX()+doorW/2

    drYtop=CenterDoor.getY()
    drYbottom=bottomRight.getY()
    
    #Draw door via Functional Decomposition.
    Door(drXleft,drYtop,drXright,drYbottom,win)
    
    #Prompt for 1 click for window.
    message.undraw()
    message = Text(Point(2,0.2), "Click one point for window")
    message.draw(win)

    windowCenter=win.getMouse()
    windowWide=doorW/2

    winXleft=windowCenter.getX()-windowWide/2
    winXright=windowCenter.getX()+windowWide/2

    winYtop=windowCenter.getY()+windowWide/2
    winYbottom=windowCenter.getY()-windowWide/2
    #Draw window
    winRect=Rectangle(Point(winXleft,winYtop),Point(winXright,winYbottom))
    winRect.draw(win)
    winRect.setFill("white")

    #Prompt for 1 click for roof
    message.undraw()
    message = Text(Point(2,0.2), "Click one point for roof")
    message.draw(win)
    
    p1=win.getMouse()

    p2=topLeft

    p3=Point(bottomRight.getX(),topLeft.getY())

    #Draw roof using "Functional decomposition" 
    Roof(p1,p2,p3,win)
    
    #Prompt to Quit.
    message.setText("Click to quit")
    win.getMouse()
    win.close()
    
#Functional decomposure
def LilHouseonPrarie(x,y,z):
    
    rectangle = Rectangle(x,y)
    rectangle.setFill("pink")
    rectangle.setOutline("black")
    rectangle.draw(z)
    
def Roof(x,y,z,FL):
    roofPoly=Polygon(x,y,z)
    roofPoly.setFill("black")
    roofPoly.draw(FL)

def Door(x,y,z,FL,win):
    doorRect=Rectangle(Point(x,y),Point(z,FL))
    doorRect.setFill("brown")
    doorRect.draw(win)

        
main()
