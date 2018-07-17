from graphics import *
from time import *
import tree_creation
from tkinter import messagebox

loop = 0
treeInst = tree_creation.tree_creation()
PathNodes = treeInst.getPath()
print (PathNodes)

ListOfFirst = [x[0] for x in PathNodes]
ListOfSecond = [x[1] for x in PathNodes]
ListOfTimes = [x[3] for x in PathNodes]

#check repeation
NumOfelements = sorted(set(list(set(ListOfFirst))+list(set(ListOfSecond))))
listOfColors = ['white', 'yellow', 'orange', '#9400D3', 'black', 'grey' ,'blue']
DicOfColors = {1:'white' , 3:'yellow', 6: 'orange' , 7:'#9400D3' , 8:'black'}

print("list of all first persons : "+str(ListOfFirst))
print("%%%%%%%%%%%")
print("list of all second persons : "+str(ListOfSecond))
print("%%%%%%%%%%%")
print("list of all times : "+str(ListOfTimes))
print("%%%%%%%%%%%")
print(NumOfelements)
# GUI

StartGame = messagebox.showinfo("Logic Game : ","Welcome to logic game 1  (^_^)")
win = GraphWin("Logic Game : " , 640 , 285)
win.setBackground('#1E90FF')
#----------------------------------------------------------------------------------
for x in NumOfelements:
    if (x==0):
        pass
    else:
     globals()['Circle%s' % x] = Circle(Point(50, (30+(20*loop))), 10)
     globals()['Circle%s' % x].setFill(listOfColors[loop])
     globals()['Circle%s' % x].draw(win)
     loop = loop+1

LeftGround = Rectangle(Point(10,0),Point(140,150))
LeftGround.setFill("")
LeftGround.setWidth(30)
LeftGround.setOutline("green")
LeftGround.draw(win)
#----------------------------------------------------------------------------------
RightGround = Rectangle(Point(630,0),Point(485,150))
RightGround.setFill("")
RightGround.setWidth(30)
RightGround.setOutline("green")
RightGround.draw(win)
#----------------------------------------------------------------------------------
Boot = Rectangle(Point(80,60),Point(150,80))
Boot.setFill("")
Boot.setWidth(15)
Boot.setOutline("brown")
Boot.draw(win)
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# game notations
loop =0
for x in NumOfelements:
    if (x==0):
        pass
    else:
     globals()['NotationCircle%s' % x] = Circle(Point(10, 175+(20*loop)), 10)
     globals()['NotationCircle%s' % x].setFill(listOfColors[loop])
     testText = Text(Point(70, 175+(20*loop)), "this is for : "+str(x))
     testText.setFill(listOfColors[loop])
     testText.draw(win)
     globals()['NotationCircle%s' % x].draw(win)
     loop = loop+1

# transfaring

def moveRigth(Fname, Sname , BootName):
    x = 0
    while x < 40 :
        BootName.move(10,0)
        Fname.move(10,0)
        Sname.move(10,0)
        sleep(.2)
        x = x+1
def moveLeft(name , BootName):
    y = -40
    while y < 0 :
        BootName.move(-10,0)
        name.move(-10,0)
        sleep(.1)
        y = y+1

testText = Text(Point(320,25),"score = "+str(ListOfTimes.pop())+" seconds")
testText.setFill("black")
testText.draw(win)
Starttime = 0
while Starttime < 10 :
    sleep(.2)
    Starttime = Starttime+1

loop=0
time = 0
for node in PathNodes:
    person1 = ListOfFirst.pop()
    person2 = ListOfSecond.pop()
    if (person1==0 and person2==0):
        pass
    elif (person2==0):
        globals()['Circle%s' % person1].undraw()
        globals()['Circle%s' % person1] = Circle(Point(530,65), 10)
        globals()['Circle%s' % person1].setFill(DicOfColors[person1])
        globals()['Circle%s' % person1].draw(win)
        moveLeft(globals()['Circle%s' % person1],Boot)
        testText.undraw()
        testText = Text(Point(320, 25), "score = " + str(time+person1)+ " seconds")
        testText.setFill("black")
        testText.draw(win)
        time = time+person1
    else:
        globals()['Circle%s' % person1].undraw()
        globals()['Circle%s' % person2].undraw()
        globals()['Circle%s' % person1] = Circle(Point(100, 65), 10)
        globals()['Circle%s' % person1].setFill(DicOfColors[person1])
        globals()['Circle%s' % person1].draw(win)
        globals()['Circle%s' % person2] = Circle(Point(130,65), 10)
        globals()['Circle%s' % person2].setFill(DicOfColors[person2])
        globals()['Circle%s' % person2].draw(win)
        moveRigth(globals()['Circle%s' % person1],globals()['Circle%s' % person2],Boot)
        if (person1>person2):
            testText.undraw()
            testText = Text(Point(320, 25), "score = " + str(time + person1) + " seconds")
            testText.setFill("black")
            testText.draw(win)
            time = time + person1
        else:
            testText.undraw()
            testText = Text(Point(320, 25), "score = " + str(time + person2) + " seconds")
            testText.setFill("black")
            testText.draw(win)
            time = time + person2

# for the gui
loop = 0
for x in NumOfelements:
    if (x==0):
        pass
    else:
     globals()['Circle%s' % x].undraw()
     globals()['Circle%s' % x] = Circle(Point(580, (30+(20*loop))), 10)
     globals()['Circle%s' % x].setFill(listOfColors[loop])
     globals()['Circle%s' % x].draw(win)
     loop = loop+1

sleep(1.5)
EndGame = messagebox.showinfo("Logic Game : ","The End  (^_^)")
win.destroy()
win.close()






