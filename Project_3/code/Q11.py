import numpy as np
import environment
import value_iteration
import RF1
import RF2
import irl


def main():
    size = 10
    w = 0.1
    gamma = 0.8
    reward = RF1.RF1().reward
    Rmax = max(reward.flatten())
    actions = {'up': 0, 'down': 1, 'left': 2, 'right': 3}
    env = environment.Environment(100, actions, w, gamma, reward)

    _, Expert_P = value_iteration.value_iteration(env)

    # Inverse Reinforcement Learning
    acc_list = np.empty([500])
    l1_list = np.arange(0.0, 5.0, 0.01)
    for l1 in l1_list:
        learned_reward = irl.irl(env, Expert_P, Rmax, l1)
        learned_reward_mesh = np.zeros((size, size))

        for s in env.S:
            learned_reward_mesh[int(s % 10), int(s / 10)] = learned_reward[s]
        env.R = learned_reward_mesh
        env.get_p()

        _, Agent_P = value_iteration.value_iteration(env)

        acc = 0
        for i in range(100):
            if (Agent_P[i] == Expert_P[i]):
                acc += 1
        np.append(acc_list, [acc/100.0])
    print(acc_list)


if __name__ == '__main__':
    main()
