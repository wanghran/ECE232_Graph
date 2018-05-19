from cvxopt import matrix, solvers
import numpy as np
import environment
import value_iteration


def Q11(A, opt_P, OG_reward):
    lamb = np.arange(0.0, 5.0, 0.01)
    I = np.identity(100)
    env = environment.Environment(0.1, 100)
    A = ['up', 'down', 'left', 'right']
    gamma = 0.8
    acc_list = np.empty([500])
    for i in lamb:
        C = matrix([0, 1, -i])
        G = matrix([[-A, I, 0], [-A, 0, 0], [-I, 0, -I],
                    [-I, 0, -I], [-I, 0, 0], [I, 0, 0]])
        h = matrix([0, 0, 0, 0, reward, reward])
        sol = solvers.lp(c, G, h)
        x = sol['x']
        reward = x[0]
        S = range(10 * 10)
        _, P = value_iteration.value_iteration(env, reward, S, A, gamma)
        acc = 0
        for j in range(101):
            if (P[j] == opt_P[j]):
                acc += 1
        np.append(acc_list, [acc/100.0])
    plot(lamb, acc_list)