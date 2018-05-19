import numpy as np
import matplotlib.pyplot as plt
import heat_map
from RF1 import RF1

og_reward = RF1()
heat_map.heat_map(og_reward.reward, 'heat map for ground truth reward')
opt_reward = None
heat_map.heat_map(opt_reward, 'heat map for optimal reward')
