"""
Flavio Leon
4.18.2017
naturals.py
Gui that prompts the user for number and displays from 1 to number in a series.
input: user's number
process: create canvas 500x500, recieve entry text of number. Use function to
return list of numbers. Create rectangle button. Output to display list.
output: Gui interface,List of numbers displayed.


"""
from graphics import *
def main():
    win=GraphWin("Natural numbers", 500,500)
    win.setCoords(0,0,6,6)

    title=Text(Point(3,5.5),"Natural Numbers Calculator")
    title.draw(win)

    entlabel=Text(Point(1.8,4),"Enter a number:")
    entlabel.draw(win)

    number=Entry(Point(3.5,4),10)
    number.setText("0")
    number.draw(win)

    button= Rectangle(Point(1.75,3),Point(4.25,2))
    button.setFill("black")
    button.draw(win)

    blabel=Text(Point(3,2.5),"Display Naturals")
    blabel.setTextColor("green")
    blabel.setStyle("bold")
    blabel.draw(win)


    win.getMouse()
    n=eval(number.getText())
    
    s=naturalBornK(n)
    s=str(s)
    #print(s[1:-1])
         
    
    listN=Text(Point(2.5,1), "List of Naturals: "+s[1:-1])
    listN.draw(win)
    
        
def naturalBornK(n):

    mylist = []
    for x in range(1, n+1):

        mylist = mylist + [x]

    return mylist



main()
