
#Konstanten (sämtliche Angaben in Grundeinheiten)
G = 6.67e-11 #Gravitationskonstante
Me = 6e24 #Masse der Erde
m = 1000 #Masse des Steins
Re = 6.4e6 #Radius der Erde
dx = 1000 #Distanz

#Anfangsbedingungen
r = 10*Re
Wtotal = 0 

#loop
while r > Re:
  Fg = G*Me*m/(r*r)
  W = Fg*dx
  Wtotal = Wtotal + W
  r = r - dx
  
#output
print Wtotal
