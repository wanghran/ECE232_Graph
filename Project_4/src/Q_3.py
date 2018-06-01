import re
import csv
import argparse


with open('../output/out.txt', 'r') as f:
    actor_data = f.readlines()

with open('../output/edge_list.txt', 'r') as f:
    edge_data = f.readlines()

    actors = []
    for line in actor_data:
        temp = line.split('||')
        actors.append(temp[1])

    actors_index = []
    for name in ["Cruise, Tom", "Watson, Emma (II)", "Clooney, George", "Hanks, Tom", "Johnson, Dwayne (I)",
                 "Depp, Johnny", "Smith, Will (I)", "Streep, Meryl", "DiCaprio, Leonardo", "Pitt, Brad"]:
        actors_index.append(actors.index(name))

    print(actors_index)

    weight = [0] * 10
    pair = [''] * 10

    for line in edge_data:
        temp = line.split('\t')

        step = 0
        for i in actors_index:
            if int(temp[0]) == i:
                w = float(temp[2])
                if w > weight[actors_index.index(i)]:
                    weight[actors_index.index(i)] = w
                    pair[actors_index.index(i)] = actors[int(temp[1])]

    print(pair)
    print(weight)



