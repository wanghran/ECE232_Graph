from cvxopt import matrix, solvers
import numpy as np


def irl(env, policy, Rmax, l1):
    n_states = env.size
    n_actions = len(env.actions.keys())
    transition_probability = env.P
    discount = env.gamma

    A = set(env.actions.keys())

    # Minimise c . x.
    c = -np.hstack([np.zeros(n_states), np.ones(n_states), -l1 * np.ones(n_states)])

    def get_index(env, a):
        return list(env.actions.keys()).index(a)

    def T(a, s):
        return np.dot(transition_probability[get_index(env, policy[s]), s]
                                    - transition_probability[get_index(env, a), s],
                      np.linalg.inv(np.eye(n_states)
                                    - discount*transition_probability[get_index(env, a)]))

    # 300 * 100
    T_stack = np.vstack([
        -T(a, s)
        for s in range(n_states)
        for a in A - {policy[s]}
    ])
    # 300 * 100
    I_stack1 = np.vstack([
        np.eye(1, n_states, s)
        for s in range(n_states)
        for a in A - {policy[s]}
    ])
    # 100 * 100
    I_stack2 = np.eye(n_states)
    # 300 * 100
    zero_stack1 = np.zeros((n_states * (n_actions - 1), n_states))
    # 100 * 100
    zero_stack2 = np.zeros((n_states, n_states))

    D_left = np.vstack([T_stack, T_stack, -I_stack2, I_stack2, -I_stack2, I_stack2])
    D_middle = np.vstack([I_stack1, zero_stack1, zero_stack2, zero_stack2, zero_stack2, zero_stack2])
    D_right = np.vstack([zero_stack1, zero_stack1, -I_stack2, -I_stack2, zero_stack2, zero_stack2])
    D = np.hstack([D_left, D_middle, D_right])

    b = np.zeros((n_states*(n_actions-1)*2 + 2*n_states, 1))
    b_bounds = np.vstack([Rmax*np.ones((n_states, 1))]*2)
    b = np.vstack((b, b_bounds))

    A_ub = matrix(D)
    b = matrix(b)
    c = matrix(c)
    results = solvers.lp(c, A_ub, b)
    r = np.asarray(results["x"][:n_states], dtype=np.double)

    return r.reshape((n_states,))
