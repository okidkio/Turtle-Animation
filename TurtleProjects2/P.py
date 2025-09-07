from turtle import *
import colorsys
import math

# Screen setup
bgcolor("black")
tracer(0, 0)  # Turn off animation delay for smooth drawing
width(2)       # Line thickness
speed(0)       # Fastest drawing speed

# Create turtle
t = Turtle()
t.hideturtle()
t.up()
t.goto(0, 0)
t.down()

# Spiral parameters
radius = 5
angle = 0
h = 0  # hue value for colors

# Draw spiral with smooth curves and color transitions
for i in range(300):
    # Convert hue to RGB
    c = colorsys.hsv_to_rgb(h % 1, 1, 1)
    t.pencolor(c[0], c[1], c[2])
    
    # Move and draw
    t.circle(radius + i * 0.5, 45)
    t.right(24)
    
    # Gradually change hue for smooth color transition
    h += 0.01
    
    # Update screen for animation effect
    update()

# Keep window open
done()
