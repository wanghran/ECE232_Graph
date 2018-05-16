"""
Reward Function 1
"""

import numpy as np


class RF1:
    def __init__(self):
        self.reward = np.zeros([10, 10])
        self.reward[9, 9] = 1.0
