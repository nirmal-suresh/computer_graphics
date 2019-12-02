from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from bressenham_to_import import line
list=[]
x=40
y=40
width=35
spacing=20
top_margin=40
right_margin=40
def myInit():
    global n,x,y,width,spacing,top_margin,right_margin,maximum
    glClearColor(0.0,1.0,1.0,0.0)
    glColor3f(1.0,0.0,0.0)
    glPointSize(2.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0,x+n*(width+spacing)+right_margin+50,0.0,x+maximum+50+top_margin)

def readInput():
    global n,list
    n= int(input('Enter number of values:'))
    for i in range(n):
            print 'enter value',i+1,': '
            value=int(raw_input())
            list.append(value)

    return max(list)

def setPixel(xcoordinate,ycoordinate):

    glBegin(GL_POINTS)
    glVertex2i(xcoordinate,ycoordinate)
    glEnd()
    glFlush()

def Display():
        
        global n,list,x,y,width,spacing,top_margin,right_margin

        glClear(GL_COLOR_BUFFER_BIT)
        #draw x axis
        line(x,y,x+n*(width+spacing)+50,y)
        #draw y axis
        line(x,y,x,x+maximum+50)
        #xof is the x offset
        xof=x

        for i in range(n):
            xof=xof+spacing
            
            #draw the bar
            line(xof,y,xof,list[i]+y)
            line(xof,list[i]+y,xof+width,list[i]+y)
            line(xof+width,list[i]+y,xof+width,y)

            xof=xof+width


def main():
    global n,x,y,width,spacing,top_margin,right_margin,maximum
    maximum=readInput()
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(x+n*(width+spacing)+right_margin+50,x+maximum+50+top_margin)
    glutInitWindowPosition(50,50)
    glutCreateWindow("DDA Line Algorithm")
    glutDisplayFunc(Display)
    myInit()
    glutMainLoop()
main()