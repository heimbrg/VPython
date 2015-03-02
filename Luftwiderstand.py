# Simulation Fall mit Luftwiderstand
from visual import *

boden = box(length=4, height=0.5, width=4, color=color.blue)

ball = sphere(pos=(0,4,0), color=color.red)
ball.geschwindigkeit = vector(0,-1,0)
ball.beschleunigung = vector(0,9.8,0)

power = 2
constant = .5

dt = 0.01
while 1:
    rate(100)
    ball.pos = ball.pos + ball.geschwindigkeit*dt
    if ball.y < 1:
        ball.geschwindigkeit.y = -ball.geschwindigkeit.y
    else:
		ball.geschwindigkeit.y = ball.geschwindigkeit.y + ball.beschleunigung.y*dt
		ball.accelebeschleunigungration.y = -9.8 - sign(ball.geschwindigkeit.y) * constant * ball.radius * ball.geschwindigkeit.y ** power
		
