import turtle
import time

# Score
score_a = 0
score_b = 0

#Setting up the screen, title, background color, width etc.
# must return the window created
def setUpScreen():
    # Set up the screen
    wn = turtle.Screen()
    # Set background color
    wn.bgcolor('light green')
    # Set height and width
    wn.setup(width = 800, height = 600)
    wn.title('Virtual Ping Pong')
    # Turns off the screen updates
    wn.tracer(0)
    return wn

# Create and return the paddle
# a and b will give the position of the paddle on the screen
def createPaddle(a, b):
    paddle = turtle.Turtle()
    # Set speed, shape, color and penup
    paddle.color('green')
    paddle.shape('square')
    paddle.penup()
    paddle.speed(0)
    paddle.goto(a,b)
    # move paddle to the left/right of the screen
    # position of the paddle is given by a and b
    paddle.shapesize(5, 1)
    return paddle

# Create and return the ball
def createBall():
    ball = turtle.Turtle()
    # Set speed, shape, color and penup
    ball.speed(0)
    ball.shape('circle')
    ball.color('purple')
    ball.penup()
    # setting delta for the ball movement 
    ball.dx = 3
    ball.dy = 2
    return ball

# Write score and highscore on the screen
# when a player will miss the ball score is given to the other player
def trackScoreOnScreen():
    pen = turtle.Turtle()
    # Set color, speed
    pen.color('Teal')
    pen.speed(0)
    # penup and hide turtle
    pen.penup()
    pen.hideturtle()
    # Move the score to top of screen
    pen.goto(0,260)
    pen.write("Player A: 0  Player B: 0", align='center', font=('Times New Roman', 24, 'bold'))
    return pen

# Function to call to move the ball automatically
# should be called from the main loop. 
def moveBall():
    # Moving Ball
    x = ball.xcor()
    y = ball.ycor()
    ball.setx(x+ball.dx)
    ball.sety(y+ball.dy)
    # remove print statement after implementing this function

# Function to be called by pressing up key 
# It will help to move paddle A in upwards to save ball from touching the border
def paddle_a_up():
    # remove print statement after implementing this function
    y = paddle_a.ycor()
    if y<300:
        paddle_a.sety(y+20)

# Function to be called by pressing 'a' key 
# It will help to move paddle B in upwards to save ball from touching the border
def paddle_b_up():
    # remove print statement after implementing this function
    y = paddle_b.ycor()
    if y<300:
        paddle_b.sety(y+20)

# Function to be called by pressing down key 
# It will help to move paddle A in downwards to save ball from touching the border
def paddle_a_down():
    # remove print statement after implementing this function
    y = paddle_a.ycor()
    if y>-300:
        paddle_a.sety(y-20)

# Function to be called by pressing 'z' key 
# It will help to move paddle B in downwards to save ball from touching the border
def paddle_b_down():
    # remove print statement after implementing this function
    y = paddle_b.ycor()
    if y>-300:
        paddle_b.sety(y-20)

# Bind 'a', 'z', 'up' and 'down' keys with their function
def bindKeyboardKeys(wn):
    # remove print statement after implementing this function
    wn.listen()
    wn.onkeypress(paddle_a_up, 'w')
    wn.onkeypress(paddle_a_down, 's')
    wn.onkeypress(paddle_b_up, 'Up')
    wn.onkeypress(paddle_b_down, 'Down')

# detect collision of ball with the borders, 
# increment the score
# handle the bounce of the ball
def detectHandleBallCollisionWithBorders(ball, trackScore):
    global score_a
    global score_b
    
    # checking if ball touching top or bottom of the screen
    y = ball.ycor()
    if y>280 or y<-280:
        ball.dy *=  -1
    
    # r1everse the direction of the ball wrt y axis 
    
    # check if ball touches right side border of the screen
    if ball.xcor() > 390:
        # reset ball at origin and move the ball
        ball.goto(0, 0)
        ball.dx *= -1
        # increment score for player A
        score_a+=1
        # update the score on the top of the screen
        trackScore.clear()
        trackScore.write("Player A: {}  Player B: {}".format(score_a, score_b), align='center', font=('Courier', 24, 'bold'))
        time.sleep(1)
        print('detect ball collision on the right side of the screen')

    # check if ball touches left side border of the screen
    if ball.xcor() < -390:
        # reset ball at origin and move the ball
        ball.goto(0, 0)
        ball.dx *= -1
        # increment score for player B
        score_b+=1
        trackScore.clear()
        trackScore.write("Player A: {}  Player B: {}".format(score_a, score_b), align='center', font=('Courier', 24, 'bold'))
        # update the score on the top of the screen
        time.sleep(1)
        print('detect ball collision on the left side of the screen')

    print("detectHandleBallCollisionWithBorders function called")

# detect and handle collision of the ball with the paddle
# if ball will touch the paddle,  push ball in reverse direction 
def detectHandleBallCollisionWithPaddle(ball):
    # detect collision with the right paddle and paddle lenght
    # set x axis to the right boundary point
    # reverse the direction 
    # if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() -60):
        
    # detect collision with the left paddle and paddle lenght
    # set x axis to the left boundary point
    # reverse the direction 
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() -60):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() -60):
        ball.setx(-340)
        ball.dx *= -1
    print("detectHandleBallCollisionWithPaddle function called")

####################################
#                                  #
#   Start of the main function     #
#                                  #
####################################

#Call Functions in main program
wn = setUpScreen()
ball = createBall()
paddle_a = createPaddle(-350, 0)
paddle_b = createPaddle(350, 0)
trackScore = trackScoreOnScreen()
bindKeyboardKeys(wn)

# Main game loop
while True:
    wn.update()

    # Moving Ball
    moveBall()

    # Border checking
    detectHandleBallCollisionWithBorders(ball, trackScore)
    
    # Paddle and ball collisions
    detectHandleBallCollisionWithPaddle(ball)
        
    time.sleep(0.01)

wn.mainloop()