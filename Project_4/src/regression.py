import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def work(movie_obj_list, target_movie_obj_list):
    # assert movie_obj_list is list
    i = 0
    length = 0
    for community in movie_obj_list:
        length += len(community)
    X = np.zeros([length, 3])
    Y = np.zeros([length, 1])
    for community in movie_obj_list:
        for movie in community:
            genre_score = movie.genre_score
            actor_score = movie.actor_score
            director_score = movie.director_score
            rating = movie.rating
            X[i, 0] = genre_score
            X[i, 1] = actor_score
            X[i, 2] = director_score
            Y[i, 0] = rating
            i += 1
    
    i = 0
    X_label = np.zeros([3, 3])
    Y_label = np.zeros([3, 1])
    movie_title = []
    for movie in target_movie_obj_list:
        movie_obj = target_movie_obj_list[movie]
        genre_score = movie_obj.genre_score
        actor_score = movie_obj.actor_score
        director_score = movie_obj.director_score
        rating = movie_obj.rating
        X_label[i, 0] = genre_score
        X_label[i, 1] = actor_score
        X_label[i, 2] = director_score
        Y_label[i, 0] = rating
        movie_title.append(movie)
        i += 1
    
    model = LinearRegression()

    model.fit(X, Y)
    Y_pred = model.predict(X)

    print("Mean squared error: %.2f"
          % mean_squared_error(Y, Y_pred))
    
    Y_pred = model.predict(X_label)
    i = 0
    for i in range(3):
        print(movie_title[i])
        print("Rating: %.2f"
            % Y_pred[i][0])
