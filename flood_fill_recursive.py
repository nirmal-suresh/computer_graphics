from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from bressenham_circle import circle

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
		glClear(GL_COLOR_BUFFER_BIT)
		circle(xc,yc,R)

def floodFill(x,y,old_color,new_color):
	color=glReadPixels(x,y,1,1,GL_RGB,GL_FLOAT)
	if((color[0][0][0]==old_color[0][0][0]) and (color[0][0][1]==old_color[0][0][1]) and (color[0][0][2]==old_color[0][0][2])):
		setPixelColor(x,y,new_color)
		floodFill(x+1,y,old_color,new_color)
		floodFill(x,y+1,old_color,new_color)
		floodFill(x-1,y,old_color,new_color)
		floodFill(x,y-1,old_color,new_color)

def setPixelColor(x,y,color):
	glColor3f(color[0][0][0],color[0][0][1],color[0][0][2])
	glBegin(GL_POINTS)
	glVertex2i(int(round(x)),int(round(y)))
	glEnd()
	glFlush()

def onMouseClick(button,state,x,y):
	new_color=[[[1.0,0.0,0.0]]]
	old_color=[[[1.0,1.0,1.0]]]
	print x,y
	floodFill(x,600-y,old_color,new_color)

def main():
	
	readInput()
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(600,600)
	glutInitWindowPosition(50,50)
	glutCreateWindow("DDA Line Algorithm")
	glutDisplayFunc(Display)
	new_color=[[[1.0,0.0,0.0]]]
	old_color=[[[1.0,1.0,1.0]]]

	glutMouseFunc(onMouseClick)
	myInit()
	glutMainLoop()
main()