# TODO: input a movie name, get its community, get the genre score inside that
#       community, get the actor score inside the community, perform linear
#       regression
import numpy as np
from regression import work

class Movie:
    def __init__(self, movie_id, title, actors, genre, director,
                 rating):
        self.id = movie_id
        self.title = title
        self.actors = actors
        self.genre = genre
        self.director = director
        self.genre_score = None
        self.actor_score = None
        self.director_score = None
        self.rating = rating


with open('../output/movie_dict.txt', 'r') as f:
    data = f.readlines()

target = {}   # movie name : movie_id
movie_name = {}  # movie_id : movie name in the community
movie_actor = {}  # movie_id : actor_id
for line in data:
    movie = line.split('||')[1]
    movie_id = line.split('||')[0]
    if movie in ['Batman v Superman: Dawn of Justice (2016)',
                 'Mission: Impossible - Rogue Nation (2015)',
                 'Minions (2015)']:
        target[movie] = int(movie_id)
    movie_name[int(movie_id)] = movie
    movie_actor[int(movie_id)] = [int(id) for id in line.split('||')[2].split(
                                  '\t\t')]
del data

with open('../output/community.txt', 'r') as f:
    comms = f.readlines()

comm = []  # [[com1], [com2], [com3], ...], all movie ids
for line in comms:
    com_list = [int(i) for i in line.split(' ')]
    comm.append(com_list)
del comms

with open('../data/movie_genre.txt', 'r', encoding='ISO-8859-1') as f:
    movie_genre = f.readlines()
genre_dict = {}  # movie name : genre
genre_count = {}  # genre : number
for line in movie_genre:
    title = line.split('\t\t')[0]
    genre = line.split('\t\t')[1].replace('\n', '')
    genre_dict[title] = genre
    if genre in genre_count:
        genre_count[genre] += 1
    else:
        genre_count[genre] = 1
del movie_genre

movie_director = {}  # movie name : director
with open('../data/director_movies.txt', 'r', encoding='ISO-8859-1') as f:
    movie_directors = f.readlines()
for line in movie_directors:
    title = line.split('\t\t')[1].split('\t\t')
    director = line.split('\t\t')[0]
    for name in title:
        movie_director[name] = director
del movie_directors

movie_rating = {}
with open('../data/movie_rating.txt', 'r', encoding='ISO-8859-1') as f:
    movie_ratings = f.readlines()
for line in movie_ratings:
    movie_rating[line.split('\t\t')[0]] = float(line.split('\t\t')[1].replace('\n', ''))
del movie_ratings

comm_movie = []  # [[com1], [com2], ..] movie object

i = 0
target_com = {}  # name : com_id
for com_list in comm:
    ids = []
    movie_list = []
    for movie in target:
        ids.append(target[movie])
    for node in com_list:
        if node not in ids:
            movie_id = node
            name = movie_name[node]
            actor = movie_actor[node]
            genre = (genre_dict[movie_name[node]]) if (
                movie_name[node] in genre_dict) else None
            director = (movie_director[movie_name[node]]) if (
                movie_name[node] in movie_director) else None
            rating = (movie_rating[movie_name[node]]) if (
                movie_name[node] in movie_rating) else None
            if rating is None:
                pass
            else:
                movie_list.append(Movie(movie_id, name, actor, genre, director, rating))
        else:
            target_com[node] = i
    if len(movie_list) == 0:
        pass
    else:
        comm_movie.append(movie_list)
    i += 1

for movie in list(target):  # target becomes movie name : Movie
    movie_id = target[movie]
    name = movie
    actor = movie_actor[movie_id]
    genre = (genre_dict[movie_name[movie_id]]) if (
        movie_name[movie_id] in genre_dict) else None
    director = (movie_director[movie_name[movie_id]]) if (
        movie_name[movie_id] in movie_director) else None
    rating = (movie_rating[movie_name[movie_id]]) if (
        movie_name[movie_id] in movie_rating) else None
    target[movie] = Movie(movie_id, name, actor, genre,
                          director, rating)
del movie_name, movie_actor, movie_director, comm

i = 0
for community in comm_movie:
    comm_genres = []
    comm_genre_count = {}
    total = 0
    score = {}
    ratings = 0
    for movie_obj in community: 
        genre = movie_obj.genre
        if genre is not None:
            comm_genres.append(genre)
            total += 1
        if genre in comm_genre_count:
            comm_genre_count[genre] += 1
        else:
            comm_genre_count[genre] = 1
        ratings += movie_obj.rating if movie_obj.rating is not None else 0
    for genre in comm_genres:
        c_i = comm_genre_count[genre]
        p_i = c_i / total
        q_i = genre_count[genre] / len(genre_dict)
        score[genre] = np.log(c_i) * p_i / q_i


    total_score = 0
    for genre in score:
        total_score += score[genre]
    mean = total_score / len(score)


    for movie_obj in community:
        movie_obj.genre_score = score[movie_obj.genre] if movie_obj.genre\
            is not None or movie_obj.genre in score else mean

    for movie in target:
        if target_com[target[movie].id] == i:
            target[movie].genre_score = score[target[movie].genre] if\
                target[movie].genre is not None else mean

    director_rating = {}
    actor_rating = {}
    for movie_obj in community:
        if movie_obj.director is None:
            pass
        if movie_obj.actors is None:
            pass
        if movie_obj.director in director_rating:
            if movie_obj.rating is None:
                pass
            else:
                director_rating[movie_obj.director].append(movie_obj.rating)
        else:
            if movie_obj.rating is None:
                pass
            else:
                director_rating[movie_obj.director] = [movie_obj.rating]
        for actor in movie_obj.actors:
            if actor in actor_rating:
                if movie_obj.rating is None:
                    pass
                else:
                    actor_rating[actor].append(movie_obj.rating)
            else:
                if movie_obj.rating is None:
                    pass
                else:
                    actor_rating[actor] = [movie_obj.rating]

    director_count = 0.0
    director_mean = 0.0
    total_rating = 0.0
    for director, ratings in director_rating.items():
        director_count += len(ratings)
        total_rating += np.sum(ratings)
    
    director_mean = total_rating / director_count

    for movie_obj in community:
        if movie_obj.director is None or movie_obj.director not in director_rating:
            movie_obj.director_score = director_mean
        else:
            movie_obj.director_score = np.mean(
                director_rating[movie_obj.director])
        actor_score = []
        for actor in movie_obj.actors:
            if actor not in actor_rating:
                pass
            else:
                actor_score.append(np.mean(actor_rating[actor]))
        movie_obj.actor_score = np.mean(actor_score)

    actor_score = []
    for movie in target:
        if target_com[target[movie].id] == i:
            if target[movie].director is None:
                target[movie].director_score = director_mean
            else:
                target[movie].director_score = np.mean(
                    director_rating[target[movie].director]
                )
            for actor in target[movie].actors:
                if actor not in actor_rating:
                    pass
                else:
                    actor_score.append(np.mean(actor_rating[actor]))
            target[movie].actor_score = np.mean(actor_score)
    i += 1

del genre_count, genre_dict, movie_rating

# alive: target, comm_movie
# for community in comm_movie:
#     for movie_obj in community:
#         assert movie_obj.genre_score is not None
#         assert movie_obj.director_score is not None
#         assert movie_obj.actor_score is not None

# for _, movie_obj in target.items():
#     print(movie_obj.genre_score)
#     # assert movie_obj.actor_score is not None
#     print(movie_obj.actor_score)
#     # assert movie_obj.director_score is not None
#     print(movie_obj.director_score)

# print(type(comm_movie['Batman v Superman: Dawn of Justice (2016)']))
# for movie in comm_movie['Batman v Superman: Dawn of Justice (2016)']:
#     print(movie.id)
work(comm_movie, target)
