# Antescher
# Omnifone hackathon 20160718

__author__ = "adean"
__date__ = "$18-Jul-2016 10:11:12$"

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import math

from antmap import AntMap

antMap = AntMap()
antMap.read_map()

# directions
NORTH_EAST = 0
SOUTH_EAST = 1
SOUTH_WEST = 2
NORTH_WEST = 3
direction = NORTH_EAST

vertices= (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )
    

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

def Floor():
    glBegin(GL_QUADS)
    glColor(1, 1, 1)
    glVertex3i(0, 0, 0)
    glVertex3i(0, 0, 128 * 16)
    glVertex3i(128 * 16, 0, 128 * 16)
    glVertex3i(128 * 16, 0, 0)
    glEnd()

def Cube():
    glColor(1, 1, 1)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def Axes():
    # axes
    glPushMatrix()
    glTranslate(64 * 16, 0, 64 * 16)
    glBegin(GL_LINES)
    glColor(255, 0, 0)
    glVertex3i(-1000, 0, 0)
    glColor(255, 255, 0)
    glVertex3i(1000, 0, 0)
    glColor(0, 255, 0)
    glVertex3i(0, -1000, 0)
    glColor(0, 255, 255)
    glVertex3i(0, 1000, 0)
    glColor(0, 0, 255)
    glVertex3i(0, 0, -1000)
    glColor(255, 0, 255)
    glVertex3i(0, 0, 1000)
    glEnd()
    glPopMatrix()

def DrawMap():
    #print("drawMap")
    antMap.draw()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

#    glTranslatef(0.0, 0.0, -5)
    dist = 1000
    height = dist
    direction = NORTH_EAST
    position = [0, 0]
    angle = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # change viewpoint with O and P
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_o]:
                direction = (direction + 1) % 4
            if pressed[pygame.K_p]:
                direction = (direction + 5) % 4

        #glRotatef(1, 3, 1, 1)
        angle = (direction + .5) * math.pi / 2;
        glLoadIdentity();
        gluPerspective(10, (display[0]/display[1]), 0.1, 2500.0)
        gluLookAt(position[0] * 16 + (dist * math.cos(angle)), height, position[1] * 16 + (dist * math.sin(angle)),
            position[0] * 16, 0, position[1] * 16,
            0, 1, 0)

        position[1] += 1

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK)
        Floor()
        Cube()
        Axes()
        DrawMap()
        pygame.display.flip()
        pygame.time.wait(10)

main()