from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from dda_to_import import lineDDA

def myInit(Xl,Xr,Yb,Yt):

	glClearColor(0.0,1.0,1.0,0.0)
	glColor3f(1.0,0.0,0.0)
	glPointSize(2.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()	
	gluOrtho2D(Xl,Xr,Yb,Yt)

	return Xl,Xr,Yb,Yt

def readInput():
	global P1x,P1y,P2x,P2y
	print 'coordinates (x1 y1 x2 y2):'
	P1x,P1y,P2x,P2y = map(int,raw_input().split())

def Endpoint(x,y,Window):
	Pcode=[]
	print 'endpoint,','x1=',x,'y1=',y
	code = 1 if x<Window[0] else 0
	Pcode.insert(0,code) 
	code = 1 if x>Window[1] else 0
	Pcode.insert(0,code) 
	code = 1 if y<Window[2] else 0
	Pcode.insert(0,code) 
	code = 1 if y>Window[3] else 0
	Pcode.insert(0,code) 

	return Pcode

def Visible(P1code,P2code):
	Vflag='yes'
	print P1code
	print P2code

	for i in range(0,4):
		if P1code[i] and P2code[i]:
			Vflag='no'
			break

	for i in range(0,4):
		if P1code[i] or P2code[i]:
			Vflag='partial'

	return Vflag

def Cohen_Sutherland(Xl,Xr,Yb,Yt):
	global P1x,P1y,P2x,P2y
	
	Window=[Xl,Xr,Yb,Yt]
	P1code=Endpoint(P1x,P1y,Window)
	P2code=Endpoint(P2x,P2y,Window)
	Vflag=Visible(P1code,P2code)
	print Vflag
	if Vflag=='yes':
		return 'yes'

	elif Vflag=='no':
		#exit without drawing line
		return 'no'
	Iflag=1
	if P2x==P1x:
		Iflag=-1

	elif P2y==P1y:
		Iflag=0
	else:
		Slope=(P2y-P1y)/float(P2x-P1x)
		print Slope


	print 'before while'
	while Vflag=='partial':
		for i in range(0,4):
			if P1code[3-i]!=P2code[3-i]:
				print 'inside if'
				if P1code[3-i]==0:
					print 'swap'
					P1x,P1y=P2x,P2y
					P1code,P2code=P2code,P1code

				if Iflag!=-1 and i<=1:
					print 'modified'
					P1y=Slope*(Window[i]-P1x)+P1y
					P1x=Window[i]
					print 'x1=',P1x,'y1=',P1y
					P1code=Endpoint(P1x,P1y,Window)
				if Iflag!=0 and i<=1:
					if Iflag!=1:
						print 'modified'
						P1x=(1/Slope)*(Window[i]-P1y)+P1x
					P1y=Window[i]
					print 'x1=',P1x,'y1=',P1y
					P1code=Endpoint(P1x,P1y,Window)

				Vflag=Visible(P1code,P2code)
				if Vflag=='yes':
					return 'yes'
				elif Vflag=='no':
					#exit without drawing line
					return 'no'

def Display():
	print 'flag0'
	print 'x1=',P1x,'y1=',P1y,'x2=',P2x,'y2=',P2y
	print 'flag1'
	glClear(GL_COLOR_BUFFER_BIT)
	lineDDA(P1x,P1y,P2x,P2y)

def main():
	
	readInput()
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(600,600)
	glutInitWindowPosition(50,50)
	glutCreateWindow("DDA Line Algorithm")
	Xl=100
	Xr=400
	Yb=100
	Yt=300
	
	code=Cohen_Sutherland(Xl,Xr,Yb,Yt)
	if code=='yes':
		glutDisplayFunc(Display)
	
	myInit(0.0,640.0,0.0,480.0)
	glutMainLoop()
main()
