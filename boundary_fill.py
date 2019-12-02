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
	gluOrtho2D(0,600,600,0)

def readInput():
	global R,xc,yc
	print 'Radius,xc,yc:'
	R,xc,yc = map(int,raw_input().split())

def Display():
	
		glClear(GL_COLOR_BUFFER_BIT)
		circle(xc,yc,R)

def boundaryFill(x,y,fill_color,border_color):
	color=glReadPixels(x,y,1,1,GL_RGB,GL_FLOAT)
	if(((color[0][0][0]!=fill_color[0][0][0]) or (color[0][0][1]!=fill_color[0][0][1]) or (color[0][0][2]!=fill_color[0][0][2])) and ((color[0][0][0]!=border_color[0][0][0]) or (color[0][0][1]!=border_color[0][0][1]) or (color[0][0][2]!=border_color[0][0][2]))):
		setPixelColor(x,y,fill_color)
		boundaryFill(x+1,y,fill_color,border_color)
		boundaryFill(x,y+1,fill_color,border_color)
		boundaryFill(x-1,y,fill_color,border_color)
		borderFill(x,y-1,fill_color,border_color)

def setPixelColor(x,y,color):
	glColor3f(color[0][0][0],color[0][0][1],color[0][0][2])
	glBegin(GL_POINTS)
	glVertex2i(int(round(x)),int(round(y)))
	glEnd()
	glFlush()

def onMouseClick(button,state,x,y):
	border_color=[[[0.0,0.0,0.0]]]
	fill_color=[[[1.0,0.0,0.0]]]
	print x,y
	boundaryFill(x,y,fill_color,border_color)

def main():
	
	readInput()
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(600,600)
	glutInitWindowPosition(50,50)
	glutCreateWindow("DDA Line Algorithm")
	glutDisplayFunc(Display)
	border_color=[[[1.0,0.0,0.0]]]
	fill_color=[[[1.0,1.0,1.0]]]

	glutMouseFunc(onMouseClick)
	myInit()
	glutMainLoop()
main()