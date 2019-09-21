from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from dda_to_import import lineDDA

def myInit():

	glClearColor(0.0,1.0,1.0,0.0)
	glColor3f(1.0,0.0,0.0)
	glPointSize(2.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()	
	gluOrtho2D(0,600,0,600)

def readInput():
	global P1x,P1y,P2x,P2y
	global Xl,Xr,Yb,Yt
	print 'coordinates (x1 y1 x2 y2):'
	P1x,P1y,P2x,P2y = map(int,raw_input().split())
	print 'Clipping Window limits (Xl,Xr,Yb,Yt):'
	Xl,Xr,Yb,Yt = map(int,raw_input().split())

def Endpoint(x,y,Window):
	Pcode=[]
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

	while Vflag=='partial':
		for i in range(0,4):
			if P1code[3-i]!=P2code[3-i]:
				if P1code[3-i]==0:
					P1x,P2x=P2x,P1x
					P1y,P2y=P2y,P1y
					P1code,P2code=P2code,P1code

				if Iflag!=-1 and i<=1:
					P1y=Slope*(Window[i]-P1x)+P1y
					P1x=Window[i]
					P1code=Endpoint(P1x,P1y,Window)
				if Iflag!=0 and i>1:
					if Iflag!=1:
						P1x=(1/Slope)*(Window[i]-P1y)+P1x
					P1y=Window[i]
					P1code=Endpoint(P1x,P1y,Window)

				Vflag=Visible(P1code,P2code)
				if Vflag=='yes':
					return 'yes'
				elif Vflag=='no':
					#exit without drawing line
					return 'no'

def Display():
	glClear(GL_COLOR_BUFFER_BIT)
	#draw clipping window
	print 'Display function called'
	lineDDA(Xl,Yb,Xr,Yb)
	lineDDA(Xr,Yb,Xr,Yt)
	lineDDA(Xr,Yt,Xl,Yt)
	lineDDA(Xl,Yt,Xl,Yb)
	if code=='yes':
		#draw clipped line
		lineDDA(P1x,P1y,P2x,P2y)

def main():
	
	readInput()
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(600,600)
	glutInitWindowPosition(50,50)
	glutCreateWindow("Cohen-Sutherland line clipping")
	glutDisplayFunc(Display)
	global code

	code=Cohen_Sutherland(Xl,Xr,Yb,Yt)
	print 'called cohen sutherland'
	glutDisplayFunc(Display)

	myInit()
	glutMainLoop()
main()
