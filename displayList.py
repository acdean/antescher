# all the display lists
# there are 1, 2, 3, 4, 5, 6 cubes in a list
# there are 5 directions

from OpenGL.GL import *

class DisplayList:
    block_lists = []

#    def __init__(self):

    def generate(self, size):
        for d in range(0, 5):       # directions
            self.block_lists.append([])
            for i in range(1, 6):   # blocks
                x0 = 0
                y0 = 0
                z0 = 0
                x1 = size
                y1 = i * size
                z1 = size
                print("DI:", d, i)
                l = glGenLists(1)
                glNewList(l, GL_COMPILE);
                glBegin(GL_QUADS)
                if (d == 0):    # NORTH
                    glVertex3f(x0, y0, z0)
                    glVertex3f(x0, y0, z1)
                    glVertex3f(x0, y1, z1)
                    glVertex3f(x0, y1, z0)
                elif (d == 1):  # EAST
                    glVertex3f(x0, y0, z1)
                    glVertex3f(x1, y0, z1)
                    glVertex3f(x1, y1, z1)
                    glVertex3f(x0, y1, z1)
                elif (d == 2):  # SOUTH
                    glVertex3f(x1, y0, z0)
                    glVertex3f(x1, y1, z0)
                    glVertex3f(x1, y1, z1)
                    glVertex3f(x1, y0, z1)
                elif (d == 3):  # WEST
                    glVertex3f(x0, y0, z0)
                    glVertex3f(x0, y1, z0)
                    glVertex3f(x1, y1, z0)
                    glVertex3f(x1, y0, z0)
                elif (d == 4):  # TOP
                    glVertex3f(x0, y1, z0)
                    glVertex3f(x0, y1, z1)
                    glVertex3f(x1, y1, z1)
                    glVertex3f(x1, y1, z0)
                glEnd()
                glEndList()
                self.block_lists[d].append(l)
            print("BLOCK LISTS:", self.block_lists)

