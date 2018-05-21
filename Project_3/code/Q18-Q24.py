import numpy as np
import environment
from environment import plot_policy
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
    reward = RF2.RF2().reward
    Rmax = max(reward.flatten())
    actions = {'up': 0, 'down': 1, 'left': 2, 'right': 3}
    env = environment.Environment(100, actions, w, gamma, reward)

    _, Expert_P = value_iteration.value_iteration(env)

    # Inverse Reinforcement Learning
    acc_list = np.zeros(500)
    # l1_list = np.arange(0.0, 5.0, 0.01)
    l1_list = np.linspace(0.0, 5.0, 500)
    j = 0
    max_learn_reward_mesh = None
    max_acc = 0
    max_lambda = 0
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
        if acc_list[j] > max_acc:
            max_acc = acc_list[j]
            max_learn_reward_mesh = learned_reward_mesh
            max_lambda = l1 
        j += 1
    
    print("###### Q18######")
    plt.plot(l1_list, acc_list) 
    plt.title('Q18 Lambda vs. Accurary') 
    plt.xlabel('Lambda') 
    plt.ylabel('Accuracy') 
    plt.show()

    print("###### Q19######")   
    print("\tThe largest lamda is {}".format(max_lambda)) 
    # learned_reward = irl.irl(env, Expert_P, Rmax, Mlambda) 
    # learned_reward_mesh = np.zeros((size, size)) 
 
    print("###### Q20######")   
    heat_map(max_learn_reward_mesh, 'Reward heat map for Lambda max')

    print("###### Q21######")   
    env.R = max_learn_reward_mesh 
    env.get_p() 
    optV, optP = value_iteration.value_iteration(env) 
    optV_mesh = np.zeros([size, size]) 
    for s in env.S: 
        optV_mesh[int(s % 10), int(s / 10)] = optV[s] 
    heat_map(optV_mesh, 'Heat map of the state value calculated from Lambda max') 
 
    print("###### Q23######")   
    plot_policy(optP)

if __name__ == '__main__':
    main()
