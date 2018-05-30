import re
import csv
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("input", help="input file name",
                    type=str)
parser.add_argument("output", help="output file name",
                    type=str)
args = parser.parse_args()


with open( args.input + 'actor_movies.txt', 'r', encoding = "ISO-8859-1") as f:
    data = f.readlines()
p = re.compile(r'\((\d{4}|\?\?\?\?)(\)|/[a-zA-Z]*\))')

with open( args.output, "w+") as f:
    for line in data:
        temp = line.split('\t\t')
        if len(temp) <= 1:
            continue
        actor = temp[0]
        movies = []
        for i in range (1, len(temp)):
            movie = temp[i]
            if p.search(movie) != None :
                movies.append(movie[:p.search(movie).end()])
            movies = list(set(movies))
        if len(movies) < 10:
            continue
        str_movies = '\t\t'.join(movies)
        f.write(actor + '||')
        f.write(str_movies + "\n")

with open( args.input + 'actress_movies.txt', 'r', encoding = "ISO-8859-1") as f:
    data = f.readlines()
p = re.compile(r'\((\d{4}|\?\?\?\?)(\)|/[a-zA-Z]*\))')

with open( args.output, "a") as f:
    for line in data:
        temp = line.split('\t\t')
        if len(temp) <= 1:
            continue
        actor = temp[0]
        movies = []
        for i in range (1, len(temp)):
            movie = temp[i]
            if p.search(movie) != None :
                movies.append(movie[:p.search(movie).end()])
            movies = list(set(movies))
        if len(movies) < 10:
            continue
        str_movies = '\t\t'.join(movies)
        f.write(actor + '||')
        f.write(str_movies + "\n")