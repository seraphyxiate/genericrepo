from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
print bob
bob.delay = 0.01
	
import math
	
def square(t,length):
	for i in range(4):
		fd(t, length)
		lt(t)
		
def polyline(t, n, length, angle):
	for i in range(n):
		fd(t, length)
		lt(t, angle)		
		
def polygon(t, n, length):
	angle = 360.0 / n
	polyline(t, n, length, angle)
	
def circle(t, r):
	arc(t, r, 360)
	
def arc(t, r, angle):
	arc_length = 2 * math.pi * r * angle / 360
	n = int(arc_length / 3) + 1
	step_length = arc_length / n
	step_angle = float(angle) / n
	polyline(t, n, step_length, step_angle)
	
def petal(t,r,angle): #draws a single petal
	for i in range(2): #petal is drawn in two arcs
		arc(t,r,angle)
		lt(t,180-angle) #turning at 180-angle, redrawing the arc leads to the origin

def flower(t,r,angle,n):
	for i in range(n): #n=qty. of petals
		petal(bob,r,angle)
		lt(bob,360.0/n)
		
flower(bob,100,45,8)

wait_for_user()