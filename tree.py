import turtle
from random import randint

def tree(branchLen,myturtle):
    if branchLen > 10:
        myturtle.forward(branchLen)
        myturtle.right(20)
        tree(branchLen - 10,myturtle)
        myturtle.left(40)
        tree(branchLen - 10,myturtle)
        myturtle.right(20)
        myturtle.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    myWin.setworldcoordinates(-500, -10, 500, 500)
    t.left(90)
    t.down()
    t.color("darkgreen")
    tree(75,t)
    myWin.exitonclick()

main()