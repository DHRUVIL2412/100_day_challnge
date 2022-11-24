# from turtle import *
# timmy = Turtle()
# timmy.forward(100)
# timmy.color('blue')
# exitonclick()

# from prettytable import PrettyTable
# import anothermodule
# print(anothermodule.anotherVariable)
# x = PrettyTable()
# x.field_names = ["City name",'area','population','annualrainfall']
# x.add_row(["ahemedabad",'chandlodia',2000000,600.0])
# x.add_row(['gandinagar','shersha',10000,400.0])
# x.add_row(['surat','bhojare',10000,3.0])
# x.add_row(['mirzapur','location',30000,4.0])
# print(x)

# x = PrettyTable()

# x.add_column('ahemedabad',['chandlodia',2000,2])
# x.add_column('surat',['karannagar',4000,30])
# x.add_column('junagadh',['varansi',7888,83])
# print(x)


# class user:
#     def __init__(self):
#         self.self = self

# user1 = user()
# user1.id = 101
# user1.name = 'dhruvil'
# user1.mobileNumber = 7016446713

# print(user1.id)


# class user:
#     def __init__(self):
#         self.self = self

# user1 = user()
# user1.id = 101
# user1.name = 'dhruvil'
# user1.mobileNumber = 7016446713

# print(user1.id)
# print(user1.name)
# print(user1.mobileNumber)


# class user:
#     def __init__(self,userid,userName):
#         self.userid = userid
#         self.userName = userName
#         self.follower = 0
#         self.following = 0
#     def follow(self,user):
#         user.follower +=1
#         self.following +=1

# user1 = user(10,'dhruvil')

# user2 = user(11,'prshant')
# user1.follow(user2)
# print(user1.follower)
# print(user2.follower)
# print(user1.following)
# print(user2.following)

# class userData:
#     def __init__(self,userName, userId):
#         self.uesrName = userName
#         self.userId = userId
#         self.follower = 0
#         self.following = 0
#     def userFollower(self,userData):
#         userData.follower +=1
#         self.following +=1
        
# user1 = userData("dhruvil",10)
# user2 = userData('ashish',2)
# user1.userFollower(user2)

# print(user1.follower)
# print(user1.following)
# print(user2.follower)
# print(user2.following)



# from turtle import Turtle, exitonclick,Screen

# timmy = Turtle()
# timmy.color('blue')
# screen = Screen()
# exitonclick()

# conda = Turtle()
# screen = Screen()
# screen.register_shape("giphy.gif")
# conda.color('red')

# conda.speed(5)
# conda.position()
# conda.forward(300)
# conda.position()
# conda.speed(5)
# conda.bk(300)

# screen.exitonclick()

# condo = Turtle()

# condo.color('red')
# condo.speed(5)
# condo.position()
# condo.forward(300)
# condo.position()
# condo.speed(5)
# condo.back(300)
# screen = Screen()
# screen.exitonclick()


# from turtle import Turtle,exitonclick

# t= Turtle()
# t.color('green','green')
# t.shape('triangle')
# t.forward(200)
# t.left(90)
# t.forward(200)
# t.left(90)
# t.forward(200)
# t.left(90)
# t.forward(200)
# t.fill()
# exitonclick()

# import random
# from turtle import Turtle as tim,exitonclick
# def choiceColor():
#     colors = ('green','blue','red')
#     colormaker = random.choice(colors)
#     print(colormaker)
#     return colormaker
# timmy = tim()
# for i in range(3,10):
#     for j in range(i):
#         timmy.forward(50)
#         timmy.left(360/i)
#         timmy.color(f'{(choiceColor())}')
# exitonclick()

# from turtle import Turtle ,exitonclick
# import random
# def colorPiker():
#     colorList = ['red','green','blue','coral','black','magenta']
#     colorChooseFromList = random.choice(colorList)
#     return colorChooseFromList
# timmy = Turtle()
# for i in range(3,10):
#     for j in range(i):
#         timmy.forward(50+(i*10))
#         timmy.left(360/i)
#         timmy.color(f'{colorPiker()}')
# exitonclick()

# import random
# import turtle

# def colorPicker():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     getColor = (r,g,b)
#     return getColor 

# direction = [0,90,180,270]
# timmy = turtle.Turtle()
# turtle.colormode(255)
# timmy.pensize(50)
# timmy.pencolor('green')
# timmy.speed(10)
# timmy.shape('square')
# for i in range(1000):
#     timmy.color(colorPicker())
#     timmy.forward(5)
#     timmy.setheading(random.choice(direction))
# turtle.exitonclick()


# import random
# import turtle

# def colorPicker():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     getColor = (r,g,b)
#     return getColor 

# direction = [0,90,180,270]
# timmy = turtle.Turtle()
# turtle.colormode(255)
# timmy.pensize(10)
# timmy.pencolor('green')
# timmy.speed(10)
# timmy.shape('square')
# for i in range(100):
#         timmy.color(colorPicker())
#         timmy.forward(100)
#         timmy.left(50)
# turtle.exitonclick()

# import random
# import turtle

# def colorPicker():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     getColor = (r,g,b)
#     return getColor 

# timmy = turtle.Turtle()
# turtle.colormode(255)
# timmy.speed(0)


# def cordinateCircle(type_of_danta):
#     for i in range(int(360/type_of_danta)):
#         timmy.color(colorPicker())
#         timmy.circle(100)
#         timmy.setheading(timmy.heading()+type_of_danta)
# cordinateCircle(5)
# turtle.exitonclick()

# import random
# from turtle import Turtle , exitonclick
# import turtle

# turtle.colormode(255)
# tom = Turtle()
# tom.pensize(20)
# def colorChoose():
#     r = random.randint(1,255)
#     g = random.randint(1,255)
#     b = random.randint(1,255)
#     colorSelected = (r,g,b)
#     return colorSelected

# def staitLine():
#     tom.pendown()
#     tom.color(colorChoose())
#     tom.forward(0)
#     tom.penup()    
#     tom.forward(40)
# def counterDouts(length):
#     for i in range(length):
#         staitLine()
# def turnLeft():
#     tom.left(90)
#     staitLine()
#     tom.left(90)
# def turnRight():
#     tom.right(90)
#     staitLine()
#     tom.right(90)


# for i in range(100):
#     if i%10==0:
#         counterDouts(20)
#         turnLeft()
#         counterDouts(20)
#         turnRight()
# exitonclick()


# import random
# from turtle import Turtle , exitonclick
# import turtle

# turtle.colormode(255)
# tom = Turtle()
# tom.pensize(20)
# def colorChoose():
#     r = random.randint(1,255)
#     g = random.randint(1,255)
#     b = random.randint(1,255)
#     colorSelected = (r,g,b)
#     return colorSelected

# def staitLine():
#     tom.pendown()
#     tom.color(colorChoose())
#     tom.forward(0)
#     tom.penup()    
#     tom.forward(40)
# def counterDouts(length):
#     for i in range(length):
#         staitLine()
# def turnLeft():
#     tom.left(90)
#     staitLine()
#     tom.left(90)
# def turnRight():
#     tom.right(90)
#     staitLine()
#     tom.right(90)

# tom.setheading(224)
# tom.penup()
# tom.forward(400)
# tom.setheading(0)
# for i in range(4):
#     counterDouts(10)
#     turnLeft()
#     counterDouts(10)
#     turnRight()
# exitonclick()

# from turtle import Turtle , exitonclick
# import turtle
# import random
# turtle.colormode(255)
# def colorGenrator():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     return (r,g,b)

# def directionControl():
#     direction = [90,180,270,360,160,200,300,330,60]

#     return random.choice(direction)

# tom = turtle.Turtle()
# tom.pensize(20)
# tom.speed(10)
# for i in range(100):
#     tom.forward(30)
#     tom.left(directionControl())
#     tom.color(colorGenrator())
# exitonclick()

# from turtle import Turtle,exitonclick , Screen

# t = Turtle()
# screen = Screen()

# def moveForward():
#     t.forward(10)
# def moveBackward():
#     t.backward(10)
# def turn_left():
#     newHeading = t.heading()+10
#     t.setheading(newHeading)
# def turn_right():
#     newHeading = t.heading-10
#     t.setheading(newHeading)
# def clearfun():
#     t.clear() 
#     t.penup( )
#     t.home()
#     t.pendown()
# screen.listen()
# screen.onkey(moveForward,'w')
# screen.onkey(moveBackward,'s')
# screen.onkey(turn_left,'a')
# screen.onkey(turn_right,'d')
# screen.onkey(clearfun,'c')
# exitonclick()



# from turtle import Turtle,exitonclick , Screen 
# import random
# screen = Screen()
# screen.setup(width=500 , height = 400)
# user_bet = screen.textinput(title='about the race ',prompt="who is wining the race")
# color = ['red','green','blue','black','orange','brown']
# y_posotion = [ -70,-40,-10,20,50,80]
# print(user_bet)
# def gotoPosition(x,y):
#     return t.goto(x,y)
# for i in range(int(user_bet)):
#     t = Turtle(shape='turtle')
#     t.penup()
#     t.color(color[i])
#     gotoPosition(-230,y_posotion[i])

# while True:
#     t.speed(1)
#     randome_forward = random.randint(0,20)
#     t.forward(randome_forward)

# exitonclick()

# import curses
# import maths
# import sys

# def main(argv):
#   # BEGIN ncurses startup/initialization...
#   # Initialize the curses object.
#   stdscr = curses.initscr()

#   # Do not echo keys back to the client.
#   curses.noecho()

#   # Non-blocking or cbreak mode... do not wait for Enter key to be pressed.
#   curses.cbreak()

#   # Turn off blinking cursor
#   curses.curs_set(False)

#   # Enable color if we can...
#   if curses.has_colors():
#     curses.start_color()

#   # Optional - Enable the keypad. This also decodes multi-byte key sequences
#   # stdscr.keypad(True)

#   # END ncurses startup/initialization...

#   caughtExceptions = ""
#   try:
#    # Create a 5x5 window in the center of the terminal window, and then
#    # alternate displaying a border and not on each key press.

#    # We don't need to know where the approximate center of the terminal
#    # is, but we do need to use the curses terminal size constants to
#    # calculate the X, Y coordinates of where we can place the window in
#    # order for it to be roughly centered.
#    topMostY = math.floor((curses.LINES - 5)/2)
#    leftMostX = math.floor((curses.COLS - 5)/2)

#    # Place a caption at the bottom left of the terminal indicating 
#    # action keys.
# #    stdscr.addstr (curses.LINES-1, 0, "Press Q to quit, any other key to alternate.")
# #    stdscr.refresh()
   
# #    # We're just using white on red for the window here:
# #    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)

# #    index = 0
# #    done = False
# #    while False == done:
# #     # If we're on the first iteration, let's skip straight to creating the window.
# #     if 0 != index:
# #      # Grabs a value from the keyboard without Enter having to be pressed. 
# #      ch = stdscr.getch()
# #      # Need to match on both upper-case or lower-case Q:
# #      if ch == ord('Q') or ch == ord('q'): 
# #       done = True
# #     mainWindow = curses.newwin(5, 5, topMostY, leftMostX)
# #     mainWindow.bkgd(' ', curses.color_pair(1))
# #     if 0 == index % 2:
# #      mainWindow.box()
# #     else:
# #      # There's no way to "unbox," so blank out the border instead.
# #      mainWindow.border(' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')
# #     mainWindow.refresh()

# #     stdscr.addstr(0, 0, "Iteration [" + str(index) + "]")
# #     stdscr.refresh()
# #     index = 1 + index

# #   except Exception as err:
# #    # Just printing from here will not work, as the program is still set to
# #    # use ncurses.
# #    # print ("Some error [" + str(err) + "] occurred.")
# #    caughtExceptions = str(err)

# #   # BEGIN ncurses shutdown/deinitialization...
# #   # Turn off cbreak mode...
# #   curses.nocbreak()

# #   # Turn echo back on.
# #   curses.echo()

# #   # Restore cursor blinking.
# #   curses.curs_set(True)

# #   # Turn off the keypad...
# #   # stdscr.keypad(False)

# #   # Restore Terminal to original state.
# #   curses.endwin()

# #   # END ncurses shutdown/deinitialization...

# #   # Display Errors if any happened:
# # #   if "" != caughtExceptions:
# # #    print ("Got error(s) [" + caughtExceptions + "]")

# # # if __name__ == "__main__":
# # #   main(sys.argv[1:])


# from turtle import Screen , Turtle ,exitonclick
# import random

# t = Turtle()
# screen = Screen()
# screen.setup(600,600)
# screen.colormode(255)
# screen.bgcolor('black')
# screen.title('snake game')

# screeen_positioning = [(00,00),(-50,00),(-100,00),(-150,00)]
# segment = []
# for i in screeen_positioning:
#   newSegment = Turtle("circle")
#   newSegment.color('white')
#   newSegment.goto(i)
#   segment.append(newSegment)

# gameStart = True
# while gameStart:
#   for s in segment:
#     s.left(19)
#     s.forward(10)



# exitonclick()

# from turtle import Turtle , Screen , exitonclick
# screen = Screen()
# screen.setup(500,500)
# screen.bgcolor('black')
# colores =['red','green','blue','pink','white']
# position = [(-230,-80),(-230,-40),(-230,00),(-230,40),(-230,80)]
# segment = []
# for i in range(5):
#   t1 = Turtle()
#   t1.color(colores[i])
#   t1.shape('turtle')
#   t1.penup()
#   t1.goto(position[i])
#   segment.append(t1)
#
# gameIsStart = True
#
# while True:
#   for i in segment:
#
# exitonclick()
#

from turtle import Turtle,Screen,exitonclick
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(800,600)
screen.bgcolor('black')
screen.title('pipg pong game')

pad1 = Paddle(-350,0)
pad2 = Paddle(350,0)

screen.listen()
screen.onkey(pad2.go_up,'Up')
screen.onkey(pad2.go_down,'Down')
screen.onkey(pad1.go_up,'w')
screen.onkey(pad1.go_down,'s')

ball = Ball()
game_is_on = True
while game_is_on :
    ball.move()



exitonclick()