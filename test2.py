from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from bressenham_circle import circle


def myInit():

    glClearColor(0.0,1.0,1.0,0.0)
    glColor3f(1.0,0.0,0.0)
    glPointSize(10.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0,600,0,600)

def setPixel(xcoordinate,ycoordinate):

    glBegin(GL_POINTS)
    glVertex2i(xcoordinate,ycoordinate)
    glEnd()
    glFlush()

def onMouseClick(button,state,x,y):
    y=600-y
    print x,y
    color=glReadPixels(x,y,1,1,GL_RGB,GL_FLOAT)
    print color

    read()

def Display():
    
        glClear(GL_COLOR_BUFFER_BIT)
        setPixel(0,0)
        setPixel(100,100)
        setPixel(600,600)

def read():
    print 'read'
    color=glReadPixels(0,0,1,1,GL_RGB,GL_FLOAT)
    print color
    color=glReadPixels(100,100,1,1,GL_RGB,GL_FLOAT)
    print color
    color=glReadPixels(600,600,1,1,GL_RGB,GL_FLOAT)
    print color

def main():
    
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600,600)
    glutInitWindowPosition(50,50)
    glutCreateWindow("DDA Line Algorithm")
    glutDisplayFunc(Display)
    glutMouseFunc(onMouseClick)
    
    myInit()
    glutMainLoop()
main()
