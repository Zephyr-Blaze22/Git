import turtle

# window
window=turtle.Screen()
window.bgcolor('black')
window.setup(width=800, height=600)
window.tracer(0)

# right paddle
right_paddle=turtle.Turtle()
right_paddle.shape('square')
right_paddle.color('white')
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.pu()
right_paddle.goto(350, 0)

# left paddle
left_paddle=turtle.Turtle()
left_paddle.shape('square')
left_paddle.color('white')
left_paddle.shapesize(stretch_len=1, stretch_wid=5)
left_paddle.pu()
left_paddle.goto(-350,0)

# ball
ball=turtle.Turtle()
ball.shape('square')
ball.color('red')
ball.speed(40)
ball.pu()
ball.goto(0,0)
ball.dx=0.2
ball.dy=0.2

# score
score_r=0
score_l=0

pen=turtle.Turtle()
pen.color('white')
pen.pu()
pen.hideturtle()
pen.speed(0)
pen.goto(0,260)
pen.write("Игрок A: 0  Игрок B: 0", align="center", font=("Courier", 18, "normal"))

# func
def right_up():
    y_1=right_paddle.ycor()
    if y_1<250:
        right_paddle.sety(y_1+20)

def right_down():
    y_1=right_paddle.ycor()
    if y_1>-250:
        right_paddle.sety(y_1-20)

def left_up():
    y_2=left_paddle.ycor()
    if y_2<250:
        left_paddle.sety(y_2+20)

def left_down():
    y_2=left_paddle.ycor()
    if y_2>-250:
        left_paddle.sety(y_2-20)

# start
window.listen()
window.onkeypress(right_up, 'Up')
window.onkeypress(right_down, 'Down')
window.onkeypress(left_up, 'w')
window.onkeypress(left_down, 's')

while True:
    window.update()

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        score_l+=1
        pen.clear()
        pen.write(f"Игрок A: {score_l}  Игрок B: {score_r}", align="center", font=("Courier", 18, "normal"))
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        score_r+=1
        pen.clear()
        pen.write(f"Игрок A: {score_l}  Игрок B: {score_r}", align="center", font=("Courier", 18, "normal"))
    if (340<ball.xcor()<350) and (right_paddle.ycor()-50<ball.ycor()<right_paddle.ycor()+50):
        ball.dx*=-1
        ball.dx+=0.01
        ball.setx(340)
    if (-350<ball.xcor()<-340) and (left_paddle.ycor()-50<ball.ycor()<left_paddle.ycor()+50):
        ball.dx*=-1
        ball.dx+=0.01
        ball.setx(-340)