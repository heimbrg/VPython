#Libraries
from visual import *
from random import randint

#Variables
particles = []
num = 50
mass = 10000000000000
dt = 0.02
G = 6.67384*10**(-11)

#Object Gen
for i in xrange(0,num):
    particles.append(sphere(pos = vector(randint(-200,200),randint(-200,200),randint(-200,200)), f = vector(0,0,0), v = vector(0,0,0), a = vector(0,0,0), make_trail=True))

#Main loop
while True:
    rate(100000)
    for i in particles:
        i.f = vector(0,0,0)
        for j in particles:
            if i.pos - j.pos != vector(0,0,0):
                i.f = i.f + ((G*mass**2)/mag(i.pos-j.pos)**2)*(j.pos-i.pos)
        i.a = i.f/mass
        i.v = i.v + i.a*dt
        i.pos = i.pos + i.v*dt
        
