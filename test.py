from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from bressenham_circle import circle


def myInit():

    glClearColor(0.0,1.0,1.0,0.0)
    glColor3f(1.0,0.0,0.0)
    glPointSize(2.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0,600.0,0.0,600.0)

def setPixel(xcoordinate,ycoordinate):

    glBegin(GL_POINTS)
    glVertex2i(xcoordinate,ycoordinate)
    glEnd()
    glFlush()

def Display():
    
        glClear(GL_COLOR_BUFFER_BIT)
        setPixel(100,100)
        print '100,100'
        color=glReadPixels(100,100,1,1,GL_RGB,GL_FLOAT)
        print color
        print '200,200'
        color=glReadPixels(200,200,1,1,GL_RGB,GL_FLOAT)
        print color
        print color[0][0][0]
        print color[0][0][1]
        print color[0][0][2]
        


def main():
    
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600,600)
    glutInitWindowPosition(50,50)
    glutCreateWindow("DDA Line Algorithm")
    glutDisplayFunc(Display)
    
    myInit()
    glutMainLoop()
main()
