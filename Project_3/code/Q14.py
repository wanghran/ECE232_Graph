from environment import Environment
from RF1 import RF1
import value_iteration
import value_map
from irl import irl

og_reward = RF1().reward
env = Environment(0.1, 10)
S = range(size * size)
A = ['up', 'down', 'left', 'right']
gamma = 0.8
ogV, ogP = value_iteration(env, og_reward, S, A, gamma)
opt_reward = irl(100, 4, None, ogP, gamma, og_reward)
optV, _ = value_iteration(env, opt_reward, S, A, gamma)
V_mesh = np.zeros((size, size))
for s in S:
    V_mesh[s % 10, s / 10] = optV[s]
value_map.value_map(V_mesh, 'state value heat map for the \
                    optimal reward function')
