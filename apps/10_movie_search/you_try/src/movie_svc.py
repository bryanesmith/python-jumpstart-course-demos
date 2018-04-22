import collections

import requests

MovieResult = collections.namedtuple(
    'MovieResult',
    'imdb_code,title,duration,director,year,rating,imdb_score,keywords,genres')


def find_movies(search_text):

    if not search_text or not search_text.strip():
        raise ValueError("Search text is required")

    url = 'http://movie_service.talkpython.fm/api/search/{}'.format(search_text)

    resp = requests.get(url)
    resp.raise_for_status()

    movies_data = resp.json().get('hits')
    movies = [MovieResult(**md) for md in movies_data]

    return sorted(movies, key=lambda md: -md.year)
