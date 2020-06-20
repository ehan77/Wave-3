# ??? CPT ??? #

# IMPORTS #
import turtle
import time
import random

delay = 0.1

# SCORE #
score = 0
high_score = 0

# SCREEN #
wn = turtle.Screen()
wn.title("SNAKEYUM by Erica")
wn.bgcolor("lightblue")
wn.setup(width = 700 , height = 700)
wn.tracer(0)

# SNAKE :) #
ply = turtle.Turtle()
ply.speed(0)
ply.shape("circle")
ply.color("white")
ply.penup()
ply.goto(0 , 0)
ply.direction = "stop"

# THE FOOOOD #
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("purple")
food.penup()
food.goto(0 , 100)

segments = []

# PEN #
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0 , 260)
pen.write("SCORE: 0 HIGH SCORE: 0" ,  align = "center" , font = ("System" , 24 , "normal"))

# FUNCTIONS #
def go_up() :
    if ply.direction != "down" :
        ply.direction = "up"

def go_down() :
    if ply.direction != "up" :
        ply.direction = "down"

def go_left() :
    if ply.direction != "right" :
        ply.direction = "left"

def go_right() :
    if ply.direction != "left" :
        ply.direction = "right"

def move() :
    if ply.direction == "up" :
        y = ply.ycor()
        ply.sety(y + 20)

    if ply.direction == "down" :
        y = ply.ycor()
        ply.sety(y - 20)

    if ply.direction == "left" :
        x = ply.xcor()
        ply.setx(x - 20)

    if ply.direction == "right" :
        x = ply.xcor()
        ply.setx(x + 20)

# KEYBOARD BINDINGS #
wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")

# MAIN GAME LOOP
while True:
    wn.update()

    # BORDER COLLISION #
    if ply.xcor() > 290 or ply.xcor() < -290 or ply.ycor() > 290 or ply.ycor() < -290 :
        time.sleep(1)
        ply.goto(0 , 0)
        ply.direction = "stop"

        # HIDE SEGMENTS #
        for segment in segments:
            segment.goto(1000 , 1000)

        # CLEAR SEGMENTS #
        segments.clear()

        # REST SCORE #
        score = 0

        # RESET DELAY #
        delay = 0.1

        pen.clear()
        pen.write("SCORE: {}  HIGH SCORE: {}".format(score , high_score), align = "center" , font = ("System" , 24 , "normal"))



    # FOOD COLLISION #

    if ply.distance(food) < 20 :
        x = random.randint(-285,285)
        y = random.randint(-285,285)
        food.goto(x , y)

        # ! SNAKES BODY PART ! #
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)

        # SHORTEN DELAY #
        delay-=0.001

        # INCREASE SCORE #
        score+=10

        if score > high_score :
            high_score = score

        pen.clear()
        pen.write("SCORE: {}  HIGH SCORE: {}".format(score , high_score),align = "center" , font = ("System" , 24 , "normal"))

    # END SEGMENT #
    for index in range(len(segments)-1 , 0 , -1) :
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x , y)

    if len(segments) > 0 :
        x = ply.xcor()
        y = ply.ycor()
        segments[0].goto(x , y)

    move()

    # HEAD N BODY COLLISION
    for segment in segments :
        if segment.distance(ply) < 20 :
            time.sleep(1)
            ply.goto(0 , 0)
            ply.direction = "stop"

            # HIDE SEGMENTS #
            for segment in segments:
                segment.goto(1000 , 1000)

            # CLEAR SEGMENTS #
            segments.clear()

            # RESET SCORE #
            score = 0

            # RESET DELAY #
            delay = 0.1

            pen.clear()
            pen.write("SCORE: {}  SCORE: {}".format(score , high_score) , align = "center" , font = ("System" , 24 , "normal"))


    time.sleep(delay)

wn.mainloop()