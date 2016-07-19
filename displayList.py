# all the display lists
# there are 1, 2, 3, 4, 5, 6 cubes in a list
# there are 5 directions

from OpenGL.GL import *

class DisplayList:
    block_lists = []

#    def __init__(self):

    def generate(self):
        glGenLists(1)
        for d in range(0, 5):       # directions
            self.block_lists.append([])
            for i in range(0, 6):   # blocks
                print("DI:", d, i)
                self.block_lists[d].append(glGenLists(1))
            print("BLOCK LISTS:", self.block_lists)
