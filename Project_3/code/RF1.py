"""
Reward Function 1
"""

import numpy as np


class RF1:
    def __init__(self):
        self._reward = np.zeros([10, 10])
        self._reward[9, 9] = 1.0

    @property
    def reward(self):
        return self._reward
