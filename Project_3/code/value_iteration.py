import numpy as np
from RF1 import RF1
from RF2 import RF2
import environment
from environment import plot_policy
import heat_map
import value_map

EPSILON = 0.01


def value_iteration(env):
    # Initialization
    S = env.S
    delta = float("inf")  # large number
    reward = env.R
    gamma = env.gamma
    P = env.P
    A = env.actions.keys()
    V = np.zeros(len(S))
    V_tmp = np.zeros(len(S))
    PI = ['null'] * len(S)
    # Estimation
    while delta > EPSILON:
        delta = 0
        for s in S:
            v = V[s]
            # find the maximum action-value
            maximum = float("-inf")
            i = 0
            for a in A:
                p_s = P[i][s]
                summation = 0
                for s_prime in range(len(p_s)):
                    possibility = p_s[s_prime]
                    summation += possibility * (reward[int(s % 10), int(s / 10)] + gamma * V[s_prime])
                maximum = max(maximum, summation)
                i += 1
            V_tmp[s] = maximum
            delta = max(delta, abs(v - V_tmp[s]))
        for s in S:
            V[s] = V_tmp[s]

    # Computation
    for s in S:
        maximum = float("-inf")
        i = 0
        a_optimal = 'null'
        for a in A:
            p_s = P[i][s]
            summation = 0
            for s_prime in range(len(p_s)):
                possibility = p_s[s_prime]
                summation += possibility * (reward[int(s % 10), int(s / 10)] + gamma * V[s_prime])
            if summation > maximum:
                a_optimal = a
                maximum = summation
            i += 1
        PI[s] = a_optimal

    return V, PI


def main():
    size = 10
    w = 0.1
    gamma = 0.8
    reward = RF1().reward
    actions = {'up': 0, 'down': 1, 'left': 2, 'right': 3}
    env = environment.Environment(100, actions, w, gamma, reward)

    V_optimal, PI_optimal = value_iteration(env)
    V_mesh = np.zeros((size, size))
    for s in env.S:
        V_mesh[s % 10, s / 10] = float('%.3f' % (V_optimal[s]))

    # draw value_map
    value_map.value_map(V_mesh, 'Q2')
    # draw heat_map
    heat_map.heat_map(V_mesh, 'Q3')
    # draw policy_map
    plot_policy(PI_optimal)


if __name__ == '__main__':
    main()
