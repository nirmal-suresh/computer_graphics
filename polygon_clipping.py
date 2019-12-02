from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from bressenham_to_import import line
list=[]

def myInit():

    glClearColor(0.0,1.0,1.0,0.0)
    glColor3f(1.0,0.0,0.0)
    glPointSize(2.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0,600.0,0.0,600.0)

def readInput():
	global n,Xl,Xr,Yb,Yt
	n= int(input('Enter number of sides:'))
	for i in range(n):
			print 'enter coordinate',i+1,' (x,y):'
			x,y= map(int,raw_input().split())
			list.append((x,y))
	print 'Clipping Window limits (Xl,Xr,Yb,Yt):'
	Xl,Xr,Yb,Yt = map(int,raw_input().split())
			
	

def Display():
    
        glClear(GL_COLOR_BUFFER_BIT)
        #draw clipping window
        global list
        line(Xl,Yb,Xl,Yt)
        line(Xl,Yt,Xr,Yt)
        line(Xr,Yt,Xr,Yb)
        line(Xr,Yb,Xl,Yb)
        for i in range(len(list)-1):
        	x1=list[i][0]
        	y1=list[i][1]
        	x2=list[i+1][0]
        	y2=list[i+1][1]
        	line(x1,y1,x2,y2)
        x1=list[i+1][0]
        y1=list[i+1][1]
        x2=list[0][0]
        y2=list[0][1]
        line(x1,y1,x2,y2)
        
def left_clipping(list1):
	global Xl
	list2=[]
	yn=0
	for i in range(len(list1)):
		
		x1=list1[i][0]
		y1=list1[i][1]
		if i==len(list1)-1:
			x2=list1[0][0]
			y2=list1[0][1]
		else:
			x2=list1[i+1][0]
			y2=list1[i+1][1]
		dy=y2-y1
		dx=x2-x1
		if dx!=0:
			m=dy/float(dx)
		#out to in
		if(x1<Xl and x2>Xl):
			yn=m*(Xl-x1)+y1
			list2.append((Xl,yn))
			list2.append((x2,y2))
		#in to in
		elif(x1>Xl and x2>Xl):
			list2.append((x2,y2))
		#in to out
		elif(x1>Xl and x2<Xl):
			yn=m*(Xl-x1)+y1
			list2.append((Xl,yn))
	return list2
	
def right_clipping(list1):
	global Xr
	list2=[]
	yn=0
	for i in range(len(list1)):
		x1=list1[i][0]
		y1=list1[i][1]
		if i==len(list1)-1:
			x2=list1[0][0]
			y2=list1[0][1]
		else:
			x2=list1[i+1][0]
			y2=list1[i+1][1]
		dy=y2-y1
		dx=x2-x1
		if dx!=0:
			m=dy/float(dx)
		#out to in
		if(x1>Xr and x2<Xr):
			yn=m*(Xr-x1)+y1
			list2.append((Xr,yn))
			list2.append((x2,y2))
		#in to in
		elif(x1<Xr and x2<Xr):
			list2.append((x2,y2))
		#in to out
		elif(x1<Xr and x2>Xr):
			yn=m*(Xr-x1)+y1
			list2.append((Xr,yn))
	return list2
	
def top_clipping(list1):
	global Yt
	list2=[]
	xn=0
	for i in range(len(list1)):
		x1=list1[i][0]
		y1=list1[i][1]
		if i==len(list1)-1:
			x2=list1[0][0]
			y2=list1[0][1]
		else:
			x2=list1[i+1][0]
			y2=list1[i+1][1]
		dy=y2-y1
		dx=x2-x1
		if dx!=0:
			m=dy/float(dx)
		#out to in
		if(y1>Yt and y2<Yt):
			if dx==0:
				xn=x1
			else:
				xn=(1/m)*(Yt-y1)+x1
			list2.append((xn,Yt))
			list2.append((x2,y2))
		#in to in
		elif(y1<Yt and y2<Yt):
			list2.append((x2,y2))
		#in to out
		elif(y1<Yt and y2>Yt):
			if dx==0:
				xn=x1
			else:
				xn=(1/m)*(Yt-y1)+x1
			list2.append((xn,Yt))
	return list2
	
def bottom_clipping(list1):
	global Yb
	list2=[]
	xn=0
	for i in range(len(list1)):
		
		x1=list1[i][0]
		y1=list1[i][1]
		if i==len(list1)-1:
			x2=list1[0][0]
			y2=list1[0][1]
		else:
			x2=list1[i+1][0]
			y2=list1[i+1][1]
		dy=y2-y1
		dx=x2-x1
		if dx!=0:
			m=dy/float(dx)
		#out to in
		if(y1<Yb and y2>Yb):
			if dx==0:
				xn=x1
			else:
				xn=(1/m)*(Yb-y1)+x1
			list2.append((xn,Yb))
			list2.append((x2,y2))
		#in to in
		elif(y1>Yb and y2>Yb):
			list2.append((x2,y2))
		#in to out
		elif(y1>Yb and y2<Yb):
			if dx==0:
				xn=x1
			elif m==0:
				print x1,y1,x2,y2
			else:
				xn=(1/m)*(Yb-y1)+x1
			list2.append((xn,Yb))
	return list2
						        
def polygon_clipping():
	global list,n
	list1=left_clipping(list)
	print 'after left clipping: ',list1,len(list1)
	list1=right_clipping(list1)
	print 'after right clipping: ',list1,len(list1)
	list1=top_clipping(list1)
	print 'after top clipping: ',list1,len(list1)
	list=bottom_clipping(list1)
	print 'after bottom clipping: ',list,len(list)
	
        
def main():
    
    readInput()
    polygon_clipping()
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600,600)
    glutInitWindowPosition(50,50)
    glutCreateWindow("DDA Line Algorithm")
    glutDisplayFunc(Display)
    myInit()
    glutMainLoop()
main()
