import re
from sklearn.metrics import mean_squared_error

class Movie:
    def __init__(self, title, actors, rating):
        self.title = title
        self.actors = actors
        self.rating = rating 

movie_rating = {}
with open('../data/movie_rating.txt', 'r', encoding='ISO-8859-1') as f:
    data = f.readlines()

avg_rating = 0
num = 0
for line in data:
    movie_rating[line.split('\t\t')[0]] = float(line.split('\t\t')[1])
    avg_rating += float(line.split('\t\t')[1])
    num += 1
avg_rating = avg_rating / num
del data




with open('../output/movie_dict.txt', 'r') as f:
    data = f.readlines()

movies = {}

for line in data:
    movie_title = line.split('||')[1]
    actors = line.split('||')[2].split('\t\t')
    if movie_title not in movie_rating:
        rating = 0
    else:
        rating = movie_rating[movie_title]
    movies[movie_title] = Movie(movie_title, actors, rating)
del data


with open('../output/out.txt', 'r') as f:
    data = f.readlines()

actors = []
i = 0
for line in data:
    temp = line.split('||')
    movie_acted = temp[2].split('\t\t')
    actor_weights = []

    for title in movie_acted:
        if title in movies:
            actor_weights.append(movies[title].rating)
    if len(actor_weights) == 0:
        actors.append(0)
    else:
        actors.append(sum(actor_weights)/ len(actor_weights))

rmse = 0

p_score = []
g_score = []
for movie_title in movie_rating:
    # if movie_title not in movies:
    #     p_score.append(5)
    #     g_score.append(movies[movie_title].rating)
    #     continue
    if movie_title in movies:
        m_actors = movies[movie_title].actors
        a_score = [actors[int(a_id)] for a_id in m_actors]
        p_score.append(sum(a_score)/len(a_score))
    else:
        p_score.append(avg_rating)
    g_score.append(movie_rating[movie_title])

print(len(p_score))
print("The RMSE score for this bipartite graph is {} ".format(mean_squared_error(p_score, g_score)))

target = ['Batman v Superman: Dawn of Justice (2016)',
                 'Mission: Impossible - Rogue Nation (2015)',
                 'Minions (2015)']
for t in target:
    m_actors = movies[t].actors
    a_score = [actors[int(a_id)] for a_id in m_actors]
    print("The predicted score for {} is {} ".format(t, sum(a_score)/len(a_score)))