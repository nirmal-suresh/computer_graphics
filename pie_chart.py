from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from bressenham_circle import circle
from bressenham_to_import import line
from math import sin,cos,pi

coordinates=[]
n=0
def myInit():

    glClearColor(0.0,1.0,1.0,0.0)
    glColor3f(1.0,0.0,0.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-300,300,-300,300)

def setPixel(xcoordinate,ycoordinate):

    glBegin(GL_POINTS)
    glVertex2i(xcoordinate,ycoordinate)
    glEnd()
    glFlush()

def Display():
        global n
        glClear(GL_COLOR_BUFFER_BIT)
        circle(0,0,200)
        line(0,0,200,0)
        print coordinates
        for i in range(n-1):
            line(0,0,coordinates[i][0],coordinates[i][1])
        

def main():
    theta=0
    names=[]
    values=[]
    global n
    n= int(input('Enter number of values:'))
    for i in range(n):
        print 'Enter name and value:'
        name,value=raw_input().split()
        value=int(value)
        names.append(name)
        values.append(value)

    total=sum(values)
    for i in range(n):
        values[i]=(values[i]/float(total))*(2*pi)

    for i in range(n-1):
        theta=theta+values[i]
        coordinates.append((200*cos(theta),200*sin(theta)))    


    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600,600)
    glutInitWindowPosition(50,50)
    glutCreateWindow("DDA Line Algorithm")
    glutDisplayFunc(Display)
    
    myInit()
    glutMainLoop()
main()