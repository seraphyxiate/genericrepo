from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
print bob
bob.delay = 0.01
	
import math
		
def polyline(t, n, length, angle):
	for i in range(n):
		fd(t, length)
		lt(t, angle)		
		
def polygon(t, n, length):
	angle = 360.0 / n
	polyline(t, n, length, angle)

def spokes(t, n, length):
	polygon(t, n, length)
	radius = float(length/(2*math.sin(math.pi/n)))
	interiorAngle = (180-360/n)/2
	lt(t,interiorAngle)
	fd(t,radius)
	for i in range(n):	
		rt(t,180-360/n)
		fd(t,radius)
		lt(t,180)
		fd(t,radius)		

spokes(bob, 18, 50)
wait_for_user()