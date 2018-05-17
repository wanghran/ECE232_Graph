import numpy as np
import RF1
import RF2
import environment
import heat_map
import value_map

EPSILON = 0.01


def value_iteration(env, reward, S, A, gamma):
    # Initialization
    V = np.zeros(len(S))
    V_tmp = np.zeros(len(S))
    PI = ['null'] * len(S)
    delta = 10000  # large number

    # Estimation
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
                maximum = max(maximum, summation)
            V_tmp[s] = maximum
            delta = max(delta, abs(v - V_tmp[s]))
        for s in S:
            V[s] = V_tmp[s]

    # Computation
    for s in S:
        maximum = 0
        for a in A:
            P = env.get_next_state_prob(s % 10, s / 10, a)
            summation = 0
            for s_prime, possibility in P.items():
                summation += possibility * (reward[s % 10, s / 10] + gamma * V[s_prime])
            if summation > maximum:
                a_optimal = a
                maximum = summation
        PI[s] = a_optimal

    return V, PI


def main():
    size = 10
    A = ['up', 'down', 'left', 'right']
    w = 0.1
    gamma = 0.8
    reward = RF1.RF1().reward

    env = environment.Environment(w, size)
    S = range(size * size)

    V_optimal, PI_optimal = value_iteration(env, reward, S, A, gamma)

    V_mesh = np.zeros((size, size))
    for s in S:
        V_mesh[s % 10, s / 10] = V_optimal[s]

    # draw value_map
    value_map.value_map(V_mesh, 'Q2')
    # draw heat_map
    heat_map.heat_map(V_mesh, 'Q3')


    arrows = {'left': u'\u2190', 'up': u'\u2191', 'right': u'\u2192', 'down': u'\u2193' }
    pi_temp = [['' for x in range(size)] for y in range(size)] 

    for s in S:
        pi_temp[s % 10][s / 10] = arrows[PI_optimal[s]].encode("utf-8")

    for line in pi_temp:
        for arrow in line:
            print arrow,
            print '   ',
        print('\n')


if __name__ == '__main__':
    main()
