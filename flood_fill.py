from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from parametric_circle import circle
from time import sleep
d=0
def myInit():

	glClearColor(1.0,1.0,1.0,1.0)
	glColor3f(0.0,0.0,0.0)
	glPointSize(1.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0,600,0,600)

def readInput():
	global R,xc,yc
	print 'Radius,xc,yc:'
	R,xc,yc = map(int,raw_input().split())

def Display():
		global d
		if d==1:
			return
		glClear(GL_COLOR_BUFFER_BIT)
		circle(xc,yc,R)

def floodFill(x,y,old_color,new_color):
	toFill = []
	toFill.append((x,y))

	while toFill:
		(x,y)=toFill.pop(0)
		color=glReadPixels(x,y,1,1,GL_RGB,GL_FLOAT)
		if((color[0][0][0]==old_color[0][0][0]) and (color[0][0][1]==old_color[0][0][1]) and (color[0][0][2]==old_color[0][0][2])):
			setPixelColor(x,y,new_color)
			toFill.append((x,y+1))
			toFill.append((x+1,y))
			toFill.append((x-1,y))
			toFill.append((x,y-1))

def setPixelColor(x,y,color):
	glColor3f(color[0][0][0],color[0][0][1],color[0][0][2])
	glBegin(GL_POINTS)
	glVertex2i(int(round(x)),int(round(y)))
	glEnd()
	glFlush()

def onMouseClick(button,state,x,y):
	global d
	if d==1:
		return
	new_color=[[[1.0,0.0,0.0]]]
	old_color=[[[1.0,1.0,1.0]]]
	floodFill(x,600-y,old_color,new_color)
	d=d+1

def main():
	
	readInput()
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(600,600)
	glutInitWindowPosition(50,50)
	glutCreateWindow("flood_fill")
	glutDisplayFunc(Display)
	new_color=[[[1.0,0.0,0.0]]]
	old_color=[[[1.0,1.0,1.0]]]

	glutMouseFunc(onMouseClick)
	myInit()
	glutMainLoop()
main()