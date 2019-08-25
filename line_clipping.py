from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from symmetric_dda import line

def myInit(Xl,Xr,Yb,Yt):

	glClearColor(0.0,1.0,1.0,0.0)
	glColor3f(1.0,0.0,0.0)
	glPointSize(2.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()	
	gluOrtho2D(Xl,Xr,Yb,Yt)

	return Xl,Xr,Yb,Yt

def readInput():
	print 'coordinates (x1 y1 x2 y2):'
	x1,y1,x2,y2 = map(int,raw_input().split())

	return x1,y1,x2,y2


def Endpoint(P,Window):
	Pcode=[]
	code = 1 if P[0]<Window[0] else 0
	Pcode.insert(0,code) 
	code = 1 if P[0]<Window[1] else 0
	Pcode.insert(0,code) 
	code = 1 if P[1]<Window[2] else 0
	Pcode.insert(0,code) 
	code = 1 if P[1]<Window[3] else 0
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

def Cohen_Sutherland(P1x,P1y,P2x,P2y,Xl,Xr,Yb,Yt):
	P1=[P1x,P1y]
	P2=[P2x,P2y]
	Window=[Xl,Xr,Yb,Yt]
	P1code=Endpoint(P1,Window)
	P2code=Endpoint(P2,Window)
	Vflag=Visible(P1code,P2code)
	if Vflag=='yes':
		#draw line
		glutDisplayFunc(Display(P1x,P1y,P2x,P2y))
	elif Vflag=='no':
		#exit without drawing line
		return
	Iflag=1
	if P2x==P1x:
		Iflag=-1

	elif P2y==P1y:
		Iflag=0
	else:
		Slope=(P2y-P1y)/(P2x-P1x)

	while Vflag=='partial':
		for i in range(0,4):
			if P1code[3-i]!=P2code[3-i]:
				if P1code[3-i]==0:
					Temp=P1code
					P1=P2
					P2=Temp
					Tempcode=P1code
					P1code=P2code
					P2code=Tempcode

				if Iflag!=-1 and i<=1:
					P1y=Slope*(Window[i]-P1x)+P1y
					P1x=Window[i]
					P1code=Endpoint(P1code,Window)
				if Iflag!=0 and i<=1:
					if Iflag!=1:
						P1x=(1/Slope)*(Window[i]-P1y)+P1x
					P1y=Window[i]
					P1code=Endpoint(P1,Window)

				Vflag=Visible(P1code,P2code)
				if Vflag=='yes':
					#draw line
					glutDisplayFunc(Display(P1x,P1y,P2x,P2y))
				elif Vflag=='no':
					#exit without drawing line
					return

def Display():
	glClear(GL_COLOR_BUFFER_BIT)
	line(100,100,200,200)

def main():
	
	x1,y1,x2,y2=readInput()
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(600,600)
	glutInitWindowPosition(50,50)
	glutCreateWindow("DDA Line Algorithm")
	Xl=0.0
	Xr=640.0
	Yb=0.0
	Yt=480.0
	#Cohen_Sutherland(x1,y1,x2,y2,Xl,Xr,Yb,Yt)
	print 'flag'
	glutDisplayFunc(Display)
	print 'flag 2'
	myInit(Xl,Xr,Yb,Yt)
	glutMainLoop()
main()
