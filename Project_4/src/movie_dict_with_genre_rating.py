import argparse

paser = argparse.ArgumentParser()
paser.add_argument('movie', help='movie file', type=str)
paser.add_argument('genre', help='genre file', type=str)
# paser.add_argument('rating', help='rating file', type=str)
paser.add_argument('output', help='output file', type=str)
args = paser.parse_args()

data = None
with open(args.movie, 'r', encoding='ISO-8859-1') as f:
    data = f.readlines()

movie_dict = {}
for line in data:
    temp = line.split('||')
    ident = int(temp[0])
    movies = temp[2].split('\t\t')
    for movie in movies:
        if(movie in movie_dict):
            assert type(movie_dict[movie]) is list
            movie_dict[movie].extend([ident])
        else:
            movie_dict[movie] = [ident]

for movie in list(movie_dict):
    if(len(movie_dict[movie]) < 5):
        del(movie_dict[movie])

data = None
with open(args.genre, 'r', encoding='ISO-8859-1') as f:
    data = f.readlines()

genre_dic = {}
for line in data:
    temp = line.split('\t\t')
    genre_dic[temp[0]] = temp[1]

data = None
# TODO: add rating dictionary

err = open('../output/missing_match.txt', 'w+')
movie_id = 0
with open(args.output, 'w+') as f:
    for movie in movie_dict:
        f.write('%d||' % movie_id)
        movie_d = movie.replace('\n', '')
        f.write(movie_d + "||")
        if (movie_d in genre_dic):
            f.write(genre_dic[movie_d].replace('\n', '') + '||')
        else:
            err.write(str(movie_id) + '||' + movie_d + '\n')
        for i in range(len(movie_dict[movie]) - 1):
            f.write(str(movie_dict[movie][i]) + '\t\t')
        f.write(str(movie_dict[movie][-1]) + '\n')
        movie_id += 1
