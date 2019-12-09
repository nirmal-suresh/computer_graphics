from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from math import sin,cos,pi
from time import sleep
xc=yc=r=0
xs=ys=R=0
def setIdentity():
	c=[[0 for col in range(3)] for row in range(3)]

	for i in range(3):
		for j in range(3):
			if i==j:
				c[i][j]=1
	return c

def my_init():
	glClearColor(0.0,0.0,0.0,0.0)
	gluOrtho2D(0,600,0,600)

def setPixel(x,y):
	glColor(1.0,1.0,1.0)
	glBegin(GL_POINTS)
	glVertex2f(x,y)
	glEnd()

def para_semi_circle(xc,yc,r):
	theta=0
	step=1/float(r)
	while theta<pi:
		x=xc+(r*cos(theta))
		y=yc+(r*sin(theta))
		setPixel(x,y)
		theta+=step

	for x in range(xc-r,xc+r+1):
		setPixel(x,yc)

def dda_circle(xc,yc,r):
	x1=r
	y1=0
	sx=x1
	sy=y1
	val=0
	i=0
	while val<r:
		val=2**i
		i+=1
	e=1/float(2**(i-1))

	x2=x1+(e*y1)
	y2=y1-(e*x2)
	setPixel(xc+x2,yc+y2)
	x1=x2
	y1=y2
	while (y1-sy)<e or (sx-x1)>e:
		x2=x1+(e*y1)
		y2=y1-(e*x2)
		setPixel(xc+x2,yc+y2)
		x1=x2
		y1=y2

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

def translate(tx,ty):
	global xc,yc
	T=setIdentity()
	T[2][0]=tx
	T[2][1]=ty
	X=[[xc,yc,1]]
	X=matrix_mul(X,T)
	xc=X[0][0]
	yc=X[0][1]

def rotate(theta,xr,yr):
	global xc,yc
	translate(-xr,-yr)
	T=setIdentity()
	T[0][0]=cos(theta)
	T[0][1]=-sin(theta)
	T[1][0]=sin(theta)
	T[1][1]=cos(theta)
	X=[[xc,yc,1]]
	X=matrix_mul(X,T)
	xc=X[0][0]
	yc=X[0][1]
	translate(xr,yr)

def display():
	global xs,ys,R,r,xc,yc
	glClear(GL_COLOR_BUFFER_BIT)
	para_semi_circle(xs,ys,R)
	xc=xs-R-r
	yc=ys
	theta=0
	step=1/float(R)

	while theta<pi:
		glutSwapBuffers()
		sleep(0.1)
		glClear(GL_COLOR_BUFFER_BIT)
		para_semi_circle(xs,ys,R)
		dda_circle(xc,yc,r)
		rotate(step,xs,ys)
		theta+=step
		print theta
		


def input():
	global xs,ys,R,r
	print 'Enter center of semi-circle:'
	xs,ys=map(int,raw_input().split())
	R=int(raw_input('Enter radius of semi circle:'))
	r=int(raw_input('Enter radius of ball:'))

def main():
	input()
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
	glutInitWindowPosition(100,100)
	glutInitWindowSize(600,600)
	glutCreateWindow('ball moving aroun semi circle.')

	my_init()
	glutDisplayFunc(display)
	glutMainLoop()

main()