
# Generic Block object - has some number of sides which each have a string
# With the periodic blocks there are (usually) 6 sides, always with 1 or 2 letters on each side, this
# is kept generic to use with different blocks/letter combinations.
class Block:
    def __init__(self):
        self.sides = [] # list of strings on each side of block

    def addside(self, sidestring):
        self.sides.append(sidestring)

class BlockSet:
    def __init__(self):
        self.blocks = [] # list of blocks within the set

    # Add a new block to the block set
    #   stringslist is a list of strings, each will be a side on the new block
    def addblock(self, stringslist):
        newblock = Block()
        for s in stringslist:
            newblock.addside(s)
        self.blocks.append(newblock)
