import argparse

paser = argparse.ArgumentParser()
paser.add_argument('input', help='input file', type=str)
args = paser.parse_args()


def MD(input=args.input):
    data = None
    with open(args.input, 'r', encoding='ISO-8859-1') as f:
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

    return movie_dict
