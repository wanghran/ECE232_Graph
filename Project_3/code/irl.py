from cvxopt import matrix, solvers
import numpy as np


def irl(n_states, n_actions, transition_probability, policy, discount, Rmax, l1):
    A = set(range(n_actions))

    # Minimise c . x.
    c = -np.hstack([np.zeros(n_states), np.ones(n_states), -l1 * np.ones(n_states)])

    # TODO might need
    # Set of actions to help manage reordering actions.
    # The transition policy convention is different here to the rest of the code
    # for legacy reasons; here, we reorder axes to fix this. We expect the
    # new probabilities to be of the shape (A, N, N).
    # transition_probability = np.transpose(transition_probability, (1, 0, 2))

    def T(a, s):
        return np.dot(transition_probability[policy[s], s] - transition_probability[a, s],
                      np.linalg.inv(np.eye(n_states) - discount*transition_probability[policy[s]]))

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
