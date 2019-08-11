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
    gluOrtho2D(0.0,640.0,0.0,480.0)

def readInput():
    global x1,y1,x2,y2
    print 'coordinates (x1 y1 x2 y2):'
    x1,y1,x2,y2 = map(int,raw_input().split())

def Display():
    
        glClear(GL_COLOR_BUFFER_BIT)
        lineDDA(x1,y1,x2,y2)


def main():
    
    readInput()
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600,600)
    glutInitWindowPosition(50,50)
    glutCreateWindow("DDA Line Algorithm")
    glutDisplayFunc(Display)
    myInit()
    glutMainLoop()
main()