'''
A program to create random pairs of students and assign a random problem.
Demonstrates use of generator expressions, tuples, and lists
'''

import random
from itertools import batched
from collections.abc import Generator

FIRSTNAME_COLUMN = 'firstname'
PROBLEM_NAMES = ('Music listening history', 'Bill tracker', 'Pantry-to-Recipe matcher')

def get_column_values(filename : str, column_name = FIRSTNAME_COLUMN) -> tuple[str, ...]:
    '''Reads a CSV file and returns column values found at specified index

    Returns
    -------
    tuple(str, ...)
        the sequence of names found
    '''

    with open(filename, 'r', encoding="utf-8") as file:
        # first line is header with column names, values are all in quotes, so remove them
        # and find the index of the column (by its name) whose values we want
        column_index = file.readline().replace('"', '').split(",").index(column_name)

        return tuple(entry.split(",")[column_index].strip('"') for entry in file.readlines())


def print_pairs_problems(pair_gen : Generator) -> None:
    '''Iterates over the pair generator and prints each pair, 
    thus mutating the generator. Pauses for user between each pair.'''

    for p in pair_gen:
        _ = input("\nPress enter to show next pair...")
        problem = random.choice(PROBLEM_NAMES)
        print(f'\nPair: {p[0]} and {p[1] if len(p) > 1 else None}, problem: {problem}')



def main() -> None:
    '''Loads roster from a CSV file, randomly puts students in pairs and assigns 
    each a random problem
    '''

    names : tuple[str, ...] = get_column_values('data/cs2100-roster.csv')
    # names needed as a sequence as we will randomly sample it to create random pairs
    # batched() batches the random values into tuples of length 2 (in this case)

    pair_generator = (pair for pair in batched(random.sample(names, len(names)), 2))
    print_pairs_problems(pair_generator)

if __name__ == '__main__':
    main()
