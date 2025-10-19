import turtle
import random
import time

# window
window=turtle.Screen()
window.title('Lesson 2.')
window.bgcolor('Black')
window.setup(width=600, height=600)

# player
player=turtle.Turtle()
player.shape('square')
player.color('red')
player.pu()
player.speed(0)
player.goto(0, -250)

# enemy
enemy=turtle.Turtle()
enemy.shape('square')
enemy.color('white')
enemy.pu()
enemy.goto(random.randint(-280,280),250)
enemy.speed(0)
i=5

# enemy_1
enemy_1=turtle.Turtle()
enemy_1.shape('square')
enemy_1.color('white')
enemy_1.pu()
enemy_1.goto(random.randint(-280,280),250)
enemy_1.speed(0)
j=4

# enemy_2
enemy_2=turtle.Turtle()
enemy_2.shape('square')
enemy_2.color('white')
enemy_2.pu()
enemy_2.goto(random.randint(-280,280),250)
enemy_2.speed(0)
f=3

# tablet
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
score=0
pen.write(f"Счёт: {score} ", align="center", font=("Courier", 18, "normal"))

# func
def go_right():
    x=player.xcor()
    if x<280:
        player.setx(x+20)
    else:
        player.setx(x)

def go_left():
    x=player.xcor()
    if x>-280:
        player.setx(x-20)
    else:
        player.setx(x)
window.listen()
window.onkeypress(go_right, 'Right')
window.onkeypress(go_left, 'Left')

while True:
    window.update()
    y=enemy.ycor()
    y-=i
    if y>-300:
        enemy.sety(y)
    else:
        enemy.goto(random.randint(-280, 280), 250)
        if i >=10:
            i+=0.5
        else:
            i+=1
        score+=1
        pen.clear()
        pen.write(f"Счёт: {score} ", align="center", font=("Courier", 18, "normal"))

    y_1=enemy_1.ycor()
    y_1-=j
    if y_1>-300:
        enemy_1.sety(y_1)
    else:
        enemy_1.goto(random.randint(-280, 280), 250)
        if j >=10:
            j+=0.5
        else:
            j+=1
        score+=1
        pen.clear()
        pen.write(f"Счёт: {score} ", align="center", font=("Courier", 18, "normal"))

    y_2=enemy_2.ycor()
    y_2-=f
    if y_2>-300:
        enemy_2.sety(y_2)
    else:
        enemy_2.goto(random.randint(-280, 280), 250)
        if f >=10:
            f+=0.5
        else:
            f+=1
        score+=1
        pen.clear()
        pen.write(f"Счёт: {score} ", align="center", font=("Courier", 18, "normal"))

    if player.distance(enemy)<20:
        print("💥 Столкновение! Игра окончена.")
        time.sleep(1)
        break
    if player.distance(enemy_1)<20:
        print("💥 Столкновение! Игра окончена.")
        time.sleep(1)
        break
    if player.distance(enemy_2)<20:
        print("💥 Столкновение! Игра окончена.")
        time.sleep(1)
        break