# item holding a single column
# this is 5 ints denoting the n, e, s, w, top values
# which will differ depending on neighbours

__author__ = "adean"
__date__ = "$18-Jul-2016 10:58:39$"

class AntColumn:

    north = 0
    east = 0
    south = 0
    west = 0
    top = 0

    def __init__(self, x, z, data):
        if data[x][z] != 0:
            if x - 1 < 0:
                self.north = data[x][z]
            else:
                self.north = data[x][z] & ~data[x - 1][z]
            if z + 1 >= MAP_SIZE:
                self.east  = data[x][z]
            else:
                self.east  = data[x][z] & ~data[x][z + 1]
            if x + 1 >= MAP_SIZE:
                self.south = data[x][z]
            else:
                self.south = data[x][z] & ~data[x + 1][z]
            if z - 1 < 0:
                self.west  = data[x][z]
            else:
                self.west  = data[x][z] & ~data[x][z - 1]
            # top only if this cube is full but the one above is empty
            for y in [0x1, 0x2, 0x4, 0x8, 0x10, 0x20]:
                if ((data[x][z] & y) != 0):             # this bit is set
                    if ((data[x][z] & (y << 1)) == 0):  # the one above it isn't
                        self.top = self.top | y         # set this bit
