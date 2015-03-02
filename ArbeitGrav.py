from visual import *

#Konstanten
G = 6.67e-11
Me = 6e24
m = 1000
Re = 6.4e6
dx = 1000

#Anfangsbedingungen
r = 10*Re
Wtotal = 0

#loop
while r > Re
  Fg = G*Me*m/(r*r)
  W = Fg*dx
  Wtotal = Wtotal + W
  r = r - dx
  
#output
print Wtotal
