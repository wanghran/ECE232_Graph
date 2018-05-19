from environment import Environment
import value_iteration
import value_map

env = Environment(0.1, 10)
opt_reward = None
S = range(size * size)
A = ['up', 'down', 'left', 'right']
gamma = 0.8
optV, _ = value_iteration(env, opt_reward, S, A, gamma)
V_mesh = np.zeros((size, size))
for s in S:
    V_mesh[s % 10, s / 10] = optV[s]
value_map.value_map(V_mesh, 'state value heat map for the \
                    optimal reward function')
