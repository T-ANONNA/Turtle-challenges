import turtle as t
import random
tim=t.Turtle()
tim.shape("turtle")
t.colormode(255)

def random_color():
    r= random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color= (r,g,b)
    return color

tim.width(5)
tim.speed("fastest")
tim.color(random_color())

def draw_spirograph(size_of_gap):
        for i in range(int(360 / size_of_gap)):
            tim.circle(100)
            # print(tim.heading())
            current_heading = tim.heading()
            tim.setheading(current_heading + size_of_gap)
            tim.circle(100)
draw_spirograph(10)




screen=t.Screen()
screen.exitonclick()