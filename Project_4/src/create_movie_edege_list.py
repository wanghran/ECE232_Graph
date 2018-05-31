import re
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("movie_dict_path", help="movie dict path",
                    type=str)
parser.add_argument("output", help="outpath",
                    type=str)
args = parser.parse_args()

with open( args.movie_dict_path, 'r', encoding = "ISO-8859-1") as f:
    data = f.readlines()

movies = []

for line in data:
    temp = line.split('||')
    actors = temp[2].split('\t\t')
    movies.append(set(actors))

with open( args.output, "w+") as f:
    for i in range(len(movies)):
        for j in range(i+1, len(movies)):
            actors_i = movies[i]
            actors_j = movies[j]
            i_and_j = actors_i & actors_j
            if len(i_and_j) == 0:
                continue
            i_or_j = actors_i | actors_j
            weight = len(i_and_j) / len(i_or_j)
            f.write("%d\t%d\t%f\n"%(i,j,weight))
        progress = i*100/300000
        print('{:1f} % complete '.format(progress))
