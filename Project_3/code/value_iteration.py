import numpy as np
import RF1
import RF2
import environment
import heat_map
import value_map

EPSILON = 0.01


def value_iteration(env, reward, S, A, gamma):
    V = np.zeros(len(S))
    V_tmp = np.zeros(len(S))
    delta = 10000  # large number

    while delta > EPSILON:
        delta = 0
        for s in S:
            v = V[s]
            # find the maximum action-value
            maximum = 0
            for a in A:
                P = env.get_next_state_prob(s % 10, s / 10, a)
                summation = 0
                for s_prime, possibility in P.items():
                    summation += possibility * (reward[s % 10, s / 10] + gamma * V[s_prime])
                if summation > maximum:
                    maximum = summation
                    a_optimal = a
            V_tmp[s] = maximum
            delta = max(delta, abs(v - V_tmp[s]))
        for s in S:
            V[s] = V_tmp[s]

    # for s in S:
    #     pi[s] = find the max index

    return V


def main():
    size = 10
    A = ['up', 'down', 'left', 'right']
    w = 0.1
    gamma = 0.8
    reward = RF2.RF2().reward

    env = environment.Environment(w, size)
    S = range(size * size)

    V_optimal = value_iteration(env, reward, S, A, gamma)

    V_mesh = np.zeros((size, size))
    for s in S:
        V_mesh[s % 10, s / 10] = V_optimal[s]

    # draw value_map
    value_map.value_map(V_mesh, 'Q2')
    # draw heat_map
    heat_map.heat_map(V_mesh, 'Q3')


if __name__ == '__main__':
    main()
