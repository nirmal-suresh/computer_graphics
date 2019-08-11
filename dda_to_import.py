from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from math import floor

def setPixel(xcoordinate,ycoordinate):

    glBegin(GL_POINTS)
    glVertex2i(xcoordinate,ycoordinate)
    glEnd()
    glFlush()

def Sign(x):
	if x<0:
		return -1
	elif x==0:
		return 0
	else:
		return 1

def Integer(a):
	return int(a-0.5)

def lineDDA(x1,y1,x2,y2):
	if abs(x2-x1)>=abs(y2-y1):
		Length=abs(x2-x1)
	else:
		Length=abs(y2-y1)

	dx=(x2-x1)/Length
	dy=(y2-y1)/Length

	x=x1+0.5
	y=y1+0.5

	i=1

	while i<=Length:
		setPixel(Integer(x),Integer(y))
		x=x+dx
		y=y+dy
		i=i+1

