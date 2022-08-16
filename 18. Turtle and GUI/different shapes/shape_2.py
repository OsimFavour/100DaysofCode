import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()
t.colormode(255)


def random_color():
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	color = (r, g, b)
	return color


def shape(num_sides):
	angle = 360 / num_sides
	for _ in range(num_sides):
		tim.forward(100)
		tim.right(angle)


# Setheading so that the different shapes will fit into it's line
tim.setheading(90)
for _ in range(5):
	tim.forward(10)
	tim.penup()
	tim.forward(10)
tim.setheading(0)
tim.pendown()

for n_side in range(3, 10):
	tim.color(random_color())
	shape(n_side)
