def prepare_movie_data(movies, ratings):
    rating_stats = ratings.groupby("movieId")["rating"].agg(
        average_rating="mean",
        rating_count="count"
    ).reset_index()

    movies_with_ratings = movies.merge(rating_stats, on="movieId")

    return movies_with_ratings


def get_movies_by_genre(movies_with_ratings, genre):
    genre_movies = movies_with_ratings[
        movies_with_ratings["genres"].str.contains(genre, na=False)
    ]

    return genre_movies


def get_recommendations(movies_with_ratings, genre, preference):
    genre_movies = get_movies_by_genre(movies_with_ratings, genre)

    if preference == "Popular":
        recommendations = genre_movies.sort_values(
            by="rating_count",
            ascending=False
        )

    elif preference == "Highly Rated":
        recommendations = genre_movies.sort_values(
            by="average_rating",
            ascending=False
        )

    elif preference == "Underrated":
        recommendations = genre_movies[
            genre_movies["rating_count"] < 50
        ].sort_values(
            by="average_rating",
            ascending=False
        )

    else:
        recommendations = genre_movies

    return recommendations.head(10)
