import turtle
import time

# window
window = turtle.Screen()
window.bgcolor('black')
window.setup(width=600, height=700)
window.tracer(0)

# platform
plat=turtle.Turtle()
plat.color('white')
plat.shape('square')
plat.shapesize(stretch_len=5, stretch_wid=1)
plat.pu()
plat.goto(0,-280)

# ball
ball=turtle.Turtle()
ball.color('red')
ball.shape('square')
ball.pu()
ball.dx=1
ball.dy=1
ball.goto(0,0)
ball.speed(40)

# blok
blocks=[]
colors=['green','orange']
for row in range(6):
    for col in range(11):
        block=turtle.Turtle()
        block.color(colors[row%2])
        block.shape('square')
        block.shapesize(stretch_len=2, stretch_wid=1)
        block.pu()
        block.speed(0)
        x=-250 + col*50
        y=140 + row*30
        block.goto(x,y)
        blocks.append(block)

# score
score=0
pen=turtle.Turtle()
pen.color('white')
pen.pu()
pen.hideturtle()
pen.goto(0,320)
pen.write(f"Счёт: {score} ", align="center", font=("Courier", 18, "normal"))

# func
def move_right():
    x=plat.xcor()
    if x>220:
        plat.setx(x)
    else:
        plat.setx(x+20)

def move_left():
    x=plat.xcor()
    if x<-220:
        plat.setx(x)
    else:
        plat.setx(x-20)

# start
window.listen()
window.onkeypress(move_left, 'Left')
window.onkeypress(move_right, 'Right')

while True:
    window.update()

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    for block in blocks:
        if ball.distance(block) < 25:
            block.goto(1000, 1000)  
            blocks.remove(block) 
            score+=1
            pen.clear()
            pen.write(f"Счёт: {score} ", align="center", font=("Courier", 18, "normal"))   
            ball.dy *= -1            
            break 
    if (ball.ycor() - plat.ycor() < 20) and (abs(ball.xcor() - plat.xcor()) < 60):
        offset = ball.xcor() - plat.xcor()
        ball.dx = offset / 30 
        ball.dy *= -1
    if ball.xcor()>290:
        ball.dx*=-1
    if ball.xcor()<-290:
        ball.dx*=-1
    if ball.ycor()<-340:
        pen.clear()
        pen.write('You lose', align="center", font=("Courier", 18, "normal"))
        time.sleep(1)
        break
    if ball.ycor()>300:
        ball.dy*=-1
    if len(blocks) == 0:
        print("🎉 Победа!")
        break