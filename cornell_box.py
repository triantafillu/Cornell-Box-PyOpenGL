from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np

#Draw filled cirle (made for ceiling, that's why only coordinates x and z are changing)
def draw_circle(cx, cy, cz, r):
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(cx, cy, cz)
    for i in range (0, 500):
        glVertex3f((cx + (r * np.cos(i * np.pi*2 / 500))), cy , (cz + (r * np.sin(i * np.pi *2/ 500))))
    glEnd()

#Draw lamp of circle shape
def drawlamp():
    glColor3f(1,1,1)
    glNormal3f(0, -1, 0)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [1,1,1,1])
    draw_circle(0, 99.99, -400, 20)
    glDisable(GL_LIGHT0)

#Set 4 sources of light near lamp to make illusion of lighting from lamp
def lighting():
    pos0 = [-15, 99.9,-400, 1]
    pos1 = [15, 99.9, -400, 1]
    pos2 = [0, 99.9, -390, 1]
    pos3 = [0, 99.9, -410, 1]

    glShadeModel(GL_SMOOTH)
    glEnable(GL_LIGHTING)
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0,0,0,1])
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)
    glEnable(GL_LIGHT2)
    glEnable(GL_LIGHT3)

    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.1, 0.1, 0.1, 0])
    glLightfv(GL_LIGHT1, GL_AMBIENT, [0.1, 0.1, 0.1, 0])
    glLightfv(GL_LIGHT2, GL_AMBIENT, [0.1, 0.1, 0.1, 0])
    glLightfv(GL_LIGHT3, GL_AMBIENT, [0.1, 0.1, 0.1, 0])

    glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.4, 0.4, 0.4, 1])
    glLightfv(GL_LIGHT1, GL_DIFFUSE, [0.4, 0.4, 0.4, 1])
    glLightfv(GL_LIGHT2, GL_DIFFUSE, [0.4, 0.4, 0.4, 1])
    glLightfv(GL_LIGHT3, GL_DIFFUSE, [0.4, 0.4, 0.4, 1])

    glLightfv(GL_LIGHT0, GL_POSITION, pos0)
    glLightfv(GL_LIGHT1, GL_POSITION, pos1)
    glLightfv(GL_LIGHT2, GL_POSITION, pos2)
    glLightfv(GL_LIGHT3, GL_POSITION, pos3)

    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.001)
    glLightf(GL_LIGHT1, GL_LINEAR_ATTENUATION, 0.001)
    glLightf(GL_LIGHT2, GL_LINEAR_ATTENUATION, 0.001)
    glLightf(GL_LIGHT3, GL_LINEAR_ATTENUATION, 0.001)

    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

#Draws walls by dividing quads to get smoother shadows
def draw_box():
    glClear(GL_DEPTH_BUFFER_BIT | GL_COLOR_BUFFER_BIT)

    #Draw lamp on the ceiling
    drawlamp()

    #Down
    glBegin(GL_QUADS)
    glColor3f(112/255, 149/255, 225/255)
    glNormal3f(0,1,0)
    for i in range (0,300):
        for j in range (0,300):
            glVertex3f(-100 + j,       -100,    -300 - i)
            glVertex3f(-100 + j + 1,   -100,    -300 - i)
            glVertex3f(-100 + j + 1,   -100,    -300 - i - 1)
            glVertex3f(-100 + j,       -100,    -300 - i - 1)
    glEnd()

    #Left
    glColor3f(81/255, 192/255, 191/255)
    glBegin(GL_QUADS)
    glNormal3f(1, 0, 0)
    for i in range(0,300):
        for j in range (0,300):
            glVertex3f(-100,   -100+i,        -300-j)
            glVertex3f(-100,   -100+i,        -300 - j-1)
            glVertex3f(-100,   -100 + i+1,    -300 - j-1)
            glVertex3f(-100,   -100 + i+1,    -300-j)
    glEnd()

    #Right
    glColor3f(249/255, 205/255, 151/255)
    glBegin(GL_QUADS)
    glNormal3f(-1, 0, 0)
    for i in range(0,300):
        for j in range (0,300):
            glVertex3f(100,   -100+j,      -300-i)
            glVertex3f(100,   -100 + j+1,  -300-i)
            glVertex3f(100,   -100 + j+1,  -300 - i-1)
            glVertex3f(100,   -100+j,      -300 - i-1)
    glEnd()

    #Back
    glColor3f(201 / 255, 147 / 255, 212 / 255)
    glBegin(GL_QUADS)
    glNormal3f(0, 0, 1)
    for i in range(0,300):
        for j in range (0,300):
            glVertex3f(-100,       -100,      -500)
            glVertex3f(-100 + j,   -100,      -500)
            glVertex3f(-100 + j,   -100 + i,  -500)
            glVertex3f(-100,       -100 + i,  -500)
    glEnd()

    #Up
    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glNormal3f(0, -1, 0)
    for i in range(0,300):
        for j in range (0,300):
            glVertex3f(-100+i,       100,  -300-j)
            glVertex3f(-100+i,       100,  -300 - j-1)
            glVertex3f(-100 + i+1,   100,  -300 - j-1)
            glVertex3f(-100 + i+1,   100,  -300-j)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glClearColor(0,0.6,0,0)

    #Install lightning
    lighting()

    #Draw scene
    draw_box()

    #Glass Cone
    glPushMatrix()
    glTranslatef(50,-28.5,-350)
    glRotatef(270,1, 0, 0)
    glColor4f(141/255, 182/255, 199/255, 0.8)
    glutSolidCone(20, 30, 20, 20)
    glPopMatrix()

    #Cube
    glPushMatrix()
    glTranslatef(50,-80,-350)
    glRotatef(10,0, 1, 0)
    glColor3f(0/ 255, 197 / 255, 144 / 255)
    glutSolidCube(50)
    glPopMatrix()

    #Sphere
    glPushMatrix()
    glTranslatef(50, -50, -350)
    glRotatef(10, 0, 1, 0)
    glColor3f(154/ 255, 147 / 255, 236/ 255)
    glutSolidSphere(20,20,20)
    glPopMatrix()

    #Torus
    glPushMatrix()
    glTranslatef(-75,-65,-400)
    glRotatef(85, 0, 1, 0)
    glRotatef(30, -1, 0, 0)
    glColor3f(255/255, 134/255, 66/225)
    glutSolidTorus(10, 30, 40, 40)
    glPopMatrix()

    glFlush()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-100, 100, -100, 100, 300, 600)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)

    #Set window size and position
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Cornell Box")

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)

    #Nedeed for "glass" cone
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glutMainLoop()

main()