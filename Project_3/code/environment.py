class Environment:
    def __init__(self, w, size):
        self.size = size
        self.w = w
        self.actions = {'up': 0, 'down': 1, 'left': 2, 'right': 3}

    def is_out(self, x, y):
        if x < 0 or x >= self.size:
            return True
        if y < 0 or y >= self.size:
            return True
        return False


    def get_diretion(self, action):
        if action == 'up':
            return 0,-1
        if action == 'down':
            return 0,1
        if action == 'left':
            return -1,0
        if action == 'right':
            return 0,1

    def get_next_state_prob(self, x, y, action):
        omega = float(self.w/4)
        states = [omega,omegagiit omega,omega,0]
        states[self.actions[action]] += 1 - self.w
        res = {}
        for a in self.actions:
            dx, dy = self.get_diretion(a)
            if self.is_out(x+dx, y+dy):
                states[4] += states[self.actions[a]]
                states[self.actions[a]] = 0

        for a in self.actions:
            dx, dy = self.get_diretion(a)
            key = (x+dx) + (y+dy)*10
            value = states[self.actions[a]]
            res[key] = value
        res[x+y*10] = states[4]
        return res

