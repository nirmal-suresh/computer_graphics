from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def setPixel(xcoordinate,ycoordinate):

    glBegin(GL_POINTS)
    glVertex2i(xcoordinate,ycoordinate)
    glEnd()
    glFlush()

def drawCircle(xc,yc,x,y):
	setPixel(xc+x,yc+y)
	setPixel(xc-x,yc+y)
	setPixel(xc+x,yc-y)
	setPixel(xc-x,yc-y)
	setPixel(xc+y,yc+x)
	setPixel(xc-y,yc+x)
	setPixel(xc+y,yc-x)
	setPixel(xc-y,yc-x)

def circle(xc,yc,R):
	x=0
	y=R
	d=3-2*R
	drawCircle(xc,yc,x,y)
	while y>=x:
		x=x+1
		if d>0:
			y=y-1
			d=d+4*(x-y)+10
		else:
			d=d+4*x+6
		drawCircle(xc,yc,x,y)


def mh(x,y,delta):
	x=x+1
	delta=delta+(2*x)+1

def md(x,y,delta):
	x=x+1
	y=y+1
	delta=delta+(2*x)-(2*y)+2

def mv(x,y,delta):
	y=y-1
	delta=delta-(2*y)+1