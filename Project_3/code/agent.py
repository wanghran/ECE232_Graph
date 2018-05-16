"""
An agent class that has three attributes: x, y and position, corresponding to
the actually value in the grid. Four actions associate with the agent: move
up, move down, move left, and move right.
"""

import numpy as np


class agent:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._position = self._x * 10 + self._y
        if (self._position > 99.0 or self._position < 0.0):
            raise ValueError("Position should be between 0.0 to 99.0")

    def __str__(self):
            return "x: " + str((self._position - self._position % 10) / 10) \
             + " y: " + str(self._position % 10)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x
        self._position = self._x * 10 + self._y
        if (self._position > 99.0 or self._position < 0.0):
            raise ValueError("Position should be between 0.0 to 99.0")

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y
        self._position = self._x * 10 + self._y
        if (self._position > 99.0 or self._position < 0.0):
            raise ValueError("Position should be between 0.0 to 99.0")

    @property
    def position(self):
        self._position = self._x * 10 + self._y
        return self._position

    """
    TODO: agent could be able to move out of the grid with certain
    probability
    """

    def moveUp(self):
        self._y -= 1
        self._position = self._x * 10 + self._y
        if (self._position < 0.0):
            raise ValueError("Cannot move up, over boundary")

    def moveDown(self):
        self._y += 1
        self._position = self._x * 10 + self._y
        if (self._position > 99.0):
            raise ValueError("Cannot move down, over boundary")

    def moveRight(self):
        self._x += 1
        self._position = self._x * 10 + self._y
        if (self._position > 99.0):
            raise ValueError("Cannot move right, over boundary")

    def moveLeft(self):
        self._x -= 1
        self._position = self._x * 10 + self._y
        if (self._position > 99.0):
            raise ValueError("Cannot move left, over boundary")

    def neighbor(self):
        Up = (self._y - 1) if((self._y - 1) > 0.0) else (-1)
        Down = (self._y + 1) if((self._y + 1) < 9.0) else (-1)
        Left = (self._x - 1) if((self._x - 1) > 0.0) else (-1)
        Right = (self._x + 1) if((self._x + 1) < 9.0) else (-1)
        form = []
        if (Up != -1):
            form.append([self._x, Up])
        if (Down != -1):
            form.append([self._x, Down])
        if (Left != -1):
            form.append([Left, self._y])
        if (Right != -1):
            form.append([Right, self._y])
        return np.array(form)

    def isNeighbor(self, x, y):
        neighborList = self.neighbor()
        for row in neighborList:
            if (row[0] == x and row[1] == y):
                return True
        return False

    def atCorner(self):
        return (True) if(self._position == 0 or
                         self._position == 9 or
                         self._position == 90 or
                         self._position == 99)
        (False)
