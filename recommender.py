def get_movies_by_genre(movies, genre):
    genre_movies = movies[
        movies["genres"].str.contains(genre, na=False)
    ]

    return genre_movies

