# ECE 232E Spring 2018 - Project 2

### Linzuo Li (604944917)

### Haoran Wang (505029637)

### Liang Qiu (704725636)

### Yan Huang (404759425)



# 1. Facebook network

## 1.1

### Question 1

Yes, the facebook network is connected.

### Question 2

The diameter of the network is 8.

### Question 3

The degree distribution is as follow. The average degree distribution is 43.69101.

![degree distribution p=0.003](./plots/liang/3-1.png)

### Question 4

The degree distribution and the fit line in a log-log scale is as follow.

![degree distribution p=0.003](./plots/liang/4-1.png)

The estimated slope of the fit line is $$ -1 \times 10^{-4}$$.

## 1.2

### Question 5

Number of nodes: 348

Number of edges: 2866

![degree distribution p=0.003](./plots/linzuo/5-1.png)

### Question 6

Diameter of the graph is: 2

In a personalized network, the trivial lower bound is 1, all neighbors are connected (fully connected graph). The trivial upper bound is 2, at least two neighbors of the core node is not connected. So the path between these two nodes will contain the core node, resulting a path of length 2.

### Question 7

**Upper bound = 2 :**  The person has at least two friends that do not know each other.

**Lower bound = 1 :**   The person's friends all know each other.

## 1.3.1

### Question 8

There are 40 core nodes in the Facebook network. The average degree of them is 279.375.

### Question 9

Community structure analysis using different community detection algorithms.

* ##### Node ID 1

  **Fast-Greedy modularity: ** 0.4131014

![degree distribution p=0.003](./plots/liang/9-1.png)

  **Edge-Betweenness modularity: ** 0.3533022

![degree distribution p=0.003](./plots/liang/9-2.png)

  **Infomap modularity:** 0.3891185

![degree distribution p=0.003](./plots/liang/9-3.png)

* ##### Node ID 108
  **Fast-Greedy Modularity:** 0.4359294

![degree distribution p=0.003](./plots/liang/9-4.png)

  **Edge-Betweenness:** 0.5067549

![degree distribution p=0.003](./plots/liang/9-5.png)

  **Infomap modularity:** 0.5082492

![degree distribution p=0.003](./plots/liang/9-6.png)

* ##### Node ID 349
  **Fast-Greedy Modularity:** 0.2517149

![degree distribution p=0.003](./plots/liang/9-7.png)

  **Edge-Betweenness:** 0.133528

![degree distribution p=0.003](./plots/liang/9-8.png)

  **Infomap modularity:** 0.203753

![degree distribution p=0.003](./plots/liang/9-9.png)

* ##### Node ID 484
  **Fast-Greedy Modularity:** 0.5070016

![degree distribution p=0.003](./plots/liang/9-10.png)

  **Edge-Betweenness:** 0.4890952

![degree distribution p=0.003](./plots/liang/9-11.png)

  **Infomap modularity:** 0.5152788

![degree distribution p=0.003](./plots/liang/9-12.png)

* ##### Node ID 1087
  **Fast-Greedy Modularity:** 0.1455315

![degree distribution p=0.003](./plots/liang/9-13.png)

  **Edge-Betweenness:** 0.02762377

![degree distribution p=0.003](./plots/liang/9-14.png)

  **Infomap modularity:** 0.02690662

![degree distribution p=0.003](./plots/liang/9-15.png)

## 1.3.2

### Question 10

Community structure analysis after removing the core node.

Comparing to the the original networks, the new networks have higher
modularity. The reason is that after removing the core nodes, the edges
that connected the community through the core nodes are now dropped. Thus, every parts of the networks are more seperated, meaning higher modularities.

* ##### Node ID 1

  **Fast-Greedy modularity: ** 0.4418533

![degree distribution p=0.003](./plots/Haoran/Q10_1.png)

  **Edge-Betweenness modularity: ** 0.4161461

![degree distribution p=0.003](./plots/Haoran/Q10_2.png)

  **Infomap modularity:** 0.4180077

![degree distribution p=0.003](./plots/Haoran/Q10_3.png)

* ##### Node ID 108
  **Fast-Greedy Modularity:** 0.4581271

![degree distribution p=0.003](./plots/Haoran/Q10_4.png)

  **Edge-Betweenness:** 0.5213216

![degree distribution p=0.003](./plots/Haoran/Q10_5.png)

  **Infomap modularity:** 0.5185969

![degree distribution p=0.003](./plots/Haoran/Q10_6.png)

* ##### Node ID 349
  **Fast-Greedy Modularity:** 0.2456918

![degree distribution p=0.003](./plots/Haoran/Q10_7.png)

  **Edge-Betweenness:** 0.1505663

![degree distribution p=0.003](./plots/Haoran/Q10_8.png)

  **Infomap modularity:** 0.2465785

![degree distribution p=0.003](./plots/Haoran/Q10_9.png)

* ##### Node ID 484
  **Fast-Greedy Modularity:** 0.5342142

![degree distribution p=0.003](./plots/Haoran/Q10_10.png)

  **Edge-Betweenness:** 0.5154413

![degree distribution p=0.003](./plots/Haoran/Q10_11.png)

  **Infomap modularity:** 0.5434437

![degree distribution p=0.003](./plots/Haoran/Q10_12.png)

* ##### Node ID 1087
  **Fast-Greedy Modularity:** 0.1481956

![degree distribution p=0.003](./plots/Haoran/Q10_13.png)

  **Edge-Betweenness:** 0.0324953

![degree distribution p=0.003](./plots/Haoran/Q10_14.png)

  **Infomap modularity:** 0.02737159

![degree distribution p=0.003](./plots/Haoran/Q10_15.png)

## 1.3.3

### Question 11

Given node i, the embeddedness of node i is equal to $Deg(i) - 1$. Because core node neighbors are all in the network. The neighbors of a node - 1 is the number of friends of node i except the core node.

### Question 12

During our calculation, we found that certain nodes are not connected to each other and thus an "inf" was used by igraph's distance matrix to represent a disconnected path. As a result, we replaced it with a constant value c = 5 (5 > diameter) so only numeric values are considered and disconnected path distance is taken into consideration.

![degree distribution p=0.003](./plots/linzuo/12-1.png)
![degree distribution p=0.003](./plots/linzuo/12-2.png)
![degree distribution p=0.003](./plots/linzuo/12-3.png)
![degree distribution p=0.003](./plots/linzuo/12-4.png)
![degree distribution p=0.003](./plots/linzuo/12-5.png)
![degree distribution p=0.003](./plots/linzuo/12-6.png)
![degree distribution p=0.003](./plots/linzuo/12-7.png)
![degree distribution p=0.003](./plots/linzuo/12-8.png)
![degree distribution p=0.003](./plots/linzuo/12-9.png)
![degree distribution p=0.003](./plots/linzuo/12-10.png)

The general trend is that, dispersion will increase as the number of embeddedness increases. Most of nodes tend to have few embeddedness and dispersion.  

### Question 13

We applied Fast-Greedy algorithms to find Community structure which is shown in below plots, represented by different colors. The node with maximum dispersion is highlighted with red incident edges. Core node is also enlarged for clarity. We try to change the node color to show our core node and maximum dispersion node. However, it seems that the community color seems to be overwriting our color settings for these two individual nodes. We cannot find a work around but this should not affect the graph in general.

![degree distribution p=0.003](./plots/linzuo/13-1.png)

Maximum dispersion of core:1 is ID: 57

![degree distribution p=0.003](./plots/linzuo/13-2.png)

Maximum dispersion of core:1 is ID: 1889

![degree distribution p=0.003](./plots/linzuo/13-3.png)

Maximum dispersion of core:1 is ID: 377

![degree distribution p=0.003](./plots/linzuo/13-4.png)

Maximum dispersion of core:1 is ID: 108

![degree distribution p=0.003](./plots/linzuo/13-5.png)

Maximum dispersion of core:1 is ID: 108


### Question 14

We highlighted our core node with white color. Personal network along with nodes with maximum embeddedness and dispersion/embeddedness ratio are shown in the below graph. Maximum dispersion is highlighted in red and maximum d/e ratio is highlighted in green. If the nodes share the same ID, it is highlighted with purple in this graph.

![degree distribution p=0.003](./plots/linzuo/14-1.png)

Maximum embeddedness of core:1 is ID: 57

Maximum dispersion/embeddedness ratio of core:1 is ID: 26

![degree distribution p=0.003](./plots/linzuo/14-2.png)

Maximum embeddedness of core:1 is ID: 1889

Maximum dispersion/embeddedness ratio of core:1 is ID: 1889

![degree distribution p=0.003](./plots/linzuo/14-3.png)

Maximum embeddedness of core:1 is ID: 377

Maximum dispersion/embeddedness ratio of core:1 is ID: 377

![degree distribution p=0.003](./plots/linzuo/14-4.png)

Maximum embeddedness of core:1 is ID: 108

Maximum dispersion/embeddedness ratio of core:1 is ID: 108

![degree distribution p=0.003](./plots/linzuo/14-5.png)

Maximum embeddedness of core:1 is ID: 108

Maximum dispersion/embeddedness ratio of core:1 is ID: 108

### Question 15

#### Dispersion：
From the plots we obtained, we can see that, nodes with highest dispersion is usually in the same community with the
core node. Dispersion seems to be proportional to the number embeddedness of the node, which intuitively makes since
because of the definition of embeddedness which depends on the number of mutual friends a node shares with the core node. Nodes in the same community with the core node usually shares more mutual friends with the core node resulting high dispersion.

#### Embeddeness:
By definition, embeddedness is the number of mutual friends a node shares with the core node. From the plotted graphs, we can observe that, nodes with large embeddedness always shares the same largest community with the core node.

#### Dispersion/Embeddeness:
Dispersion measures the distances between pairs of nodes without the core node and the node being calculated. A high dispersion/embeddedness ratio represents that the core node and the node of interests have mutual friends that would not be acquainted without these two nodes. So it is interesting to guess that this maximum node could have a special relationship with the core node.

## 1.4

### Question 16

The $|N_{r}|$ is 11.

### Question 17

The average accuracy of the three recommendation algorithm:

* Common Neighbors measure: 0.3927227
* Jaccard measure: 0.1457471
* Adamic Adar measure: 0.1773167

So according to my experiment results, the Common Neighbors measure is the best.

# 2. Google+ network

### Question 18

The number of personal networks are 57.

### Question 19

All those distributions show similar trends. For the outward degree distributions, all the three show that there are almost no nodes with high outward degree, for example with degree higher than 200. However, the first two have more nodes with outward degree less than 50 than that of the last one. For the inward degree distribution, the curves have the similar shapes and the only difference is the number of nodes of each graphs. The last one has more nodes than the previous two graphs.

* ##### Node ID: 109327480479767108490

![degree distribution](./plots/Haoran/Q19_1.png)
![degree distribution](./plots/Haoran/Q19_2.png)

* ##### Node ID: 115625564993990145546

![degree distribution](./plots/Haoran/Q19_3.png)
![degree distribution](./plots/Haoran/Q19_4.png)

* ##### Node ID: 101373961279443806744

![degree distribution](./plots/Haoran/Q19_5.png)
![degree distribution](./plots/Haoran/Q19_6.png)

## 2.1

### Question 20

The modularities of those three are different. The last one is more connected than the previous two and those two are similar, with similarity 0.184.

* ##### Node ID: 109327480479767108490
Modularity: 0.2527654

![degree distribution](./plots/Haoran/Q20_1.png)

* ##### Node ID: 115625564993990145546
Modularity: 0.3128763

![degree distribution](./plots/Haoran/Q20_2.png)

* ##### Node ID: 101373961279443806744
Modularity: 0.1638597

![degree distribution](./plots/Haoran/Q20_3.png)

### Question 21

higher homogeneity indicates the circles in the community are of the same type; higher completeness indicates the community comprise many different types of circles

### Question 22
$h1$ is around 0.21, $c1$ is around 0.33.  
$h2$ is around 0.48, $c2$ is around -3.53.  
$h3$ is around 0.006, $c3$ is around -1.55.  
$H(C)$ indicates the chaos of circle system of the network. If the network has more numbers of circles, $H(C)$ or say the chaos is higher;
$H(k)$ indicates the chaos of community system of the network. If the network has more numbers of communities, $H(K)$ or say the chaos is higher.  
$H(C|K)$ indicate how the circles are distributed in different communities. If more people with same circle information are in the same community, $H(C|K)$ is lower.  
$H(K|C)$ indicate how the communities are distributed in different circles. If more people with same community information are in the same circle, $H(C|K)$ is lower.
