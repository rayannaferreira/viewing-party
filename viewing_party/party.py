# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
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

# ---------------- WAVE 3 ----------------

def get_unique_watched(user_data):
    friends_titles = set()

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_titles.add(movie["title"])

    results = []

    for movie in user_data["watched"]:
        if movie["title"] not in friends_titles:
            results.append(movie)

    return results


def get_friends_unique_watched(user_data):
    watched_titles = set()

    for movie in user_data["watched"]:
        watched_titles.add(movie["title"])

    results = []
    added_titles = set()

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in watched_titles and movie["title"] not in added_titles:
                results.append(movie)
                added_titles.add(movie["title"])

    return results
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    #create an empty list for movie recomandation
    recommendations = []

    #go through each friend in the user's friend list
    for friend in user_data["friends"]:

        #go through each movie this friend watched
        for movie in friend ["watched"]:

            #check that the user has not watched this movie
            if movie not in user_data["watched"]:
                #check user has acsess to streaming 
                if movie["host"] in user_data["subscriptions"]:

                    #check if movie is not already in recomandation
                    if movie not in recommendations:
                        #add movie to recomendation list
                        recommendations.append(movie)
    return recommendations
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):

    #get_the genre user watches most ofter
    most_watched_genre = get_most_watched_genre(user_data)

    #empty list for recomendation
    recommendations = []

    #if user has not watched any movies, return empty list
    if most_watched_genre is None:
        return recommendations


    #go through each friend
    for friend in user_data["friends"]:

        #go through each movie friend watched
        for movie in friend['watched']:

            #chech if the movie has user's most watched genre
            if movie["genre"] == most_watched_genre:
                #check if user has not watched movie eyt
                if movie not in user_data["watched"]:
                    #check if movie is not in recommendations already
                    if movie not in recommendations:
                        #add movie to recomendation
                        recommendations.append(movie)
    return recommendations

#favorite movie + none of friend watched it = recommendation
def get_rec_from_favorites(user_data):
    #make an empty list for recomandation
    recommendations = []

    #check each favorite movie
    for movie in user_data["favorites"]:
        #start by thinking no friend watched it
        watched_by_friend = False

        #check each friend
        for friend in user_data["friends"]:
            #if friend watched this movie
            if movie in friend["watched"]:
                watched_by_friend = True

        #if no friend watched it, add it
        if watched_by_friend == False:
            recommendations.append(movie)
    #return final list
    return recommendations
