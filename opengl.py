# pip install PyOpenGL PyOpenGL_accelerate
# pip install pygame
# pip install numpy

import pygame
import numpy as np

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

verticies = ((1, -1, 0), (1, 1, 0), (-1, 1, 0),(-1, -1, 0))

edges = ((0, 1), (0,3), (2,1), (2,3))

def Quadrado(p, l):
    glBegin(GL_QUADS)
    for edge in edges:
        for vertex in edge:
            v = (np.array(verticies[vertex]) * l)  + np.array(p)
            glVertex3fv(v)
    glEnd()

def desenho():
    horiz = 1.8
    verti = 2.5
    tamanhoDeLado = 0.2
    for i in range(-17, 18, 5):
        i = i/10
        Quadrado((-verti, i, 0), tamanhoDeLado)
        Quadrado((verti, i, 0), tamanhoDeLado)
    for i in range(-25, 26, 5):
        i = i/10
        Quadrado((i, horiz, 0), tamanhoDeLado)
        Quadrado((i, -horiz+0.1, 0), tamanhoDeLado)



def main():
    pygame.init()   
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        desenho()

        pygame.display.flip()
        pygame.time.wait(10)

main()
