import turtle as t
import random
tim=t.Turtle()
tim.shape("turtle")
t.colormode(255)
tim.pensize(10)
tim.speed("fastest")

def random_color():
    r= random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color= (r,g,b)
    return color
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions=[0,90,180,270]
for i in range(280):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))








