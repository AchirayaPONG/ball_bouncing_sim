import turtle
import random


class Ball:
    def __init__(self, canvas_width, canvas_height, ball_radius):
        self.xpos = random.randint(-1*canvas_width + ball_radius, canvas_width
                                   - ball_radius)
        self.ypos = random.randint(-1*canvas_height + ball_radius,
                                   canvas_height - ball_radius)
        self.vx = random.randint(1, 0.01*canvas_width)
        self.vy = random.randint(1, 0.01*canvas_height)
        self.ball_color = (random.randint(0, 255), random.randint(0, 255),
                           random.randint(0, 255))
        self.canvas_radius = ball_radius


    def move_circle(self, canvas_width, canvas_height):
        # update the x, y coordinates of ball i with velocity in the x (vx)
        # and y (vy) components
        self.xpos += self.vx
        self.ypos += self.vy

        # if the ball hits the side walls, reverse the vx velocity
        if abs(self.xpos + self.vx) > (canvas_width - self.canvas_radius):
            self.vx = -self.vx

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(self.ypos + self.vy) > (canvas_height - self.canvas_radius):
            self.vy = -self.vy

    def draw_circle(self):
        # draw a circle of radius equals to size at x, y coordinates
        # and paint it with color
        turtle.penup()
        turtle.goto(self.xpos, self.ypos - self.canvas_radius)
        turtle.pendown()
        turtle.color(self.ball_color)
        turtle.begin_fill()
        turtle.circle(self.canvas_radius)
        turtle.end_fill()


class Ball_simulator:
    def __init__(self, num_balls, canvas_width, canvas_height, ball_radius):
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.ball_radius = ball_radius
        self.balls = []
        for i in range(num_balls):
            self.balls.append(Ball(canvas_width, canvas_height, ball_radius))


_num_balls = int(input("Number of balls to simulate: "))
turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()
_canvas_width, _canvas_height = turtle.screensize()
_ball_radius = 0.05 * _canvas_width
turtle.colormode(255)
simulator_ = Ball_simulator(_num_balls, _canvas_width, _canvas_height,
                            _ball_radius)

while True:
    turtle.clear()
    for ball in simulator_.balls:
        ball.draw_circle()
        ball.move_circle(_canvas_width, _canvas_height)
    turtle.update()
