import matplotlib.pyplot as plt
import numpy as np

with open('../data/movie_rating.txt', 'r', encoding='ISO-8859-1') as f:
    movie_rating = f.readlines()
    rates = {}
    for line in movie_rating:
        temp = line.split('\t\t')
        rates[temp[0]] = float(temp[1].split('\n')[0])

with open('../output/movie_dict.txt', 'r') as f:
    movie_dict = f.readlines()
    movies = []
    for line in movie_dict:
        temp = line.split('||')
        movies.append(temp[1])

communities = [0] * len(movies)
with open('../output/community.txt', 'r') as f:
    community = f.readlines()
    i = 0
    for line in community:
        temp = line.split(' ')
        for t in temp:
            communities[int(t)] = i
        i += 1

with open('../output/movie_edge_list.txt', 'r') as f:
    movie_edge_data = f.readlines()

    for movie in [10062, 26989, 85671]:
        neighs = []
        rates_neigh = []
        for line in movie_edge_data:
            temp = line.split('\t')
            if temp[0] == '\n':
                continue
            if int(temp[0]) == movie:
                neigh = movies[int(temp[1])]
                if communities[int(temp[1])] == communities[movie]:
                    neighs.append(neigh)
                    if neigh in rates:
                        rates_neigh.append(rates[neigh])
            if int(temp[1]) == movie:
                neigh = movies[int(temp[0])]
                if communities[int(temp[0])] == communities[movie]:
                    neighs.append(neigh)
                    if neigh in rates:
                        rates_neigh.append(rates[neigh])
        # the histogram of the data
        n, bins, patches = plt.hist(rates_neigh)
        plt.xlabel('Rating')
        plt.ylabel('Frequency')
        plt.show()
        print('Average rating of neighbors:', np.average(rates_neigh))

