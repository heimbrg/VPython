from visual import *

#Objekte erzeugen
auto1 = box(pos=vector(-200,9,0), size=vector(20,12,8), color=color.blue)
auto2 = box(pos=vector(-200,-9,0), size=vector(20,12,8), color=color.red)
track = box(pos=vector(0,0,-5), size=vector(420,35,2), color=color.white)

attach_trail(auto1, type='spheres')
attach_trail(auto2, type='spheres')

#Anfangswerte
v1 = vector(30,0,0)
v2 = vector(50,0,0)

#Animations Loop
dt = 0.2
zeit = 0
while zeit < 6:
    rate(20)
    auto1.pos = auto1.pos + v1*dt
    auto2.pos = auto2.pos + v2*dt
    zeit = zeit + dt
