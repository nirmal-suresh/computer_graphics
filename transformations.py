from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from bressenham_to_import import line
from math import sin,cos,pi

list=[]
x=300
y=300

def set_identity(r,c):
	a=[[0 for col in range(c)] for row in range(r)]
	for i in range(r):
		for j in range(c):
			if i==j:
				a[i][j]=1

	return a

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
	global list,n
	T=set_identity(3,3)
	T[2][0]=tx
	T[2][1]=ty
	for i in range(n):
		x=list[i][0]
		y=list[i][1]
		X=[[x,y,1]]
		X=matrix_mul(X,T)
		list[i][0]=X[0][0]
		list[i][1]=X[0][1]

def scale(sx,sy,xr,yr):
	global list,n
	translate(-xr,-yr)
	T=set_identity(3,3)
	T[0][0]=sx
	T[1][1]=sy
	for i in range(n):
		x=list[i][0]
		y=list[i][1]
		X=[[x,y,1]]
		X=matrix_mul(X,T)
		list[i][0]=X[0][0]
		list[i][1]=X[0][1]
	translate(xr,yr)

def rotate(theta,xr,yr):
	global list,n
	translate(-xr,-yr)
	T=set_identity(3,3)
	T[0][0]=cos(theta)
	T[0][1]=-sin(theta)
	T[1][0]=sin(theta)
	T[1][1]=cos(theta)
	for i in range(n):
		x=list[i][0]
		y=list[i][1]
		X=[[x,y,1]]
		X=matrix_mul(X,T)
		list[i][0]=X[0][0]
		list[i][1]=X[0][1]
	translate(xr,yr)
	
def myInit():
	global n,x,y,width,spacing,top_margin,right_margin,maximum
	glClearColor(0.0,1.0,1.0,0.0)
	glColor3f(1.0,0.0,0.0)
	glPointSize(2.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(-x,x,-y,y)

def readInput():
	global n,list
	n= int(raw_input('Enter number of sides:'))
	for i in range(n):
			print 'enter coordinate',i+1,' (x,y):'
			x,y= map(int,raw_input().split())
			list.append([x,y])

def polygon():
	global n,list
	glClear(GL_COLOR_BUFFER_BIT)
	#draw x axis
	line(-x,0,x,0)
	#draw y axis
	line(0,-y,0,y)
	for i in range(n):
		line(list[i][0],list[i][1],list[(i+1)%n][0],list[(i+1)%n][1])

def Display():
	
		glClear(GL_COLOR_BUFFER_BIT)



		polygon()

		cont='y'

		while 1:
			print '1.Translate\n2.Scale\n3.Rotate'
			print 'Enter choice:'
			choice=int(raw_input())

			if choice==1:
				print 'Enter tx,ty:'
				tx,ty=map(float,raw_input().split())
				translate(tx,ty)
			elif choice==2:
				print 'Enter sx,sy:'
				sx,sy=map(float,raw_input().split())
				print 'Enter reference point:'
				xr,yr=map(int,raw_input().split())
				scale(sx,sy,xr,yr)
			elif choice==3:
				theta=float(raw_input('Enter angle (degrees):'))
				print 'Enter reference point:'
				xr,yr=map(int,raw_input().split())
				theta=(theta*pi)/180
				rotate(theta,xr,yr)
			else:
				print 'invalid choice!'

			polygon()
			print 'Do you want to continue (y/n)?'
			cont=raw_input()
			if cont=='n' or cont=='N':
				sys.exit()

def main():
	global n,x,y
	readInput()
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(2*x,2*y)
	glutInitWindowPosition(50,50)
	glutCreateWindow("DDA Line Algorithm")
	glutDisplayFunc(Display)
	myInit()
	glutMainLoop()
main()