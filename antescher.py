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
viewDir = NORTH_EAST

offsets= (
    (1, 0),     # E
    (0, 1),     # S
    (-1, 0),    # W
    (0, -1)     # N
)

def Floor():
    glBegin(GL_QUADS)
    glColor(1, 1, 1)
    glVertex3i(0, 0, 0)
    glVertex3i(0, 0, 128 * 16)
    glVertex3i(128 * 16, 0, 128 * 16)
    glVertex3i(128 * 16, 0, 0)
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
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

#    glTranslatef(0.0, 0.0, -5)
    dist = 800
    height = dist
    viewDir = NORTH_EAST
    position = [34, 78]
    angle = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            pressed = pygame.key.get_pressed()
            # q to quit
            if pressed[pygame.K_q]:
                pygame.quit()
                quit()
            # change view direction with O and P
            if pressed[pygame.K_o]:
                viewDir = (viewDir + 1) % 4
            if pressed[pygame.K_p]:
                viewDir = (viewDir + 5) % 4
            # absolute movement using keypad
            if pressed[pygame.K_KP9]:   # E
                position[0] += offsets[viewDir][0]
                position[1] += offsets[viewDir][1]
            if pressed[pygame.K_KP3]:   # S
                position[0] += offsets[(viewDir + 1) % 4][0]
                position[1] += offsets[(viewDir + 1) % 4][1]
            if pressed[pygame.K_KP1]:   # W
                position[0] += offsets[(viewDir + 2) % 4][0]
                position[1] += offsets[(viewDir + 2) % 4][1]
            if pressed[pygame.K_KP7]:   # N
                position[0] += offsets[(viewDir + 3) % 4][0]
                position[1] += offsets[(viewDir + 3) % 4][1]
            print(position)

        #glRotatef(1, 3, 1, 1)
        angle = (viewDir + 1.5) * math.pi / 2;
        glLoadIdentity();
        gluPerspective(5, (display[0]/display[1]), 0.1, 1500.0)
        #glTranslatef(400, 300, 0); # centre screen
        gluLookAt(position[0] * 16 + (dist * math.cos(angle)), height, position[1] * 16 + (dist * math.sin(angle)),
            position[0] * 16, 0, position[1] * 16,
            0, 1, 0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK)
        Floor()
        Axes()
        DrawMap()
        pygame.display.flip()
        pygame.time.wait(10)

main()
