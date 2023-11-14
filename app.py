from flask import Flask, render_template, request, url_for
from api import fetch_poster
import pickle
from math import ceil
import re

import pandas as pd
import numpy as np

# Load dataset files
popular_df = pickle.load(open('model/movies_dataset.pkl', 'rb'))

app = Flask(__name__)

# Static location config
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['UPLOAD_FOLDER'] = 'static'
app.secret_key = 'secret'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['UPLOAD_FOLDER'] = 'static'

# Setting up home page
@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    per_page = 12
    movies_data = popular_df[['id',
                              'title',
                              'overview',
                              'genres',
                              'keywords',
                              'popularity',
                              'cast',
                              'crew',
                              'production_companies',
                              'runtime',
                              'release_year']]

    movies_data = movies_data.sort_values(by='popularity', ascending=False)

    # Pagination
    total_movies = len(movies_data)
    num_pages = ceil(total_movies / per_page)
    page = max(min(page, num_pages), 1)

    # Adjusted start_index and end_index for the requested page
    start_index = (page - 1) * per_page
    end_index = start_index + per_page

    paginated_movies = movies_data.iloc[start_index:end_index] 

    title = list(paginated_movies['title'].values)
    crew = list(paginated_movies['crew'].values)
    popularity = list(paginated_movies['popularity'].round(2))
    movie_ids = list(paginated_movies['id'].values)

    posters = fetch_poster(movie_ids)

    prev = '/?page=' + str(page - 1) if page > 1 else None
    next = '/?page=' + str(page + 1) if page < num_pages else None

    return render_template('home.html', movies=paginated_movies.to_dict(orient='records'),
                           title=title, 
                           crew=crew, popularity=popularity, 
                           posters=posters, 
                           num_pages=num_pages, current_page=page, prev=prev, next=next)


if __name__ == '__main__':
    app.run(debug=True)
