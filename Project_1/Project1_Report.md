# Part 1







# Part 2  
## Problem 1  


## Problem 2  
### b  
![alt text](https://github.com/wanghran/ECE232_Graph/blob/master/Project_1/plots/2_2_1.png)  
![alt text](https://github.com/wanghran/ECE232_Graph/blob/master/Project_1/plots/2_2_2.png)  
The average distance graph seems converge around 1500 steps with the average distance about
8 while the variance graph still fluctuates even for 2000 steps.  
### c  
![alt text](https://github.com/wanghran/ECE232_Graph/blob/master/Project_1/plots/2_2_3.png)  
From this graph, it is quite clear that the degree distribution for random walk is similar to that of the original graph. 
Since random walk is like doing random sampling from the original graph, the result is in expectation.  
### d  
![alt text](https://github.com/wanghran/ECE232_Graph/blob/master/Project_1/plots/2_2_4.png)  
![alt text](https://github.com/wanghran/ECE232_Graph/blob/master/Project_1/plots/2_2_5.png)  
![alt text](https://github.com/wanghran/ECE232_Graph/blob/master/Project_1/plots/2_2_6.png)  
![alt text](https://github.com/wanghran/ECE232_Graph/blob/master/Project_1/plots/2_2_7.png)  
Comparing to those three sets of graphs, we can see that with higher number of nodes, the convergence will take more steps. 
The plots with number of node equal to 100, it converge quite easily, at around 300. With 1000 nodes, the curve converges at around 1700 steps. 
With 10000 nodes, the curve does not even look like converge at step 2000. With higher number of nodes, the diameter of the network is also higher. 
Therefore, the higher the diameter of a network is, the longer it will take for the average distance and the variance of distance of random walks to converge.