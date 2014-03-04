from visual import *
from fractions import Fraction

scene.width=1000
scene.height=800
scene.title='Gravitation'
scene.autoscale=False
scene.fullscreen=False

#Massen
m1=100
m2=100
m3=0.01

e1=0.1
e2=0.1
e3=0.1

r1=pow(m1,Fraction(1,3))*e1
r2=pow(m2,Fraction(1,3))*e2
r3=pow(m3,Fraction(1,3))*e3
G=3
dt=0.0001

print r1
print r2
print r3

pos1=vector(0,0,0)
pos2=vector(20,0,0)
pos3=vector(10,0,0)

v1=vector(0,0,0)
v2=vector(0,5,1)
v3=vector(-2,3,0)

p1=sphere(pos=pos1, radius=r1, color=color.red)
p2=sphere(pos=pos2, radius=r2, color=color.green)
p3=sphere(pos=pos3, radius=r3, color=color.blue)
p1.trail=curve(color=p1.color)
p2.trail=curve(color=p2.color)
p3.trail=curve(color=p3.color)

def grav(p,p_m,m):
    r=p-p_m
    r_mag=mag(r)
    r_norm=norm(r)
    a=(-G*m/(r_mag**2))*r_norm
    return a

while True:
    rate(10000)
    
    a1=grav(p1.pos, p2.pos, m2) + grav(p1.pos, p3.pos, m3)
    dv1 =a1*dt
    v1=v1+dv1
    dp1=v1*dt

    a2=grav(p2.pos, p1.pos, m1) + grav(p2.pos, p3.pos, m3)
    dv2 =a2*dt
    v2=v2+dv2
    dp2=v2*dt

    a3=grav(p3.pos, p1.pos, m1) + grav(p3.pos, p2.pos, m2)
    dv3 =a3*dt
    v3=v3+dv3
    dp3=v3*dt

    
    p1.pos=p1.pos+dp1
    p1.trail.append(pos=p1.pos)
    p2.pos=p2.pos+dp2
    p2.trail.append(pos=p2.pos)
    p3.pos=p3.pos+dp3
    p3.trail.append(pos=p3.pos)

    scene.center=p1.pos
    
    if mag(p1.pos-p2.pos)<(r1+r2) or mag(p1.pos-p3.pos)<(r1+r3) or mag(p3.pos-p2.pos)<(r3+r2):
        print "Kollision!!"
        break

    
    
