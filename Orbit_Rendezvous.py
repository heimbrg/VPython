from visual import *
from visual.graph import *
 
 
# scene2 bezeichnet das Ausgabefenster, etwas grösser als standartmässig
scene2=display(width=800,height=800, x=0, y=0, title='Orbit')
 
# Dies erzeugt die Erde. Alle Distanzen werden in Erdradien angegeben
Erde=sphere(pos=vector(0,0,0), radius=1, material=materials.earth)
 
# Startpunkt für das Raumschiff
R=2.75
# GM ist eine Konstante
GM=1.47
# v ist die theoretische Geschwindigkeit für einen kreisförmigen Orbit
v=sqrt(GM/R)
 
# das Objekt objekt2 ist einfach eine Kugel, die die Erde umrundet
objekt2=sphere(pos=vector(1.5*R,0,0), radius=0.1, color=color.red, make_trail=True)
 
# Die Masse von objekt2
objekt2.m=1
# der anfängliche Impuls (Masse * Geschwindigkeit), ein Vektor
objekt2.p=vector(0,-sqrt(GM/(1.5*R)),0)
               
# L ist die Länge des Raumschiffes
L=.2
# rs steht für Raumschiff. Es ist ein Kegel (cone), dass man die Richtung erkennen kann

rs=cone(pos=vector(R,0,0), axis=(0,L,0), radius=.1, color=color.cyan,
        make_trail=True, retain=1300)
 
 
# Masse und Impuls (Masse * Geschwindigkeit) für das Raumschiff
rs.m=1
rs.p=vector(0,-v,0)*rs.m
 
# ff bezeichnet die Kraft der Triebwerke
ff=0.25
 
# dt ist der Zeitabschnitt für die Berechnugsschritte
dt=0.01
 
# Startzeit
t=0
 
# Der Winkel um den das Raumschiff bei einem Tastendruck gedreht wird
dtheta=10*pi/180
 
# dwinkel bezeichnet den Winkel zur kreisförmigen Raumschiffbahn
dwinkel=0
 
# Die Kraft F
F=vector(0,0,0)
 
# exhaust ist der Ausstoss des Triebwerks. Ein kleiner Pfeil, der anzeigt, wann das Triebwerk läuft
exhaust=arrow(pos=rs.pos, axis=-rs.axis, color=color.yellow, opacity=0)
 
 
# die Hauptschleife, läuft solange bis das Programm abgebrochen wird
while True:
 
    rate(100)
 
    # opacity=0 bedeutet, dass der Vektor unsichtbar wird (opacity=Deckkraft)
    exhaust.opacity=0
 
    F=vector(0,0,0)
 
    # Wird eine Taste gedrückt?
    if scene2.kb.keys:
        # Nimmt die gedrückte Taste und nennt sie k
        k= scene2.kb.getkey()
 
        # ist k der Hoch-Pfeil 
        if k =='up':
            # besitzt die Kraft die gleiche Richtung wie der cone: (norm(rs.axis)) ist ein Vektor mit der Länge 1 in der Richtung von rs.axis
            F=F+ff*norm(rs.axis)
 
            # der exhaust Vektor wird sichtbar
            exhaust.opacity=1
 
 
        # das gleiche wenn der Unten-Pfeil gedrückt wurde, aber Minus
        if k=='down':
            F=F-ff*norm(rs.axis)
            
            exhaust.opacity=1
 
        # wird der Links-Pfeil gedrückt, dreht sich das Raumschiff nach links (eigentlich wird hier zunächst nur der Winkel dwinkel verändert)
        if k=='left':
            dwinkel=dwinkel+dtheta
        if k=='right':
            dwinkel=dwinkel-dtheta
    
 
    # das Raumschiff selbst wird gedreht    
    rs.axis=norm(rs.pos)*.2
    rs.rotate(angle=(-pi/2+dwinkel), axis=vector(0,0,1), origin=rs.pos)
 
    # Hier kommt die Physik ins Spiel:
    # Summe der Kraft des Raumschiffes und der Gravitationskraft
    # **2 meint "hoch 2"
    Ft=-GM*norm(rs.pos)*rs.m/mag(rs.pos)**2+F
 
    # Der Impuls des Raumschiffes wird neu berechnet
    rs.p=rs.p+Ft*dt
 
    # Die neue Position des Raumschiffes wird berechnet:
    # Neue Position = alte Position*v*dt (v = p/m)
    rs.pos=rs.pos+rs.p*dt/rs.m
 
    # Das Selbe für alle anderen Objekte
    objekt2.p=objekt2.p-dt*GM*norm(objekt2.pos)/mag(objekt2.pos)**2
    objekt2.pos=objekt2.pos+objekt2.p*dt/objekt2.m
    
    # Position und Richtung des exhaust Vektors
    exhaust.pos=rs.pos
    exhaust.axis=-rs.axis
 
    # Update der Zeit
    t=t+dt

