import numpy as np

class Environment:
    def __init__(self,w, size):
        self.size = size
        self.w = w
        self.actions = [{1,0},{0,1}, {-1,0}, {0,-1}]

    def get_actions(self,x,y):
        res = []
        for dx, dy in self.actions:
            if not self.is_out(x+dx, y+dy):
                res.append({dx, dy})
    
    def is_out(self,x,y):
        if x < 0 or x >= self.size:
            return True
        if y < 0 or y >= self.size:
            return True
        return False


