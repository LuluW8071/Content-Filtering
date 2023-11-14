import requests

# TMDB API key
TMDB_API_KEY = "#"

def fetch_poster(movie_ids):
    poster_urls = []
    for movie_id in movie_ids:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
        data = requests.get(url)
        data = data.json()
        poster_path = data['poster_path']
        full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
        poster_urls.append(full_path)
    return poster_urls

# Check Api fetch request
# movie_ids = [19995] 
# posters = fetch_poster(movie_ids, api_key=TMDB_API_KEY)
# print(posters)
