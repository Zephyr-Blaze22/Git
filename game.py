import turtle

#window
window=turtle.Screen()
window.title('Lesson 1.')
window.bgcolor('Black')
window.setup(width=600, height=600)

# player
player=turtle.Turtle()
player.shape('square')
player.color('red')
player.pu()
player.speed(0)

# func
def go_up():
    y=player.ycor()
    if y+20 <300:
        player.sety(y+20)
    else:
        player.sety(y)

def go_down():
    y=player.ycor()
    if y-20 >-300:
        player.sety(y-20)
    else:
        player.sety(y)

def go_right():
    x=player.xcor()
    if x+20<300:
        player.setx(x+20)
    else:
        player.setx(x)

def go_left():
    x=player.xcor()
    if x-20>-300:
        player.setx(x-20)
    else:
        player.setx(x)

# buttoms
window.listen()
window.onkeypress(go_up, 'w')
window.onkeypress(go_down, 's')
window.onkeypress(go_right, 'd')
window.onkeypress(go_left, 'a')

while True:
    window.update()