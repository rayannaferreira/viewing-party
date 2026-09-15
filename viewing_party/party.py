
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
def get_watched_avg_rating(user_data):
    len_wached= len(user_data["watched"])
    if len_wached == 0:
        return 0.0
    
    total = 0
    for movie in user_data["watched"]:
        total+=movie["rating"]

    average= total /len_wached

    return average


def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None

    genres= {}
    for movie in user_data["watched"]:
        genre=movie["genre"]
        if genre in genres:
            genres[genre]+=1
        else:
            genres[genre]=1

    key= ""
    value= 0
    for genre,frequency in genres.items():
        if frequency>value:
            key=genre
            value=frequency

    return key






    
    




# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    watched_titles= {movie["title"] for movie in user_data["watched"]}
    friends_titles= {movie["title"] for movie in user_data["friends"][0]["watched"]}
    print(watched_titles)
    print(friends_titles)
    diference= watched_titles - friends_titles
    print(diference)

    results=[]
    for movie in user_data["watched"]:
        if movie["title"]in diference:
            results.append(movie)

    return results
        
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

