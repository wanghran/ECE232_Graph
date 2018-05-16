"""
Reward Function 2
"""

import numpy as np


class RF2:
    def __init__(self):
        self._reward = np.zeros([10, 10])
        self._reward[9, 9] = 10.0
        for i in range(1, 7):
            self._reward[i, 4] = -100.0
        self._reward[1, 5] = -100.0
        self._reward[1, 6] = -100.0
        self._reward[2, 6] = -100.0
        self._reward[3, 6] = -100.0
        self._reward[3, 7] = -100.0
        self._reward[3, 8] = -100.0
        self._reward[4, 8] = -100.0
        self._reward[5, 8] = -100.0
        self._reward[6, 8] = -100.0
        self._reward[7, 8] = -100.0
        self._reward[7, 7] = -100.0
        self._reward[7, 6] = -100.0
        self._reward[8, 6] = -100.0

    @property
    def reward(self):
        return self._reward
