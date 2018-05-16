import RF1
import RF2
import environment
import numpy as np
import heat_map

EPSILON = 0.01


def value_iteration(env, reward, S, A, gamma):
    V = np.zeros(len(S))
    delta = 1000  # large number

    while delta > EPSILON:
        delta = 0
        for s in S:
            v = V[s]
            # find the maximum action-value
            maximum = 0
            for a in ['up', 'down', 'left', 'right']:
                P = env.get_next_state_prob(s % 10, s / 10, a)
                summation = 0
                for s_prime, possibility in P.items():
                    summation = summation + possibility * (reward[s % 10, s / 10] + gamma * V[s_prime])
                if summation > maximum:
                    maximum = summation
            V[s] = maximum
            delta = max(delta, abs(v-V[s]))
    # for s in S:
    #     pi[s] = find the max index

    return V


def main():
    w = 0.1
    size = 10
    gamma = 0.8
    env = environment.Environment(w, size)
    reward_1 = RF2.RF2()
    reward = reward_1.reward
    S = range(size * size)
    A = ['up', 'down', 'left', 'right']

    V = value_iteration(env, reward, S, A, gamma)

    # draw heat map
    V_tmp = np.zeros((size, size))

    for s in S:
        V_tmp[s % 10, s / 10] = V[s]
    print(V_tmp)
    heat_map.heat_map(V_tmp, 'Heat Map of State Value')


if __name__ == '__main__':
    main()
