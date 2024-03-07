from turtle import *


#we want to paint a huose
#step 1: draw a square
speed(10)
width(7)
color("purple")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

#drawing a roof

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing 1st window
color("yellow")
penup()
goto(175, 175)
pendown()
right(60)
forward(50)
left(90)
forward(40)
left(90)
forward(50)
left(90)
forward(40)
left(90)
forward(25)
left(90)
forward(40)
left(90)
forward(25)
left(90)
forward(20)
left(90)
forward(50)

#drawing 2nd window 

penup()
goto(25, 175)
pendown()
left(90)
forward(40)
left(90)
forward(50)
left(90)
forward(40)
left(90)
forward(50)
left(90)
forward(20)
left(90)
forward(50)
left(90)
forward(20)
left(90)
forward(25)
left(90)
forward(40)



exitonclick()