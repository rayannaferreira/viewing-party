
# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    print("Entrei NA CREATE_MOVIE")
    print(title,genre,rating)
    if  title is None or  genre is None or rating is None:
        return None
    
    movie= {}
    movie["title"]= title
    movie["genre"]= genre
    movie["rating"]= rating

    return movie



def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data,tittle):
    for i in range (len(user_data["watchlist"])):
        movie= user_data["watchlist"][i]
        if movie["title"]== tittle:
            removed_movie=user_data["watchlist"].pop(i)
            user_data["watched"].append(removed_movie)
            return user_data
    return  user_data



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

