'''
    Sandbox for Numpy, Pandas.... let's play! 
    CS 2100
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# # read a CSV file into a pandas data frame
# # IMDb top movies between 1980 and 2026
# # Source: https://www.kaggle.com/datasets/elvisbui/imdb-top-movies-1980-2026

df = pd.read_csv("data/imdb_top_movies_1980_2026.csv")


# what's in the dataframe?
print(df.head())   # head is the first few rows
print(f'\nColumns of the data frame: \n{df.columns}')  # the column names
print(f'\nCommon stats on numerical data: \n{df.describe()}')  # prints common stats of numeric data

# length of dataframe is the number of rows
print(f"There are {len(df)} entries in the dataframe/file")


# Shape and missing values
print(f'Rows: {df.shape[0]}, Columns: {df.shape[1]}')
print(f'Number of NA values per column: {df.isna().sum()}')


# Genres is a string... beter if it's a list for processing
df['genres_list'] = df['genres'].str.split(",")
print('\n' + '-' * 80)
print('Genres split into a list and a column created from it')
print(df[ ['genres', 'genres_list']])



###############
# Data cleaning
###############


# TODO: Look for implausible runtimes
LONG_RUNTIME = 500
really_long = df[(df["runtime_minutes"] > LONG_RUNTIME)]

print('\n' + '-' * 80)
print(f'Movie with runtime over {LONG_RUNTIME} minutes')
print(really_long[ ['title', 'runtime_minutes', 'average_rating'] ])

# TODO: Drop rows with missing essential fields

# TODO: What's the best movie from someone's birth year?
# We need to filter for a particular year and then, for that year,
# to find the one that is best.

TOP_N = 3
def best_movies_in_year(df, year):
    mask = (df['year'] == year)
    all_movies_in_year = df[mask]
    return all_movies_in_year.sort_values('average_rating', ascending=False).head(TOP_N)

print('\n' * 2 + '-' * 80)
print(f'Demo to filter dataframe and get top {TOP_N} movies in a given year')
year = 2000 # int(input("What year would you like to see best movies: "))
print(f'The top {TOP_N} movies in {year} are... ')
print(best_movies_in_year(df, year)[ ['title', 'average_rating', 'num_votes'] ])

plt.scatter(df['average_rating'], df['num_votes'])
plt.show()

