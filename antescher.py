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

BLOCK_SIZE = 6

antMap = AntMap(BLOCK_SIZE)
antMap.read_map()

from displayList import DisplayList

displayLists = DisplayList()

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
    glColor(.9, .9, .9)
    glVertex3i(0, 0, 0)
    glVertex3i(0, 0, AntMap.MAP_SIZE * BLOCK_SIZE)
    glVertex3i(AntMap.MAP_SIZE * BLOCK_SIZE, 0, AntMap.MAP_SIZE * BLOCK_SIZE)
    glVertex3i(AntMap.MAP_SIZE * BLOCK_SIZE, 0, 0)
    glEnd()

def Axes():
    # axes (x and z are raised slightly to get them up off the floor)
    glPushMatrix()
    glTranslate((AntMap.MAP_SIZE / 2) * BLOCK_SIZE, 0, (AntMap.MAP_SIZE / 2) * BLOCK_SIZE)
    glBegin(GL_LINES)
    # x
    glColor(255, 0, 0)
    glVertex3i(-1000, 2, 0)
    glColor(255, 255, 0)
    glVertex3i(1000, 2, 0)
    # y
    glColor(0, 255, 0)
    glVertex3i(0, 2, 0)
    glColor(0, 255, 255)
    glVertex3i(0, 1000, 0)
    # z
    glColor(0, 0, 255)
    glVertex3i(0, 2, -1000)
    glColor(255, 0, 255)
    glVertex3i(0, 2, 1000)
    glEnd()
    glPopMatrix()

def DrawMap():
    #print("drawMap")
    antMap.draw()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    displayLists.generate(BLOCK_SIZE)

#    glTranslatef(0.0, 0.0, -5)
    dist = 800
    height = dist
    viewDir = NORTH_EAST
    position = [64, 129] # gate?
    angle = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            pressed = pygame.key.get_pressed()
            # q to quit
            if pressed[pygame.K_q] or pressed[pygame.K_ESCAPE]:
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
            #print("Position: ", position)

        #glRotatef(1, 3, 1, 1)
        angle = (viewDir + 1.5) * math.pi / 2;
        glLoadIdentity()
        #print("display: ",  display)
        gluPerspective(6, (display[0]/display[1]), 1.0, 1500.0)
        #glTranslatef(400, 300, 0); # centre screen
        gluLookAt(position[0] * BLOCK_SIZE + (dist * math.cos(angle)), height, position[1] * BLOCK_SIZE + (dist * math.sin(angle)),
            position[0] * BLOCK_SIZE, 0, position[1] * BLOCK_SIZE,
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

if __name__ == '__main__':
    main()
