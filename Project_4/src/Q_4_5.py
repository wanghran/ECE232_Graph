with open('../output/out.txt', 'r') as f:
    actor_data = f.readlines()
    actors = []
    nums = []
    for line in actor_data:
        temp = line.split('||')
        actors.append(temp[1])
        nums.append(len(temp[2]))

    # top_10 = []
    # num_movies = []
    # for i in [85691, 27627, 45392, 65911, 32113, 6535, 59701, 34245, 20538, 40331]:
    #     top_10.append(actors[i])
    #     num_movies.append(nums[i])
    # print(top_10)
    # print(num_movies)

    # Q 5
    famous = []
    num_movies_f = []
    for i in [14494, 111244, 12804, 27242, 32373, 16867, 62741, 107779, 17274, 53221]:
        famous.append(actors[i])
        num_movies_f.append(nums[i])
    print(famous)
    print(num_movies_f)