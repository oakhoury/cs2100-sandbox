
# Source: https://en.wikipedia.org/wiki/Generation
#   Used to determine the ranges of each named generation

# Noteworthy
# No need to define a class as you do in Java
# Delimiter for block of code is a colon before the start of the block
# Intentation of instrucdions is what defines if it's inside of a block or not
# No semicolons
# Variables have a data type... however, it's not explictly defined in the code

def get_generation(year : int) -> str:
    """Returns the name of the generation that `year` falls in.

    Parameters
    ----------
    year : int
        The year to be mapped to a generation name

    Returns
    -------
    str
        The name of the generation that `year` maps to

    Raises
    ------
    ValueError
        If year is negative

    """
    if year < 0:
        raise ValueError("year cannot be negative")
    elif year < 1901:
        generation = "Unknown"
    elif year <= 1927:
        generation = "Greatest Generation"
    elif year <= 1945:
        generation = "Silent Generation"
    elif year <= 1964:
        generation = "Baby Boomers"
    elif year <= 1980:
        generation = "Generation X"
    elif year <= 1996:
        generation = "Millenials"
    elif year <= 2012:
        generation = "Generation Z (\"Zoomers\")"  # Note the escaped character
    else:
        generation = "Generation Alpha"

    return generation

def main() -> None:
    """Program asks name and year from a user and greets them with their generation.
    """
    name : str = input("What is your name: ")
    year : int = int(input("What is your birth year: "))

    generation = get_generation(year)

    print(f"Great to meet you {name}, you are in the {generation}!")



if __name__ == '__main__':  # if file is being executed
    main()

###  Key takeaways
# Correct indentation is imperative as there are no block delimiters
# Variables are typed, but it's determined at run-time!
# We can annotate variables with their type
# MyPy analyzes annotations and code to report inconsistencies/errors
# Pylint analyzes code for style based on standard PEP 8, see: https://pep8.org
###
