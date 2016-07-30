# all the display lists
# there are 1, 2, 3, 4, 5, 6 cubes in a list
# there are 5 directions

from OpenGL.GL import *

class DisplayList:
    column = []

#    def __init__(self):

    def generate(self,  size):
        for i in range(0,  64):
            if (i == 0):
                # 0 = no blocks
                self.column.append(-1)
            else :
                glList = glGenLists(1)
                glNewList(glList, GL_COMPILE);
                glBegin(GL_QUADS)
                self.calcList(i,  size)
                glEnd()
                glEndList()
                self.column.append(glList)
            # end if
        # end i
        print(self.column);

    def calcList(self,  i,  size):
        print("")
        print "i: %d" % i
        start = -1
        # 7 is ok here. it will always be 0
        # it also makes sure the last block is always terminated
        for b in range(0, 7):
            bit = 1 << b;
            if ((i & bit) == bit):
                print "block: %d" % i
                # found a block
                if (start == -1):
                    start = b
                    print "start: %d" % start
                # end if
            else: #
                print("no block: ",  b)
                # found no block
                if (start != -1):
                    print "line: %d - %d" % (start, b)
                    # there is a current group so finish it
                    # this is the east facing quad. do more? rotate this?
                    glVertex3f(0,  start * size,  0)
                    glVertex3f(size,  start * size,  0)
                    glVertex3f(size,  b * size,  0)
                    glVertex3f(0,  b * size,  0)
                # end if
                start = -1
            # end if
        # end for

    # unused
    def generateOld(self, size):
        for d in range(0, 5):       # directions
            self.block_lists.append([])
            self.column.append([])
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
            self.column[d].append(0) # 0 - do nothing

            self.column[d].append(self.block_lists[d][1]); # 1 000001

            l = glGenLists(1)
            glNewList(l, GL_COMPILE);
            glPushMatrix()
            glTranslate(size,  0,  0)
            glCallList(self.display_lists[d][1])
            glPopMatrix()
            glEndList()
            self.column[d].append(l); # 2 000010 - 1 translated

            self.column[d].append(self.block_lists[d][2]); # 3 000011
        # for d

if __name__ == '__main__':
    print("test")
    d = DisplayList()
    d.calcList(1,  16)
    d.calcList(2,  16)
    d.calcList(3,  16)
    d.calcList(7,  16)
    d.calcList(0b101010,  16)
