import turtle as t
tim=t.Turtle()
tim.shape("turtle")


# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# 132 no video
# my solve
# arm=3
# for _ in range(arm):
#
#     tim.forward(100)
#     tim.right(360/arm)
#
# arm+=1
# for _ in range (arm):
#     tim.forward(100)
#     tim.right(360/arm)
# arm+=1
# for _ in range (arm):
#     tim.forward(100)
#     tim.right(360/arm)
# arm+=1
# for _ in range (arm):
#     tim.forward(100)
#     tim.right(360/arm)
# arm+=1
# for _ in range (arm):
#     tim.forward(100)
#     tim.right(360/arm)
# arm+=1
# for _ in range (arm):
#     tim.forward(100)
#     tim.right(360/arm)


# course solve
import random
tim.width(5)
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def draw_shape(new_sides):
    angle = 360/ new_sides
    for _ in range (new_sides):
        tim.forward(100)
        tim.right(angle)
for i in range(3,11):
    tim.color(random.choice(colours))
    draw_shape(i)