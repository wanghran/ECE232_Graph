import numpy as np
import RF1


class Environment:
    #{'up': 0, 'down': 1, 'left': 2, 'right': 3}

    def __init__(self, size, actions,omega,gamma,R):
        self.size = size
        self.omega = omega
        self.gamma = gamma
        self.R = R
        self.actions = actions
        self.P = self.find_p()
        self.S = range(10 * 10)

    def is_out(self, x, y):
        if x < 0 or x >= 10:
            return True
        if y < 0 or y >= 10:
            return True
        return False

    def get_diretion(self, action):
        if action == 'up':
            return -1, 0
        if action == 'down':
            return 1, 0
        if action == 'left':
            return 0, -1
        if action == 'right':
            return 0, 1

    def find_p(self):
        size = self.size
        res = np.zeros((4,size, size))
        count =0
        for action in self.actions.keys():
            p_i = np.zeros((size, size))
            grid = np.zeros((int(size/10), int(size/10)))
            for i in range(grid.shape[0]):
                for j in range(grid.shape[1]):
                    prob = self.get_neighbor_p(i,j,action)
                    for k in prob:
                        p_i[(i+j*10), k] = prob[k]
            res[count] = p_i
            count +=1
        return res

    def get_neighbor_p(self, x,y, action):
        omega = float(self.omega/4)
        states = [omega, omega, omega, omega, 0]
        states[self.actions[action]] += 1 - self.omega
        res = {}
        for a in self.actions:
            dx, dy = self.get_diretion(a)
            if self.is_out(x+dx, y+dy):
                states[4] += states[self.actions[a]]
                states[self.actions[a]] = 0

        for a in self.actions:
            dx, dy = self.get_diretion(a)
            if not self.is_out(x+dx, y+dy):
                key = (x+dx) + (y+dy)*10
                value = states[self.actions[a]]
                res[key] = value
        res[x+y*10] = states[4]
        return res

    def get_p(self):
        return self.P


def plot_policy(policy_map):
    S = range(10 * 10)
    arrows = {'left': u'\u2190', 'up': u'\u2191', 'right': u'\u2192', 'down': u'\u2193' }
    pi_temp = [['' for x in range(10)] for y in range(10)] 

    for s in S:
        pi_temp[int(s % 10)][int(s / 10)] = arrows[policy_map[s]]

    for line in pi_temp:
        for arrow in line:
            print(arrow ,end='')
            print('\t', end='')
        print('\n')
    return None