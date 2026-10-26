import pandas as pd
import numpy as np

from collections.abc import Callable


def demo_sorts():
    df = pd.DataFrame(
       {
            "col1": ["A", "A", "B", np.nan, "D", "C"],
            "col2": [2, 1, 9, 8, 7, 4],
            "col3": [0, 1, 9, 4, 2, 3],
            "col4": ["a", "B", "c", "D", "e", "F"],
        }
    )
    print('#' * 70)
    print('Raw unordered data')
    print(df)

    sorted_by_col1 = df.sort_values(by=["col1"])

    print('\n\n' + '#' * 70)
    print('ordered by one column: col1')
    print(sorted_by_col1)

    print('\n\n' + '#' * 70)
    print('ordered by two columns: col1, col2')
    sorted_by_col1_col2 = df.sort_values(by=["col1", "col2"], key=...)
    print(sorted_by_col1_col2)

    print('\n\n' + '#' * 70)
    print('ordered by col4 transformed values: lowercase')
    sorted_by_col4_lower = df.sort_values(by="col4", key=lambda col: col.str.lower())
    print(sorted_by_col4_lower)

    # Writing our own function to send as key:
    def ord_modulo_13(s : pd.Series) -> pd.Series:
        return s.transform(lambda x: ord(x) % 13)  # x is a string element from the series s

    # Not necessary... defined for demo of creating a Callable variable
    key_function : Callable[ [pd.Series], pd.Series ] = ord_modulo_13


    print('\n\n' + '#' * 70)
    print('ordered by col4 transformed values: ord % 13')
    sorted_by_col4_ord_mod_13 = df.sort_values(by="col4", key=key_function)
    print(sorted_by_col4_ord_mod_13)


    # How would we sort by 2 or more columns, using a function?




    # 1. create a temporary column combining the desired columns
    # 2. sort by the temporary column, with a key as needed
    # 3. drop the temporary column
    # This can be done in a chain of method calls (pipeline)
    print('\n\n' + '#' * 70)
    print('ordered by col3, col4 transformed values')

    sorted_by_col3_col4_f = (df
        .assign(difference=(df['col4'].transform(lambda x: ord(x))) - df['col3'])
        .sort_values(by=["difference"], key=lambda col: col % 13)
        .drop(columns='difference')
    )

    # Note the vectorized modulo operation!!! The key function (lambda expression doing 
    # modulo operation) is called once with the entire column 'difference'. 
    # Numpy performs the modulo operation to each element in the Series!

    print(sorted_by_col3_col4_f)


def demo_argsort():
    df = pd.DataFrame(
        {
            "col1": ["A", "A", "B", np.nan, "D", "C"],
            "col2": [2, 1, 9, 8, 7, 4],
            "col3": [0, 1, 9, 4, 2, 3],
            "col4": ["a", "B", "c", "D", "e", "F"],
        }
    )

    weights = np.array([0.7, 0.25, 0.42, 0.35, 0.8, 0.55])

    print('\n\n' + '#' * 70)
    print('\n\n' + '#' * 70)
    print(f'DataFrame:\n{df}')



    order = df['col2'].argsort()  # alternative: np.argsort(df['col2'])
    print(f'\nargsort on col2:\n{order}')


    # Viewing the DataFrame sorted using order
    print(f'DataFrame sorted on col2:\n{df.iloc[order]}')

    # Sorting a parallel array using the same order!
    print(f'Weights sorted by col2 order:\n{weights[order]}')

    # Rankings on col2
    ranks = np.argsort(order)
    print(f'\nranks based on col2:\n{ranks}')

    df.assign(rank=ranks)
    print(f'\nDataFrame with ranks based on col2:\n{ranks}')

def main():
    # demo_sorts()

    demo_argsort()

if __name__ == '__main__':
    main()