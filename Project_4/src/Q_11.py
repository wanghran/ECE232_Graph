import matplotlib.pyplot as plt
import numpy as np
import operator

# with open('../data/movie_rating.txt', 'r', encoding='ISO-8859-1') as f:
#     movie_rating = f.readlines()
#     rates = {}
#     for line in movie_rating:
#         temp = line.split('\t\t')
#         rates[temp[0]] = float(temp[1].split('\n')[0])

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
        weights = {}
        for line in movie_edge_data:
            temp = line.split('\t')
            if temp[0] == '\n':
                continue
            if int(temp[0]) == movie:
                weights[int(temp[1])] = float(temp[2].split('\n')[0])
            if int(temp[1]) == movie:
                weights[int(temp[0])] = float(temp[2].split('\n')[0])
        sorted_weights = sorted(weights.items(), key=operator.itemgetter(1))
        top_5 = sorted_weights[0:4]
        print(top_5)
        for pair in top_5:
            print(movies[pair[0]], communities[pair[0]])