from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from math import cos,sin,pi
from time import sleep
point=[0,0]
g=9.8

def set_identity(r,c):
	a=[[0 for col in range(c)] for row in range(r)]
	for i in range(r):
		for j in range(c):
			if i==j:
				a[i][j]=1

	return a

def my_init():
	global	v,g
	glClearColor(0.0,0.0,0.0,0.0)
	gluOrtho2D(0,(v**2)/g,0,(v**2)/(2*g))

def input():
	global v,theta
	v=int(raw_input('Enter initial velocity (m/s):'))
	theta=float(raw_input('Enter angle (degrees):'))
	theta=(theta*pi)/180.0

def matrix_mul(a,b):
	m=len(a)
	n=len(a[0])
	p=len(b)
	q=len(b[0])
	if n==p:
		c=[[0 for col in range(q)] for row in range(m)]
		for i in range(m):
			for j in range(q):
				for k in range(n):
					c[i][j]=c[i][j]+(a[i][k]*b[k][j])
		return	c

def translate(tx,ty):
	global	point
	t=set_identity(3,3)
	t[2][0]=tx
	t[2][1]=ty
	X=[[point[0],point[1],1]]
	X=matrix_mul(X,t)

	return X[0][0],X[0][1]
def SetPixel(x,y):
	glPointSize(10)
	glColor3f(1.0,1.0,1.0)
	glBegin(GL_POINTS)
	glVertex2f(x,y)
	glEnd()
	glFlush()

def display():
	global v,theta,point,g
	glClear(GL_COLOR_BUFFER_BIT)
	x=y=0
	t=0
	while point[1]>=0:
		glClear(GL_COLOR_BUFFER_BIT)
		x,y=translate((v*cos(theta)*t),((v*sin(theta)*t)-(0.5*g*(t**2))))
		t+=0.01#step by 0.5 seconds
		SetPixel(x,y)
		sleep(0.001)	
	sys.exit()

def main():
	input()
	global v,theta,g
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowPosition(100,100)
	glutInitWindowSize(int((v**2)/g),int((v**2)/(2*g)))
	glutCreateWindow('parabolic motion.')
	
	glutDisplayFunc(display)
	my_init()
	glutMainLoop()

main()