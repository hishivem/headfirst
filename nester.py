import sys

def print_lol(list_movies, indent=False, level=0, fh= sys.stdout):
    for movies in list_movies:
        if isinstance(movies, list):
                print_lol(movies, indent, level+1, file=fh)
        else:
            if indent:
                for tab_stop in range(level):
                   print("\t", end='', file=fh)
            print(movies, file=fh)
            
