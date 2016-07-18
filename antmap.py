__author__ = "adean"
__date__ = "$18-Jul-2016 10:42:42$"

from OpenGL.GL import *

class AntMap:

    # 2d list of the columns
    columns = []
    SIZE = 16.0
    list = -1

    def __init__(self):
        print("AntMap")
        self.data = []

    def read_map(self):
        print("AntMap.read_map")
        file = open('ANTATTCK.TAP', 'rb')
        file.seek(0x603C) # city data starts here
        for x in range(0, 128):
            self.columns.append([])
            for y in range(0, 128):
                byte = file.read(1)
                byte = byte[0] & 0x3f
                self.columns[x].append(byte)
        #print(self.columns)

    def draw(self):
        for x in range(0, 128):
            for y in range(0, 128):
                if self.columns[x][y] == 0:
                    continue
                self.draw_column(x, y, self.columns[x][y])
            # y
        # x

    def draw_column(self, x, y, data):
        for z in range(0, 6):
            if ((data & (0x1 << z)) != 0):
                self.draw_cube(x, z, y)

    def draw_cube(self, x, y, z):
        #print("draw_cube: " + str(x) + ":" + str(y) + ":" + str(z))

        x0 = 0.0
        x1 = self.SIZE
        y0 = 0.0
        y1 = self.SIZE
        z0 = 0.0
        z1 = self.SIZE

        if (self.list == -1):
            # create a new displaylist
            self.list = glGenLists(1)
            glNewList(self.list, GL_COMPILE)

            glBegin(GL_QUADS)

            # top (y + 1 constant
            glColor3fv([1, 0, 0])
            glVertex3f(x0, y1, z0)
            glVertex3f(x0, y1, z1)
            glVertex3f(x1, y1, z1)
            glVertex3f(x1, y1, z0)

            # north (x constant)
            glColor3fv([0, 1, 0])
            glVertex3f(x0, y0, z0)
            glVertex3f(x0, y0, z1)
            glVertex3f(x0, y1, z1)
            glVertex3f(x0, y1, z0)

            # w (z constant)
            glColor3fv([0, 0, 1])
            glVertex3f(x0, y0, z0)
            glVertex3f(x0, y1, z0)
            glVertex3f(x1, y1, z0)
            glVertex3f(x1, y0, z0)

            # s (x + 1 constant)
            glColor3fv([0, 1, 1])
            glVertex3f(x1, y0, z0)
            glVertex3f(x1, y1, z0)
            glVertex3f(x1, y1, z1)
            glVertex3f(x1, y0, z1)
#
            # e (z + 1 constant)
            glColor3fv([1, 0, 1])
            glVertex3f(x0, y0, z1)
            glVertex3f(x1, y0, z1)
            glVertex3f(x1, y1, z1)
            glVertex3f(x0, y1, z1)

            glEnd()
            glEndList()
        # end create list

        # print("drawing list" + str(self.list))
        glPushMatrix()
        glTranslate(x * self.SIZE, y * self.SIZE, z * self.SIZE)
        glCallList(self.list)
        glPopMatrix()
