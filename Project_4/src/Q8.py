import numpy as np
import matplotlib.pyplot as plt
import re

class Movie:
    def __init__(self, title, actors, genre):
        self.title = title
        self.actors = actors
        self.genre = genre 



with open('../data/movie_genre.txt', 'r', encoding = "ISO-8859-1",) as f:
    data = f.readlines()

genre_dict = {}
genre_count = {}
for line in data:
    title = line.split('\t\t')[0]
    genre = line.split('\t\t')[1]
    genre_dict[title] = genre
    if genre in genre_count:
        genre_count[genre] += 1
    else:
        genre_count[genre] = 1
    

with open('../output/out.txt', 'r') as f:
    data = f.readlines()

actor_list = []
for line in data:
    temp = line.split('||')
    actor_list.append(temp[1])

with open('../output/movie_dict.txt', 'r') as f:
    data = f.readlines()

movies = []
i = 0
for line in data:
    line = line.split('||')
    title = line[1]
    temp_actors = line[2].split('\t\t')
    actors = [actor_list[int(id)] for id in temp_actors]
    if title in genre_dict:
        genre = genre_dict[title]
    else:
        genre = None
        i += 1
    movie = Movie(title, actors, genre)
    movies.append(movie)

with open('../output/community.txt', 'r') as f:
    comms = f.readlines()

selected_comms = np.random.choice(comms, 10)

for m in comms:
    print(len(m.split(' ')))

i = 0

for comm in selected_comms:
    comm_genres = []
    comm = comm.split(' ')
    comm_genre_count = {}
    total = 0
    for movie_id in comm:
        genre = movies[int(movie_id)].genre
        if genre != None:
            comm_genres.append(genre)
            total += 1
        if genre in comm_genre_count:
            comm_genre_count[genre] += 1
        else:
            comm_genre_count[genre] = 1

    scores = []
    for g in comm_genres:
        c_i = comm_genre_count[g]
        p_i = comm_genre_count[g] / total
        q_i = genre_count[g] / len(genre_dict)
        if np.log(c_i) *  p_i / q_i == 0:
            print("zero appeared")
        scores.append(np.log(c_i) *  p_i / q_i)
        
    max_i = np.argmax(scores)
    print("#################################")
    print('The genre with the highest score is {}, the score is {}'.format(comm_genres[max_i], scores[max_i]))\

    plt.hist(comm_genres, bins='auto')  # arguments are passed to np.histogram
    plt.title("Frequency of Genres: community # {}".format(i))
    plt.xticks(rotation='vertical')
    plt.show()
    i += 1

with open ('../output/8c.txt', 'w+') as f:

    temp_movies = comms[-1].split(' ')
    d = {}
    for m_id in temp_movies:
        actors = movies[int(m_id)].actors
        title = movies[int(m_id)].title
        d[m_id] = title
        for actor in actors:
            f.write("%s\t%s\n"%(actor, title))

comm = temp_movies

for movie_id in comm:
    genre = movies[int(movie_id)].genre
    if genre != None:
        comm_genres.append(genre)
        total += 1
    if genre in comm_genre_count:
        comm_genre_count[genre] += 1
    else:
        comm_genre_count[genre] = 1

scores = []
for g in comm_genres:
    c_i = comm_genre_count[g]
    p_i = comm_genre_count[g] / total
    q_i = genre_count[g] / len(genre_dict)
    if np.log(c_i) *  p_i / q_i == 0:
        print("zero appeared")
    scores.append(np.log(c_i) *  p_i / q_i)
    
max_i = np.argmax(scores)
print("#################################")
print('The genre with the highest score is {}, the score is {}'.format(comm_genres[max_i], scores[max_i]))\

plt.hist(comm_genres, bins='auto')  # arguments are passed to np.histogram
plt.title("Frequency of Genres: community # {}".format(i))
plt.xticks(rotation='vertical')
plt.show()
i += 1