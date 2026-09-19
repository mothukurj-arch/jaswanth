import turtle
import math
import random

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Animated Heart for JASWANTH ❤️")

# Main turtle for drawing the heart
t = turtle.Turtle()
t.speed(0)  # Maximum drawing speed so the animation is fast and smooth
t.hideturtle()
t.pensize(1)

colors = ["#ff4d6d", "#ff758f", "#ffb3c1", "#ff2a6d", "#c77dff", "#7b2cbf"]

# Draw the heart perimeter with live animation
num_points = 500
for i in range(num_points):
    t.penup()
    t.goto(0, 0)
    
    angle = i * (math.pi * 2) / num_points
    
    # Heart parametric equations
    x = 16 * (math.sin(angle) ** 3) * 12
    y = (13 * math.cos(angle)
         - 5 * math.cos(2 * angle)
         - 2 * math.cos(3 * angle)
         - math.cos(4 * angle)) * 12
         
    t.color(random.choice(colors))
    t.goto(x, y)
    t.pendown()
    
    # Starburst effect at each point
    for _ in range(8):
        t.forward(6)
        t.backward(6)
        t.right(45)

# --- Neon Text Effect for " JASWANTH " (Appears when the animation completes) ---
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

# 1. Neon Glow Shadow Layer
writer.goto(2, -22)  # Slight offset for 3D depth
writer.color("#ff0000")
writer.write("JASWANTH", align="center", font=("Arial", 36, "bold"))

# 2. Main White Text Core
writer.goto(0, -20)
writer.color("#16f133")
writer.write("JASWANTH", align="center", font=("Arial", 36, "bold"))

turtle.done()