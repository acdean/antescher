__author__ = "adean"
__date__ = "$18-Jul-2016 10:42:42$"

from OpenGL.GL import *


class AntMap:

    MAP_SIZE = 128

    colours = [[.7, .7, .7], [.3, .3, .3], [.5, .5, .5]]
    data = [] # 2d list holding binary data read from file
    columns = [] # 2d list of Columns
    list = -1
    blockSize = 0

    def __init__(self, blockSize):
        print("AntMap")
        self.data = []
        self.blockSize = blockSize

    def read_map(self):
        print("AntMap.read_map")
        blocks = 0;
        file = open('ANTATTCK.TAP', 'rb')
        file.seek(0x603C) # city data starts here
        for z in range(0, self.MAP_SIZE):
            self.data.append([])
            for x in range(0, self.MAP_SIZE):
                byte = file.read(1)
                byte = ord(byte[0]) & 0x3f # shouldn't need this - binary
                #byte = byte[0] & 0x3f
                self.data[z].append(byte)
                if (byte != 0):
                    blocks += 1
                # fi
            # for x
        # for z
        #print(self.data)
        print(blocks, " blocks out of ", (self.MAP_SIZE * self.MAP_SIZE))

    def rationalise_map(self):
        print("AntMap.rationalise_map")
        for z in range(0, MAP_SIZE):
            self.columns.append([])
            for x in range(0, MAP_SIZE):
                column = antColumn(x, z, data)
                self.columns[z].append(column)
        print("Self Columns: ", self.columns)

    # old version - draws all cubes
    def draw(self):
        for z in range(0, self.MAP_SIZE):
            for x in range(0, self.MAP_SIZE):
                if self.data[z][x] == 0:
                    continue
                self.draw_column(x, z, self.data[z][x])
            # x
        # z

    # new version, draws relevant display list
    def draw2(self, direction):
        for z in range(0, self.MAP_SIZE):
            for x in range(0, self.MAP_SIZE):
                if self.columns[z][x] == 0:
                    continue
                self.draw_column2(x, z, direction)
            # x
        # z

    def draw_column(self, x, y, data):
        for z in range(0, 6):
            if ((data & (0x1 << z)) != 0):
                self.draw_cube(x, z, y)
            # fi
        # z

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
        x1 = self.blockSize
        y0 = 0.0
        y1 = self.blockSize
        z0 = 0.0
        z1 = self.blockSize

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
        glTranslate(x * self.blockSize, y * self.blockSize, z * self.blockSize)
        glCallList(self.list)
        glPopMatrix()
