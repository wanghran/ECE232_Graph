import numpy as np
import environment
import value_iteration
import RF1
import RF2
import irl
import matplotlib.pyplot as plt
from heat_map import heat_map


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
    acc_list = np.zeros(500)
    # l1_list = np.arange(0.0, 5.0, 0.01)
    l1_list = np.linspace(0.0, 5.0, 500)
    j = 0
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
        acc_list[j] = acc/100.0
        j += 1
    Mlambda = l1_list.item(int(np.argmax(acc_list)))
    print(Mlambda)
    learned_reward = irl.irl(env, Expert_P, Rmax, Mlambda)
    learned_reward_mesh = np.zeros((size, size))

    for s in env.S:
        learned_reward_mesh[int(s % 10), int(s / 10)] = learned_reward[s]
    # heat_map(learned_reward_mesh, 'reward heat map for lambda max') 
    env.R = learned_reward_mesh
    env.get_p()
    optV, optP = value_iteration.value_iteration(env)
    optV_mesh = np.zeros([size, size])
    for s in env.S:
        optV_mesh[int(s % 10), int(s / 10)] = optV[s]
    # heat_map(optV_mesh, 'heat map for the state value calculated \
            # from lambda max')
    environment.plot_policy(optP)


    # lambda max = 1.8336673346693386

    # plt.plot(l1_list, acc_list)
    # plt.title('lambda value vs. accurary')
    # plt.xlabel('lambda')
    # plt.ylabel('accuracy')
    # plt.show()


if __name__ == '__main__':
    main()
