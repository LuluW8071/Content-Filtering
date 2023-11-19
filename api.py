import requests

# TMDB API key
TMDB_API_KEY = '#'

# Algolia Search API key
ALGOLIA_APP_ID = '#'
ALGOLIA_API_KEY = '#'
ALGOLIA_INDEX_NAME = '#'

# TMDB API fetch Request 
def fetch_poster(movie_ids):
    poster_urls = []
    for movie_id in movie_ids:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}&language=en-US?api_key={TMDB_API_KEY}"
        data = requests.get(url)
        data = data.json()
        # print (data)

        # Check 'poster_path' exists in response
        if 'poster_path' in data:
            poster_path = data['poster_path']
            full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
            poster_urls.append(full_path)
        else:
            poster_urls.append(None)
    return poster_urls

def fetch_overview(movie_ids):
    overview_descript = []
    for movie_id in movie_ids:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}&language=en-US?api_key={TMDB_API_KEY}"
        data = requests.get(url)
        data = data.json()

        if 'overview' in data:
            overview = data['overview']
            overview_descript.append(overview)
        else:
            overview_descript.append(None)
    return overview_descript


# TEST1: TMDB Api fetch request
movie_ids = [19995] 
posters = fetch_poster(movie_ids)
overview = fetch_overview(movie_ids)
print(posters)
print(overview)

# TEST2: ALgolia Search API fetch request

# Check Trailer fetch request
# https://api.themoviedb.org/3/movie/19995/videos?api_key=58d7bb45cdb3261fb790a798152d9e93&language=en-US