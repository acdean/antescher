__author__ = "adean"
__date__ = "$18-Jul-2016 10:42:42$"

from OpenGL.GL import *

class AntMap:

    colours = [[.7, .7, .7], [.3, .3, .3], [.5, .5, .5]]
    # 2d list of the columns
    data = []
    columns = []
    list = -1
    size = 0

    def __init__(self, size):
        print("AntMap")
        self.data = []
        self.size = size

    def read_map(self):
        print("AntMap.read_map")
        file = open('ANTATTCK.TAP', 'rb')
        file.seek(0x603C) # city data starts here
        for z in range(0, 128):
            self.data.append([])
            for x in range(0, 128):
                byte = file.read(1)
                byte = ord(byte[0]) & 0x3f # shouldn't need this - binary
                self.data[z].append(byte)
        #print(self.data)

    def rationalise_map(self):
        print("AntMap.rationalise_map")
        for z in range(0, 128):
            self.columns.append([])
            for x in range(0, 128):
                column = antColumn(x, z, data)
                self.columns[z].append(column)
        print("Self Columns: ", self.columns)

    # old version - draws all cubes
    def draw(self):
        for z in range(0, 128):
            for x in range(0, 128):
                if self.data[z][x] == 0:
                    continue
                self.draw_column(x, z, self.data[z][x])
            # y
        # x

    # new version, draws relevant display list
    def draw2(self, direction):
        for z in range(0, 128):
            for x in range(0, 128):
                if self.columns[z][x] == 0:
                    continue
                self.draw_column2(x, z, direction)
            # y
        # x

    def draw_column(self, x, y, data):
        for z in range(0, 6):
            if ((data & (0x1 << z)) != 0):
                self.draw_cube(x, z, y)

    def draw_column2(self, x, z, direction):
        if direction == NORTH_EAST:
            draw_column_list(x, z, columns[x][z].north)
            draw_column_list(x, z, columns[x][z].east)
        if direction == SOUTH_EAST:
            draw_column_list(x, z, columns[x][z].south)
            draw_column_list(x, z, columns[x][z].east)
        if direction == NORTH_WEST:
            draw_column_list(x, z, columns[x][z].south)
            draw_column_list(x, z, columns[x][z].west)
        if direction == NORTH_WEST:
            draw_column_list(x, z, columns[x][z].north)
            draw_column_list(x, z, columns[x][z].west)
        # always draw top
        draw_column_list(x, z, columns[x][z].top)

    def draw_cube(self, x, y, z):
        #print("draw_cube: " + str(x) + ":" + str(y) + ":" + str(z))

        x0 = 0.0
        x1 = self.size
        y0 = 0.0
        y1 = self.size
        z0 = 0.0
        z1 = self.size

        if (self.list == -1):
            # create a new displaylist
            self.list = glGenLists(1)
            glNewList(self.list, GL_COMPILE)

            glBegin(GL_QUADS)

            # top (y + 1 constant
            glColor3fv(self.colours[0])
            glVertex3f(x0, y1, z0)
            glVertex3f(x0, y1, z1)
            glVertex3f(x1, y1, z1)
            glVertex3f(x1, y1, z0)

            # north (x constant)
            glColor3fv(self.colours[1])
            glVertex3f(x0, y0, z0)
            glVertex3f(x0, y0, z1)
            glVertex3f(x0, y1, z1)
            glVertex3f(x0, y1, z0)

            # w (z constant)
            glColor3fv(self.colours[2])
            glVertex3f(x0, y0, z0)
            glVertex3f(x0, y1, z0)
            glVertex3f(x1, y1, z0)
            glVertex3f(x1, y0, z0)

            # s (x + 1 constant)
            glColor3fv(self.colours[1])
            glVertex3f(x1, y0, z0)
            glVertex3f(x1, y1, z0)
            glVertex3f(x1, y1, z1)
            glVertex3f(x1, y0, z1)

            # e (z + 1 constant)
            glColor3fv(self.colours[2])
            glVertex3f(x0, y0, z1)
            glVertex3f(x1, y0, z1)
            glVertex3f(x1, y1, z1)
            glVertex3f(x0, y1, z1)

            glEnd()
            glEndList()
        # end create list

        #print("drawing list: " + str(self.list))
        glPushMatrix()
        glTranslate(x * self.size, y * self.size, z * self.size)
        glCallList(self.list)
        glPopMatrix()
