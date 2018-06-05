# ECE 232E Spring 2018 - Project 4

### Linzuo Li (604944917)

### Haoran Wang (505029637)

### Liang Qiu (704725636)

### Yan Huang (404759425)


# 1. Actor/Actress network

### Question 1
The total number of actors and actress is 113074. The total number of unique movies is 202483. 

## 1.1 Directed actor/actress network creation

### Question 2
![degree distribution of actor](./plots/Q2.png)
The in-degree distribution of the weighted actor/actress network. 

From the plot, we can clearly see the most people did not have any inward degree in that network. Even the highest peak has only around 0.0038. For the people have inward degree, most of them lay between 0 to around 1000. 

## 1.2 Actor pairings

### Question 3

Below we report the actor pairs and the weight for each pair. The actor pairs make sense.

* Tom Cruise - Nicole Kidman: 0.174603
* Emma Watson (II) - Daniel Radcliffe: 0.52
* George Clooney - Matt Damon: 0.119403
* Tom Hanks - Tim Allen (I): 0.101266
* Dwayne Johnson (I) - Steve Austin (IV): 0.205128
* Johnny Depp - Helena Bonham Carter: 0.081633
* Will Smith (I) - Darrell Foster: 0.102041
* Meryl Streep - Robert De Niro: 0.061856
* Leonardo DiCaprio - Martin Scorsese: 0.102041
* Brad Pitt - George Clooney: 0.098592


## 1.3 Actor rankings

### Question 4

Below we report the top 10 actors/actresses.

##### Name: number of movies, in-degree#####

Bess Flowers: 21023, 14922  
Sam Harris (II): 15467, 13702  
Harold Miller (I): 14563, 12922    
Fred Tatasciore: 10860, 7596  
Ron Jeremy: 16630, 5648  
Steve Blum (IX): 12472, 6418  
Jeffrey Sayre: 11108, 11982  
Kenner G. Kemp: 10815, 12104   
Franklyn Farnum: 14391, 11938   
Yuri Lowenthal: 9899, 5200  

No, none of them is listed in the previous section. Because most of them are senior actors/actresses and they acted in so many influential movies. People in our decade may not be familiar with them.

### Question 5

Below we report the actors/actresses in the Question 3.

##### Name: pagerank score, number of movies, in-degree 
Tom Cruise: 1.618891e-05, 1712, 1974  
Emma Watson (II): 1.692606e-05, 943, 866  
George Clooney: 2.754246e-05, 1887, 3060  
Tom Hanks: 3.426885e-05, 2101, 4014  
Eddie Johnson (I): 1.120852e-05, 309, 1070  
Johnny Depp: 3.393277e-05, 3132, 4152   
Will Smith (I): 2.457424e-05, 1249, 2460  
Meryl Streep: 2.483367e-05, 2826, 3082  
Leonardo DiCaprio: 2.469046e-05, 1345, 2532  
Brad Pitt: 2.953705e-05, 1786, 3406  

# 2. Movie network

## 2.1 Undirected movie network creation

### Question 6

## 2.2 Communities in the movie network

### Question 6

### Question 7

1.
    ![c1](./plots/Q7_1.png)
    The most dominant genre in this community is Drama

2.
    ![c1](./plots/Q7_2.png)
    The most dominant genre in this community is Short
3.
    ![c1](./plots/Q7_3.png)
    The most dominant genre in this community is Documentary
4.
    ![c1](./plots/Q7_4.png)
    The most dominant genre in this community is Drama and Documentary
5.
    ![c1](./plots/Q7_5.png)
    The most dominant genre in this community is Adult
6.
    ![c1](./plots/Q7_6.png)
    The most dominant genre in this community is Documentary
7.
    ![c1](./plots/Q7_7.png)
    The most dominant genre in this community is Short
8.
    ![c1](./plots/Q7_8.png)
    The most dominant genre in this community is Musical
9.
    ![c1](./plots/Q7_9.png)
    The most dominant genre in this community is Short
10.
    ![c1](./plots/Q7_10.png)
    The most dominant genre in this community is Short
### Question 8

#### (a)
1. **Drama**
2. **Short**
3. **Documentary**
4. **Drama and Documentary**
5. **Adult**
6. **Documentary**
7. **Short**
8. **Musical**
9. **Short**
10. **Short**

The most dominant genre out of these 10 communities is Drama.
#### (b)

1. **Family**, score: 43.70
2. **Short**, score: 9.53
3. **Romance**, score: 58.36
4. **History**, score: 28.22
5. **Adult**, score: 69.64
6. **Adventure**, score: 75.70
7. **Romance**, score: 2.49
8. **Musical**, score: 248.8
9. **Short**, score: 5.59
10. **Short**, score: 9.54


The most dominant genre calculated using the scoring function are different from the most frequenty genre by coount. The reason is that, the normalization used in the scoring function removes the bias. For exmple, Drama is usually a very dominant genre. So many movies in the community have the same Drama genre. Therefore, it is not intuitive to compare the count directly. So the scoring function is a better indication of the dominant genre since the frequency is normalized. 

#### (c)
 ![c1](./plots/Q7_11.png)
    In terms of frequency, the four genre share the same count. The most dominant genre in this community is Short and the score is 8.48

![c1](./plots/Q8c.png)




## 2.3 Neighborhood analysis of movies

### Question 9

* Batman v Superman: Dawn of Justice (2016); Rating: 6.6 
![c1](./plots/Q9_1.png)
Average rating of its neighbors: 6.375129533678757. They are similar.

* Mission: Impossible - Rogue Nation (2015); Rating: 7.4 
![c1](./plots/Q9_2.png)
Average rating of its neighbors: 6.23, which is not similar to 7.4.  

* Minions (2015); Rating: 6.4
![c1](./plots/Q9_3.png)
Average rating of its neighbors: 6.815773353751914, which is similar.

### Question 10

Restrict the neighborhood to consist of movies from the same community.

* Batman v Superman: Dawn of Justice (2016); Rating: 6.6 
![c1](./plots/Q10_1.png)
Average rating of its neighbors: 6.340969162995596. 

* Mission: Impossible - Rogue Nation (2015); Rating: 7.4 
![c1](./plots/Q10_2.png)
Average rating of its neighbors: 6.20275.  

* Minions (2015); Rating: 6.4
![c1](./plots/Q10_3.png)
Average rating of its neighbors: 7.210610079575596.

Unfortuantely, there is not a better match than Question 9.

### Question 11
Name: community ID
* Batman v Superman: Dawn of Justice (2016): 1
Star Wars: The Old Republic (2011): 7
Broadway: Beyond the Golden Age (2016): 1
Lennon or McCartney (2014): 1
Going to Pieces: The Rise and Fall of the Slasher Film (2006): 1
Iron Man 3 (2013): 1

* Mission: Impossible III (2006): 1
Star Wars: The Old Republic (2011): 7
Grand Theft Auto V (2013): 7
Lennon or McCartney (2014): 1
Spider-Man 3 (2007): 7
Pirates of the Caribbean: At World's End (2007): 7

* Minions (2015): 7
Transformers: Dark of the Moon (2011): 7
Star Wars: The Old Republic (2011): 7
Celebrity (1998): 1
Fainaru FantajÃ® XIII (2009): 7
Kingudamu hÃ¢tsu: BÃ¢su bai surÃ®pu (2010): 7

## 2.4 Predicting ratings of movies

### Question 12

We use three features in the model: the genre score as described in question 8, the actor score, which is the mean rating of the movies in which the actor participated in the community, and the director score, which is the mean rating of the movies that the director directed in the community. The root mean square error of our model is 0.82. According to our model, Batman v Superman: Dawn of Justice (2016) got 6.35; Mission: Impossible - Rogue Nation (2015) got 6.44 and Minions (2015) got 7.80.
### Question 13