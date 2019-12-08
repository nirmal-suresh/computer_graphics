from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

points=[]

def my_init():
	glClearColor(0.0,0.0,0.0,0.0)
	gluOrtho2D(0,600,0,600)

def input():
	global points
	for i in range(4):
		print 'Enter control point ',i+1,': '
		x,y=map(int,raw_input().split())
		points.append([x,y])

def matrix_mul(a,b):
	m=len(a)
	n=len(a[0])
	p=len(b)
	q=len(b[0])

	c=[[0 for col in range(q)] for row in range(m)]
	for i in range(m):
		for j in range(q):
			for k in range(n):
				c[i][j]+=a[i][k]*b[k][j]

	return c

def fact(n):
	if n==1:
		return 1
	else:
		return n*fact(n-1)

def setPixel(x,y):
	glColor(1.0,0.0,0.0)
	glPointSize(1)
	glBegin(GL_POINTS)
	glVertex2f(x,y)
	glEnd()
	glFlush()

def setBigPixel(x,y):
	glColor(1.0,1.0,1.0)
	glPointSize(5)
	glBegin(GL_POINTS)
	glVertex2f(x,y)
	glEnd()
	glFlush()

def combination(n,r):
	return fact(n)/(fact(r)*fact(n-r))

def bezier():
	global points
	for i in range(4):
		setBigPixel(points[i][0],points[i][1])

	N=[[-1,3,-3,1],[3,-6,3,0],[-3,3,0,0],[1,0,0,0]]
	u=0
	X=[[points[0][0]],[points[1][0]],[points[2][0]],[points[3][0]]]
	Y=[[points[0][1]],[points[1][1]],[points[2][1]],[points[3][1]]]
	while u<=1:
		U=[[u**3,u**2,u,1]]
		x=matrix_mul(matrix_mul(U,N),X)
		y=matrix_mul(matrix_mul(U,N),Y)
		setPixel(x[0][0],y[0][0])
		u+=0.001

def display():
	glClear(GL_COLOR_BUFFER_BIT)
	bezier()

def main():
	input()
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowPosition(100,100)
	glutInitWindowSize(600,600)
	glutCreateWindow('bezier curve')

	my_init()
	glutDisplayFunc(display)
	glutMainLoop()

main()