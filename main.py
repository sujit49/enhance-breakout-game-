import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.title("Enhanced Breakout Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Game variables
score = 0
lives = 3
level = 1
brick_rows = 5
ball_speed_increment = 0.5

# Paddle setup
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball setup
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, -230)
ball.dx = 2
ball.dy = 2

# Brick setup
bricks = []
colors = ["red", "orange", "yellow", "green", "blue"]

def create_bricks():
    global bricks
    bricks = []
    for y in range(brick_rows):
        for x in range(-350, 400, 70):
            brick = turtle.Turtle()
            brick.shape("square")
            brick.color(colors[y % len(colors)])
            brick.shapesize(stretch_wid=1, stretch_len=3)
            brick.penup()
            brick.goto(x, 250 - y * 30)
            bricks.append(brick)

create_bricks()

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(f"Score: {score} | Lives: {lives} | Level: {level}", align="center", font=("Courier", 18, "normal"))

# Paddle movement
def paddle_left():
    x = paddle.xcor()
    if x > -350:
        paddle.setx(x - 20)

def paddle_right():
    x = paddle.xcor()
    if x < 350:
        paddle.setx(x + 20)

# Keyboard bindings
screen.listen()
screen.onkeypress(paddle_left, "Left")
screen.onkeypress(paddle_right, "Right")

# Power-up setup
power_ups = []

def create_power_up(x, y):
    power_up = turtle.Turtle()
    power_up.shape("circle")
    power_up.color("gold")
    power_up.penup()
    power_up.goto(x, y)
    power_up.dy = -2
    power_ups.append(power_up)

# Reset ball
def reset_ball():
    ball.goto(0, -230)
    ball.dx *= random.choice([-1, 1])
    ball.dy = 2

# Update score display
def update_score():
    score_display.clear()
    score_display.write(f"Score: {score} | Lives: {lives} | Level: {level}", align="center", font=("Courier", 18, "normal"))

# Game loop
running = True
while running:
    screen.update()

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Ball collision with walls
    if ball.xcor() > 390:  # Right wall
        ball.setx(390)
        ball.dx *= -1

    if ball.xcor() < -390:  # Left wall
        ball.setx(-390)
        ball.dx *= -1

    if ball.ycor() > 290:  # Top wall
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:  # Bottom wall
        lives -= 1
        update_score()
        if lives == 0:
            score_display.clear()
            score_display.write("Game Over!", align="center", font=("Courier", 24, "normal"))
            running = False
        else:
            reset_ball()

    # Ball collision with paddle
    if (ball.ycor() > -240 and ball.ycor() < -230) and (
        ball.xcor() > paddle.xcor() - 50 and ball.xcor() < paddle.xcor() + 50
    ):
        ball.sety(-230)
        ball.dy *= -1

    # Ball collision with bricks
    for brick in bricks:
        if brick.isvisible() and (
            ball.xcor() > brick.xcor() - 35
            and ball.xcor() < brick.xcor() + 35
            and ball.ycor() > brick.ycor() - 15
            and ball.ycor() < brick.ycor() + 15
        ):
            ball.dy *= -1
            brick.hideturtle()
            score += 10
            update_score()
            # Randomly drop power-up
            if random.random() < 0.2:
                create_power_up(brick.xcor(), brick.ycor())

    # Power-up movement and collection
    for power_up in power_ups:
        power_up.sety(power_up.ycor() + power_up.dy)
        if power_up.ycor() < -300:
            power_ups.remove(power_up)
            power_up.hideturtle()
        elif (
            power_up.ycor() > -250
            and power_up.ycor() < -230
            and power_up.xcor() > paddle.xcor() - 50
            and power_up.xcor() < paddle.xcor() + 50
        ):
            power_ups.remove(power_up)
            power_up.hideturtle()
            lives += 1
            update_score()

    # Check if all bricks are cleared
    if all(not brick.isvisible() for brick in bricks):
        brick_rows += 1
        level += 1
        ball.dx += ball_speed_increment
        ball.dy += ball_speed_increment
        create_bricks()
        reset_ball()
        update_score()

screen.mainloop()

