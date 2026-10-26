'''
    Pandas: groupby and query
    CS 2100
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def clean(movies : pd.DataFrame) -> pd.DataFrame:
    cleaned_movies = movies.copy()

    cleaned_movies['genres_list'] = cleaned_movies['genres'].str.split(",")
    cleaned_movies = cleaned_movies.dropna(subset=["average_rating", "num_votes", "runtime_minutes"])

    return cleaned_movies

def group_by_genre(movies : pd.DataFrame) -> pd.DataFrame:
    df = movies
    df["genres"].fillna("")

    print(df["genres"].head())
    print(df["genres"].str.len().value_counts())

    df['genre_list'] = df['genres'].str.split(",")
    print(df[ ["imdb_id", "genres", "genre_list"] ].head())


    genres = df.explode("genre_list").dropna(subset=["genre_list"])

    # explode: transforms each element of a list-like to a row
    # Expands nested data structures like lists into separate rows, while
    # maintaining relationship with other columns. Thus, if a movie has 3
    # genres, then, there will be 3 rows in the resulting data frame, one
    # row for each of the different genres.
    #
    # The call to dropna() drops rows that have no genre

    print(genres[ ["imdb_id", "genres", "genre_list"] ].head())
    print(f'Length before explode: {len(df)} and after: {len(genres)}')

    # In-class demo: Group rows by the genre and determine: the number of movies,
    # the average rating, and the median number of votes.

    summary = (
        genres.groupby('genre_list')
            .agg(movie_count=('average_rating', 'size'),
                mean_rating=('average_rating', 'mean'))
            .query('movie_count > 1000').sort_values("movie_count", ascending=False)

    )

    print(summary)

def main():
    # IMDb top movies between 1980 and 2026
    # Source: https://www.kaggle.com/datasets/elvisbui/imdb-top-movies-1980-2026
    df = pd.read_csv("data/imdb_top_movies_1980_2026.csv")
    movies = clean(df)
    group_by_genre(movies)


if __name__ == "__main__":
    main()
