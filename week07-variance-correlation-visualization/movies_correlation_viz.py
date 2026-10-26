
'''
    Correlation of statistical variables
    Plots
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

# Week 07: Statistical measures
# Exploring the mean, stdev, 25th and 75th percentile
def demo_statistical_measures(movies : pd.DataFrame) -> None:
    summary = movies.describe()

    print(f'type = {type(summary)}') # it's also a data frame
    print(summary)

    # Using the .at[] indexer to get a single value at a row/column
    rating_mean = summary.at['mean', 'average_rating']

    # Using the .loc[] indexer to get multiple row values for a column
    rating_stats  = summary.loc[ ['std', '25%', '75%'], 'average_rating']

    top_rated_movies = movies[ movies['average_rating'] > rating_mean + 1.5 * rating_stats['std']]
    movies_top_25th = movies[ movies['average_rating'] > rating_stats['75%']]
    movies_bottom_25th = movies[ movies['average_rating'] < rating_stats['25%']]
    print(f'There are {len(top_rated_movies)} movies that are 1.5x standard deviations above mean')
    print(f'There are {len(movies_top_25th)} movies that are in the top 25th percentile')
    print(f'There are {len(movies_bottom_25th)} movies that are in the bottom 25th percentile')

def demo_correlation(movies : pd.DataFrame) -> None:
    print('#' * 100)
    print('Correlation by Numpy')
    print('avg rating vs # of votes')
    print(np.corrcoef(movies['average_rating'], movies['num_votes']))
    print('\n\navg rating vs year')
    print(np.corrcoef(movies['average_rating'], movies['year']))
    print('\n\nnum_votes vs year')
    print(np.corrcoef(movies['num_votes'], movies['year']))

    print('#' * 100)
    print('\n\nCorrelation by Pandas: Pearson')
    print(movies[ ['average_rating', 'num_votes', 'year'] ].corr())
    print('\n\nCorrelation by Pandas: Spearnman')
    print(movies[ ['average_rating', 'num_votes', 'year'] ].corr(method='spearman'))

def demo_scatter_plot(movies : pd.DataFrame) -> None:

    print('\n\n' + '#' * 100)
    print('Scatter plot shows\n' +
          '\n(1) Movies with low votes, span the entire range of ratings (bad, so so, and great movies)' +
          '\n(2) With more votes, the ratings start to narrow (more people see and review better movies?)'
          '\n(3) Movies with lots of votes are rarely bad, whereas those with low votes are hit-and-miss')
    
    plt.scatter(movies['num_votes'], movies['average_rating'])
    plt.xlabel('Number of votes')
    plt.ylabel('Average rating')
    plt.savefig('figures/scatter1-votes-vs-rating.png')
    plt.show()

    plt.clf() # clears the current figure (needed to maintain the same color, o/w plt cycles)

    print('\n\n' + '#' * 100)
    print('Using alpha channel for transparency shows more detail')

    plt.scatter(movies['num_votes'], movies['average_rating'], alpha=0.15)
    plt.xlabel('Number of votes')
    plt.ylabel('Average rating')
    plt.savefig('figures/scatter2-votes-vs-rating.png')
    plt.show()


    x, y = movies["num_votes"], movies["average_rating"]

    # Create a figure that will have 3 plots, laid out horizontally
    fig, axes = plt.subplots(1, 3, figsize=(16, 4.5))

    # The values in the scatter plot are concentrated on the left side (smaller number of votes)
    # We can spread those out by using a log scale on votes
    axes[0].scatter(x, y, alpha=0.15, s=8)
    axes[0].set(xscale="log", xlabel="Votes (log scale)", ylabel="Average rating")

    # To show more details, we can use different colors to represent the number of data
    # points that overlap. Pyplotlib has hexbin() to use colors for density of the points
    # see: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hexbin.html

    hb = axes[1].hexbin(x, y, xscale="log", gridsize=40, bins="log")
    axes[1].set(xlabel="Votes (log scale)")
    fig.colorbar(hb, ax=axes[1], label="log10(count)")

    # AS there's a 
    # Rating quantiles within vote bins: makes the funnel explicit
    bins = pd.qcut(x, q=10)
    q = movies.groupby(bins, observed=True)["average_rating"].quantile([0.1, 0.5, 0.9]).unstack()
    centers = movies.groupby(bins, observed=True)["num_votes"].median()
    for col, label in zip(q.columns, ["10th percentile", "median", "90th percentile"]):
        axes[2].plot(centers, q[col], marker="o", label=label)
    axes[2].set(xscale="log", xlabel="Votes (log scale, bin medians)", ylabel="Average rating")
    axes[2].legend()

    fig.savefig('figures/scatter3-logscale-hexbin-quantiles.png', dpi=150)

    # Pandas also has supporting methods for scatter matrix
    pd.plotting.scatter_matrix(movies[ ['average_rating', 'num_votes']], figsize=(8, 8), alpha=0.3)
    plt.show()


def main() -> None:
    # read a CSV file into a pandas data frame
    # IMDb top movies between 1980 and 2026
    # Source: https://www.kaggle.com/datasets/elvisbui/imdb-top-movies-1980-2026

    df = pd.read_csv("data/imdb_top_movies_1980_2026.csv")
    movies = clean(df)

    # demo_statistical_measures(movies)

    demo_correlation(movies)

    demo_scatter_plot(movies)


if __name__ == '__main__':
    main()
