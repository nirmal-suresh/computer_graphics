from OpenGL.GL import * 
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from math import pow

def my_init():
    glClearColor(0.0,0.0,0.0,0.0)
    gluOrtho2D(-300,300,-300,300)
    
def setPixel(x,y):
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()
    glFlush()
    
def circle(xc,yc,r):
    x1=r
    y1=0
    sx=x1
    sy=y1
    i=0
    val=0
    while val<r:
        val=pow(2,i)
        i+=1
    e=1/pow(2,i-1)
    
    x2=x1+(y1*e)
    y2=y1-(x2*e)
    setPixel(xc+x2,yc+y2)
    x1=x2
    y1=y2
    
    while (y1-sy)<e or (sx-x1)>e:
        x2=x1+(y1*e)
        y2=y1-(x2*e)
        setPixel(xc+x2,yc+y2)
        x1=x2
        y1=y2
    
def input():
    global xc,yc,r
    xc,yc=map(int,raw_input('Enter center of circle (xc yc):').split())
    r=int(raw_input('Enter radius:'))        
    
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    global xc,yc,r
    circle(xc,yc,r)
    
def main():
    input()
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(100,100)
    glutInitWindowSize(600,600)
    glutCreateWindow('dda circle')
    
    my_init()
    glutDisplayFunc(display)
    glutMainLoop()
    
main()    
