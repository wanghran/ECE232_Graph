# Part 1
<<<<<<< HEAD
##Problem 1
=======
## (a)
![degree distribution p=0.003](./plots/wang/1_1_1.png)
![degree distribution p=0.004](./plots/wang/1_1_2.png)
![degree distribution p=0.01](./plots/wang/1_1_3.png)
![degree distribution p=0.05](./plots/wang/1_1_4.png)
![degree distribution p=0.1](./plots/wang/1_1_5.png)
The distributions are binomial distributions that center at their own average degrees, which are the probability p times the number of nodes, 1000. With higher probability, the graph tends to be more likely to have vertices with more edges. Therefore, comparing to p = 0.003, the graph for p = 0.01 starts at degree approximately greater than 75, which means almost all the nodes are connected. The reason for that is the probability p is greater than the threshold, c * ln(1000)/1000, where c is an arbitrary constant. Therefore, from graph 3, the frequency of degree 0 is 0. And the spikes of every graphs are caused by the probabilities, which are greater than (np)/n, where np is greater than 1. Under this condition, the graph will be almost sure to have a GCC.  
The theoretical value of the average degree is equal to the total number of nodes times the probability.  

Mean(p=0.003) = 1000 * 0.003 = 3, which is approximate equal to the empirical mean, 3.01, with 3.33% difference.  
Mean(p=0.004) = 1000 * 0.004 = 4, which is approximate equal to the empirical mean, 3.938, with 1.55% difference.  
Mean(p=0.01) = 1000 * 0.01 = 10, which is approximate equal to the empirical mean, 10.13, with 1.3% difference.  
Mean(p=0.05) = 1000 * 0.05 = 50, which is approximate equal to the empirical mean, 49.85, with 0.30% difference.  
Mean(p=0.1) = 1000 * 0.1 = 100, which is approximate equal to the empirical mean, 99.49, with 0.51% difference.  
As for variance, the distribution is binomial distribution, meaning the variance is np(1-p).  
Var(p=0.003) = 1000 * 0.003 * (1 - 0.003) = 2.991, similar to the empircal value, 3.181, with 6.35% difference.  
Var(p=0.004) = 1000 * 0.004 * (1 - 0.004) = 3.984, similar to the empircal value, 4.091, with 2.69% difference.  
Var(p=0.01) = 1000 * 0.01 * (1 - 0.01) = 9.9, similar to the empircal value, 9.622, with 2.81% difference.  
Var(p=0.05) = 1000 * 0.05 * (1 - 0.05) = 47.5, similar to the empircal value, 45.001, with 5.26% difference.  
Var(p=0.1) = 1000 * 0.1 * (1 - 0.1) = 90, similar to the empircal value, 96.160, with 6.84% difference.

### (b)
For p = 0.003 and p = 0.004, the graphs are disconnected. The probability for generating a connected graph for p = 0.003 and p = 0.004 are 0, when repeat generating graphs 100 times. That for p = 0.01 is 0.92. And the probabilities for p = 0.05 and p = 0.1 are 1.  
For p = 0.003, the diameter of the GCC is 16.
For p = 0.004, the diameter of the GCC is 10.
For p = 0.01, the diameter of the GCC is 5.
For p = 0.05, the diameter of the GCC is 3.
For p = 0.1, the diameter of the GCC is 3.

### (c)
![normalized GCC vs. p](./plots/wang/1_1_6.png)
We set the p from 0.1 times (ln(1000)/1000), which is 0.0006, to 2 times (ln(1000)/1000), which is 0.0138, with a step size of 0.05 times (ln(1000)/1000), which is 0.0003. We plot the normalized average GCC size of 100 repititions versus the probability p.  
From the graph, we could empirically estimate that giant connected component starts to emerge at around 0.0066. Theoretical value is 0.0069 so the estimation matches with it. The criterion of emergence is that the curve starts to become flat, meaning the derivative gradually approach to 0. When the curve becomes completely flat, it reaches steady state, meaning the graph is connected. 

### (d)
#### (i)
![GCC size vs. p, c=0.5](./plots/wang/1_1_7.png)
![GCC size vs. n, c=0.5](./plots/wang/1_1_8.png)
With higher edge formation probability, the size of GCC decreases. Though this looks counter-intuitive at the first glance, this actually makes sense. For all the graph sitting at the left end of x axis, they all have large numbers of nodes. Therefore, the GCC size respective its own size are much smaller comparing to the graph sitting at the right end of the graph, whose size is much smaller. And since p=c/n, for a fixed c, the smaller the number of nodes is, the higher the probability of edges forming.   
From the second graph, we can see the sizes of majority GCC are ranging from 10 to 20. Although increasing number of nodes does raise the size of GCC at the beginning, it does not affect a lot in the late phase. 

#### (ii)
![GCC size vs. p, c=1](./plots/wang/1_1_9.png)
![GCC size vs. n, c=1](./plots/wang/1_1_10.png)
For the graph with GCC size vs. probability, the trend is the similar to the previous one. However, the maximum size of GCC is way higher than that of c = 0.5. The second graph is different from the previous one. With number of nodes increases, the GCC size actually increases, rather than keeping in a certain range. And the dots are more spreaded out. This might imply that the connected components in the graphs are more than those in the graph with c = 0.5, leading to larger GCC. 

#### (iii)
![GCC size vs. p, c=1.1, 1.2, 1.3](./plots/wang/1_1_11.png)
![GCC size vs. n, c=1.1, 1.2, 1.3](./plots/wang/1_1_12.png)
The first graph still looks similar to the previous ones, except the size is much larger. However, the second graph is much different. For c=1.1, the dots look similar to that of c=1.0, with larger size of GCC. They are still quite spreaded out with higher number of nodes. The interesting part is that for c=1.1 and c=1.2, the dots are much more confined. That might imply that the graphs are connected. 
## Problem 2
### (a) 
By definition of preferential attachment model, the graph will always be connected since a node always choose a node  ii  with  degree(i)degree(i)  >= 1 and construct an edge with it. Therefore, the newly inserted node will always be connected with the graph.

![alt text](./plots/linzuo/1_2_a_1.png)
### (b)
Modualrity is 0.9327325

### (c)
Modularity is 0.9759, It did not change dramatically since the overall graph strucutre is determined by the same generative model. The modularity increased since later generated nodes are less likely to be connected.
 
### (d)

![alt text](./plots/linzuo/1_2_d_1.png)
![alt text](./plots/linzuo/1_2_d_2.png)

Slope is rooughly 0.025

### (e)

![alt text](./plots/linzuo/1_2_e_1.png)

The degree distribution of the subgraph is very similar to its parent graph. Since the subgraph is randomly sampled and the empirical distribution should be similar to its parent graph.

### (f)

We can tell from the graph that the number of degress is closely related to the age of nodes. This is one of the most important chracteristics of preferential attachment model. There is a spike at ages = 1000, showing that the generative model strickly favors starting nodes. 

![alt text](./plots/linzuo/1_2_f_1.png)

### (g) 
### m=2

The modularity is 0.52540327767565 with n= 1000, m=2
The modularity is 0.52853133625893 with n= 10000, m=2

Modularity increases as the number of selected node per iteration increases. 
Since modularity represents the strenths of dividing network into submodules, larger m will always result in a more densly connected graph. So the modularity of m=1 is high.

![alt text](./plots/linzuo/1_2_g_1.png)
![alt text](./plots/linzuo/1_2_g_2.png)
![alt text](./plots/linzuo/1_2_g_3.png)
![alt text](./plots/linzuo/1_2_g_4.png)

#### m = 5

![alt text](./plots/linzuo/1_2_g_5.png)
![alt text](./plots/linzuo/1_2_g_6.png)
![alt text](./plots/linzuo/1_2_g_7.png)
![alt text](./plots/linzuo/1_2_g_8.png)

### (h)

Both procedures will be able to generate PA models. However, the stub matching models do
not generate edges during the construction process. Instead, it randomly matches with 
other nodes regardless of current degree

![alt text](./plots/linzuo/1_2_h_1.png)
![alt text](./plots/linzuo/1_2_h_2.png)


>>>>>>> 0091231f2bb92b70488ed7ac3402fd850637b111
## Problem 3
### (a)
The degree distribution of the network is as below.  
![degree distribution](./plots/liang/1.png)  
Fit the distribution to power law and get the result exponent is **4.68233571652074**. Details are as below.  
* continuous: FALSE  
* alpha: 4.68233571652074
* xmin: 4  
* logLik: -145.530949783814  
* KS.stat: 0.0345632541890962  
* KS.p: 0.99926736466248.  

### (b)
Use fast greedy method to find the community structure. The community sizes are: **43, 45, 45, 44, 41, 42, 42, 44, 38, 42, 33, 33, 37, 33, 34, 35, 34, 34, 30, 33, 29, 29, 27, 27, 25, 23, 21, 19, 19, 19**. And the modularity is **0.935616296977663**.





# Part 2  
## Problem 1  

### (b)

We calcualted the mean and variance using a 50 step randome and 10 repeatitions per step size for variance and mean. The relationship is shown below. It seems to converge as the t grows

![alt text](./plots/linzuo/2_1_b_1.png)
![alt text](./plots/linzuo/2_1_b_2.png)

### (c) 

The result of random walk is very similar to the degree distribution of the graph. Since random walk depends on the structure of the orginal graph and thus has similar degree distribution


![alt text](./plots/linzuo/2_1_c_1.png)
![alt text](./plots/linzuo/2_1_c_2.png)

### (d)

When n == 100, with a step size of 50

![alt text](./plots/linzuo/2_1_d_3.png)
![alt text](./plots/linzuo/2_1_d_4.png)


## Problem 2  
### (b)  
![average distance for n=1000](./plots/wang/2_2_1.png)  
![variance of distance for n=1000](./plots/wang/2_2_2.png)  
The average distance graph seems converge around 1500 steps with the average distance about
8 while the variance graph still fluctuates even for 2000 steps.  
### (c)  
![degree distribution](./plots/wang/2_2_3.png)  
From this graph, it is quite clear that the degree distribution for random walk is similar to that of the original graph. 
Since random walk is like doing random sampling from the original graph, the result is in expectation.  
### (d)  
![average distance for n=100](./plots/wang/2_2_4.png)  
![variance of distance for n=100](./plots/wang/2_2_5.png)  
![average distance for n=10000](./plots/wang/2_2_6.png)  
![variance of distance for n=10000](./plots/wang/2_2_7.png)  
Comparing to those three sets of graphs, we can see that with higher number of nodes, the convergence will take more steps. 
The plots with number of node equal to 100, it converge quite easily, at around 300. With 1000 nodes, the curve converges at around 1700 steps. 
With 10000 nodes, the curve does not even look like converge at step 2000. With higher number of nodes, the diameter of the network is also higher. 
Therefore, the higher the diameter of a network is, the longer it will take for the average distance and the variance of distance of random walks to converge.

## Problem 3 
### (a) 
Generate the network and simulate random walk on the network. Measure the visit probability of each node and calculate the the relationship between the visit probabilty and the degree distribution. The results are as below. And we can see that the visit probability is highly related to the in-degree of the nodes.  
* Correlation between in-degree and visit probability:  **0.532488**   
* Correlation between out-degree and visit probability:  **-0.7304185**   
* Correlation between total-degree and visit probability:  **0.5299272**   
![degree distribution](./plots/liang/2.png)  
![degree distribution](./plots/liang/3.png)  
![degree distribution](./plots/liang/4.png)  

### (b)
Perform random walk with a teleportation probability of 0.15. The result visit probability is more distributed than the one shown in 3(a), though it's still highly related to the in-degree of the nodes.  
* Correlation between in-degree and visit probability:  **0.6149209**   
* Correlation between out-degree and visit probability:  **-0.7949347**   
* Correlation between total-degree and visit probability:  **0.6123663**   
![degree distribution](./plots/liang/5.png)  
![degree distribution](./plots/liang/6.png)  
![degree distribution](./plots/liang/7.png)  


## Problem 4

### (a)
When using teleportation based on PageRank, random jump will favor nodes with high PageRank values. Different from the result in 3b, which uses random jump with uniform distribution over all pages, the result in this problem is more likely to land onto vertices with high page rank values, like the first few nodes.The distribution becomes more concentrated in this case due to the random jump probability being affected by initial PageRank obtained from 3b  

![alt text](./plots/linzuo/2_4_a_1.png)
![alt text](./plots/linzuo/2_4_a_2.png)

Correlation between in-degree and PageRank is 0.3630926 

### (b)
After setting the favorite page to two medians, the PageRank of these two pages greatly increased. Other pages PageRank decreased significantly due to the biased random jump probability.

### (c)

Let's consider the normal PageRank equation,

 $$ Pr(A) = \frac{(1 - d)}{N} + d\sum_{T_in} \frac{Pr(T_in)}{C(T_in)}$$

, where  Pr(A) is the PageRank of page  A, d is the damping factor, $N$ is the total number of pages or nodes, $T_in$ is the set of nodes which has an edge directed to $A, C(T_in)$ is the number of edges of$ T_in$.

To take into account the effect of user's self-reinforcement, we can change the teleportation probability from  $\frac{1}{N} $to a number which reflects users' interest or trust on site  A.

