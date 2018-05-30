import re
import csv
import argparse
from movie_dict import MD

parser = argparse.ArgumentParser()
parser.add_argument("input", help="input file name",
                    type=str)

args = parser.parse_args()


args = parser.parse_args()

with open( args.input, 'r', encoding = "ISO-8859-1") as f:
    data = f.readlines()

movie_length = []

for line in data:
    temp = line.split('||')
    movie_length.append(len(temp[2].split('\t\t')))


movie_dict = MD()

edge_dict = {
}

for key in movie_dict:
    actors = movie_dict[key]
    for i in range(len(actors)):
        for j in range(i+1,len(actors)):
            act_i = actors[i]
            act_j = actors[j]
            len_i = movie_length[act_i]
            len_j = movie_length[act_j]
            if (act_i,act_j) in edge_dict:
                weights= edge_dict[(act_i,act_j)]
                edge_dict[(act_i,act_j)] = (weights[0]+1/len_i,weights[1]+1/len_j)
            else:
                edge_dict[(act_i,act_j)] = (1/len_i,1/len_j)

with open( '../output/edge_list.txt', "w+") as f:
    for key in edge_dict:
        act_i = key[0]
        act_j = key[1]
        weights = edge_dict[key]
        weight_i = weights[0]
        weight_j = weights[1]

        f.write("%d\t%d\t%f\n"%(act_i,act_j,weight_i))
        f.write("%d\t%d\t%f\n"%(act_j,act_i,weight_j))