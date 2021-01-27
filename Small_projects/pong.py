import turtle
import random
import time

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height = 600)
wn.tracer(0)

class ball_functions():
    def __init__(self):
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("square")
        self.ball.color("White")
        self.ball.penup()
        ball_functions.ball_setup(self, 0) 
        self.old_time = time.time()  

    def movement(self):
        self.ball_y = self.ball.ycor() 
        self.ball_x = self.ball.xcor()
        if (time.time() - self.old_time) > .025:
            self.ball.setx(self.ball_x + self.ball.dx)    
            self.ball.sety(self.ball_y + self.ball.dy) 
            self.old_time = time.time() 

        if self.ball.ycor() > 290:
            self.ball.sety(290)
            self.ball.dy *= -1
        if self.ball.ycor() < -290:
            self.ball.sety(-290)
            self.ball.dy *= -1
        if self.ball.xcor() < -390:
            paddle_b.score +=1
            draw_score(pen)
            ball_functions.ball_setup(self, 3)   
        if self.ball.xcor() > 390:
            paddle_a.score +=1
            draw_score(pen)
            ball_functions.ball_setup(self, -3) 

        if (self.ball.xcor() + 5) > (paddle_b.x - 5):
            if (self.ball.xcor()) < (paddle_b.x + 5):
                if (self.ball.ycor() - 5) < (paddle_b.y + 42):
                    if (self.ball.ycor() + 5) > (paddle_b.y - 42):                           #-2 0  # -0.5 1.5
                            x = paddle_b.x - 10 
                            self.ball.setx(x)
                            self.ball.dx *= -1
                            self.ball.dy += 1
                            self.ball.dx -= 1
        
        if (self.ball.xcor() - 5) < (paddle_a.x + 5):
            if (self.ball.xcor()) > (paddle_a.x - 5):
                if (self.ball.ycor() - 5) < (paddle_a.y + 42):
                    if (self.ball.ycor() + 5) > (paddle_a.y - 42):
                            x = paddle_a.x + 10 
                            self.ball.setx(x)
                            self.ball.dx *= -1
                            self.ball.dy += 2
                            self.ball.dx += 2


          
    def ball_setup(self, value):
        self.ball.goto(0,0) 
        if value != 0:
             self.ball.dy = value
             self.ball.dx = value 
        else:
            self.ball.dx = random.choice([3,-3])                           
            self.ball.dy = self.ball.dx 
        angle = random.uniform(-1.5, 1.5)
        self.ball.dx += angle
        self.ball.dy -= angle   

class paddles:

    paddle = None
    def __init__(self, position):
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("White")
        self.paddle.shapesize(stretch_wid= 5, stretch_len= 1 )
        self.paddle.penup()
        self.paddle.goto(position,0)
        self.score = 0
        self.y = self.paddle.ycor()
        self.x = self.paddle.xcor()

    def move_paddle_up(self):
        y = self.paddle.ycor()
        if y < 250:
            y += 20
            self.paddle.sety(y)
        self.y = self.paddle.ycor()
        self.x = self.paddle.xcor()

    def move_paddle_down(self):
        y = self.paddle.ycor()
        if y > -250:
            y -= 20
            self.paddle.sety(y)
        self.y = self.paddle.ycor()
        self.x = self.paddle.xcor()

paddle_a = paddles(-350)
paddle_b = paddles(350)
ball = ball_functions()

wn.listen()
wn.onkeypress(lambda: paddle_a.move_paddle_up(), "w")
wn.onkeypress(lambda: paddle_a.move_paddle_down(), "s")
wn.onkeypress(lambda: paddle_b.move_paddle_up(), "Up")
wn.onkeypress(lambda: paddle_b.move_paddle_down(), "Down")

pen = turtle.Turtle()
pen.penup()
pen.color("white")
pen.hideturtle()
pen.setundobuffer(None)

def draw_score(pen):
    pen.clear()
    pen.hideturtle()
    pen.goto(-50, 220)
    pen.write("{}".format(paddle_a.score) + "  /  {}".format(paddle_b.score), move=False, align="left", font= ("Arial", 40, "bold"))

draw_score(pen)

while True: 
    wn.update()
    ball.movement()


    