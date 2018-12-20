def print_lol(list_movies):
    for movies in list_movies:
        if isinstance(movies, list):
                print_lol(movies)
        else:
            print(movies)
            
print_lol(list_of_movies)
