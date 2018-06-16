# ECE 232E Spring 2018 - Project 5

### Linzuo Li (604944917)

### Haoran Wang (505029637)

### Liang Qiu (704725636)

### Yan Huang (404759425)


# 1. Stock Market 

## 1.1 Return correlation

### Question 1

$|p_{ij}| \leq 1$

This can be proved using Cauchy-Schwarz Inequality, According to the inequality, we have 
$$
|cov(X,Y)| \leq \sigma(X)\sigma(Y) 
$$
We are given
$$
p_{ij} = \frac{<r_ir_j>-<r_i><r_j>}{\sqrt{(<r_i^2> - {<r_i>}^2)(<r_j^2> - {<r_j>}^2)}}
$$
The numerator is:
$$
<r_ir_j>-<r_i><r_j> = cov(r_i, r_j)
$$
The denominator is:

$$
\sqrt{(<r_i^2> - {<r_i>}^2)(<r_j^2> - {<r_j>}^2)} = \sigma(r_i)\sigma(r_j)
$$

Therefore, we can see that $|p_{ij}| \leq 1$ so $|p_{ij}|$ has an upper bound of 1 and lower bound of -1



The use of Log normalization term removed the denominator $p_i(t − 1)$ so the log-normalized return is only related to the ratio of price at these two different period. In addtion, using log provides a effect of diminishing return by reducing the magnitude of large values and kept the range of $r_i$ > 0.

## 1.2 Return correlation

### Question 2

![c1](./plots/Q2_1.png)

Because $|p_ij|$ <= 1, the edge weight has a range between 0 and 2. From the above degree distribution plot, we can see that most of the edges has a weight of 1~1.5.  
## 1.3 Minimum Spinning Tree

### Question 3

![c1](./plots/Q2_2.png)

From the plot of the vine cluster, we can see that most of the stocks of the same sector (indicated by same color) are in the same community of the minimum spanning tree. The weight of edges is inversely propotional to the correlation. So stocks with high correlation will have small edges weights between them. During to the nature of minimum spanning tree, the tree is construected to reduce the total edge weight values. As a result, stocks with the same sector (accordingly with high correlations) will have their edges preserved and this is observed in the graph.

In additon, the stocks sectors with green and blue color are very exclusive. There is minimum number of other sectors within both the blue and green sector. This shows that stock in these two sectors shows very strong correlations within each other and low correlation with other sectors.

On the contrarary, stock sectors colored orange and grey are often mixed within each other. This shows that these two sectors share many similarities and thus their stocks have similar correlation value.

## 1.4 Sector clustering in MST’s

### Question 4

$\alpha_1$= 0.821755109099061

$\alpha_2$= 0.114565238702088

The first case assumes the probability of a node having a particular sector depends on the sector of neighbors. Because the minimum spanning tree is constructed in a way that neighboring nodes are stocks with high correlation values and thus high probability of being the same sector. The first $\alpha$ has relatively large value compared to $\alpha_2$. 

## 1.5 Correlation graphs for weekly data

### Question 5

![c1](./plots/Q5_1.png)
![c1](./plots/Q5_2.png)

The weekly vine cluster shows a less consitant sector distribution in terms of neighboring nodes. There are community where has many different clusters. We concluded that this is due to the temporal difference between weekly and daily stock close prices. From the finance point of view, weekly prices, in a long term, are more affected by entire market trends and many stocks of different sectors share similarities in weekly close prices.
# 2. Let’s Help Santa!

## 2.2 Build Your Graph

### Question 6

There are 1880 nodes in the cleaned graph G and 311802 edges. 

## 2.3 Traveling Salesman Problem

### Question 7

We randomly picked up some edges from the minimum spanning tree and check the street name of all the end nodes. Movement_id 828 and movement_id 1624 formed an edge. Their addresses are 4200 Amargosa Drive, Antioch and 2900 Roosevelt Lane, Antioch, respectively. ID 1484 and ID 1550 formed an edge. Their addresses are 29300 Lassen Street, Tennyson - Alquire, Hayward and 30800 San Clemente Street, Hayward. ID 2523 and ID 2149 formed an edge. Their addresses are 3300 Rocky Mountain Drive, Alum Rock, San Jose and 2200 Vista Verde Drive, East San Jose, San Jose. As we can see, those two nodes that connected with each other are all in the same area, which makes sense since people usually do not travel far via Uber. 

### Question 8

We randomly picked 1000 triangles and the percentage was about 92%. 

### Question 9

We started the algorithm at root node with movement_id 1938. The approximate TSP cost vs. the optimal cost is around 1.572. 

### Question 10

**The trajectory graph starting at node 1938**
![trajectory](plots/Q10.png)

# 3. Analysing the Traffic Flow

## 3.1 Estimate the Roads

### Question 11

Here is the road mesh I obtained. I plotted using the real coordinates so it's similar to the real road map, where you can tell the bay area, etc.

![trajectory](plots/Q11_1.png)

And this is the $$G_\Delta$$ whose nodes are different locations and whose edges are produced by *Delaunay Triangulation*.

![trajectory](plots/Q11_3.png)

## 3.2 Calculate Road Traffic Flows

### Question 12

![trajectory](plots/Q12.png)

## 3.3 Calculate the Max Flow
### Question 13

The maximum flow from Stanford to UCSC is about 29780 (cars/hour). And there are 5 edge-disjoint paths between the two spots. Here I mark the two spots with black color.

![trajectory](plots/Q13.png)

I can hardly tell how many edge-disjoint paths there are from the graph. But 5 is a reasonable number since  there are 6 edges departuring Stanford and 7 edges entering UCSC. Also, to calculate the maimum flow, I am not sure whether we should use capacity of 4 lanes (2 for each direction) or 2 lanes for one single direction for each edge. If we use the latter, then the maximum flow would be about 14890 (cars/hour). 

## 3.4 Defoliate Your Graph

### Question 14

Here is the histogram of the travel time of edges. 

![trajectory](plots/Q14_1.png)

We set the threshold travel time as 1200s and remove edges with travel time beyond that. The resulting graph is as follow. 

![trajectory](plots/Q14_2.png)

Notice the given real bridges' end points are marked with different colors as blue. They are still preserved when using the threshold of 1200s. (There exists some negligible errors between given bridges' coordinates and the original nodes' coordinates.)

![trajectory](plots/Q14_3.png)

### Question 15

Repeat Question 13, get the same maximum flow as about 29780 cars/hour (14890 cars/hour if use single direction capacity). And there are still 5 edge-disjoint paths between the two spots. Since we were supposed to only remove the fake edges, this shouldn't have any influence.

