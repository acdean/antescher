# all the display lists
# there are 1, 2, 3, 4, 5, 6 cubes in a list
# there are 5 directions

from OpenGL.GL import *

class DisplayList:
    block_lists = []
    column = []

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
            # for i
            print("BLOCK LISTS:", self.block_lists)
            
            # define the columns
            column[d].append(0) # 0 - do nothing

            column[d].append(block_lists[d][1]); # 1 000001

            l = glGenLists(1)
            glNewList(l, GL_COMPILE);
            glPushMatrix()
            glTranslate(size)
            glDrawList(display_lists[d][1])
            glPopMatrix()
            glEndList()
            column[d].append(l); # 2 000010 - 1 translated

            column[d].append(block_lists[d][2]); # 3 000011

            # for i = 0 to 63
            # if i & this == this
            # then we can use this in the list
            # then remove this - i = i & ~this
            # repeat until i = 0

            # 63 111111
            
            # 62 111110
            # 31 011111
            
            # 15 001111
            # 30 011110
            # 60 111100
            
            #  7 000111
            # 14 001110
            # 28 011100
            # 56 111000
            
            #  3 000011
            #  6 000110
            # 12 001100
            # 24 011000
            # 48 110000
            
            #  1 000001
            #  2 000010
            #  4 000100
            #  8 001000
            # 16 010000
            # 32 100000

        # for d

