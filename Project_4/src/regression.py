import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def work(movie_obj_list, target_movie_obj):
    # assert movie_obj_list is list
    i = 0
    X = np.zeros([len(movie_obj_list), 3])
    Y = np.zeros([len(movie_obj_list), 1])
    for movie in movie_obj_list:
        genre_score = movie.genre_score
        actor_score = movie.actor_score
        director_score = movie.director_score
        rating = movie.rating
        X[i, 0] = genre_score
        X[i, 1] = actor_score
        X[i, 2] = director_score
        Y[i, 0] = rating
        i += 1

    X_label = np.array([target_movie_obj.genre_score,
                        target_movie_obj.actor_score,
                        target_movie_obj.director_score])
    Y_label = np.array([target_movie_obj.rating])
    model = LinearRegression()

    X_train = X[:-20][:]
    Y_train = Y[:-20][:]
    X_test = X[-20:][:]
    Y_test = Y[-20:][:]

    model.fit(X_train, Y_train)
    Y_pred = model.predict(X_test)

    print("Mean squared error: %.2f"
          % mean_squared_error(Y_test, Y_pred))
