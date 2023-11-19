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
        # print (data)

        if 'overview' in data:
            overview = data['overview']
            overview_descript.append(overview)
        else:
            overview_descript.append(None)
    return overview_descript

def fetch_trailers(movie_ids):
    trailers = []
    for movie_id in movie_ids:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?language=en-US&api_key={TMDB_API_KEY}"
        data = requests.get(url)
        data = data.json()
        # print(data)
        if 'results' in data:
            for video in data['results']:
                if video.get('name') == "Official Trailer":
                    key = video.get('key')
                    full_path = f"https://www.youtube.com/watch?v={key}"
                    trailers.append(full_path)
        else:
            trailers.append(None)
    return trailers

# TEST1: TMDB Api fetch request
# movie_ids = [211672] 
# posters = fetch_poster(movie_ids)
# overview = fetch_overview(movie_ids)
# trailers = fetch_trailers(movie_ids)
# print(posters)
# print(overview)
# print(trailers)