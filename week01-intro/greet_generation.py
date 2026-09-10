
# Source: https://en.wikipedia.org/wiki/Generation
#   Used to determine the ranges of each named generation

def get_generation(year):
    if year < 1901:
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

def main():
    name = input("What is your name: ")
    year = input("What is your birth year: ")

    generation = get_generation(year)

    print(f"Great to meet you {name}, you are in the {generation}!")



if __name__ == '__main__':
    main()

###  Key takeaways
# Correct indentation is imperative as there are no block delimiters
# Variables are typed, but it's determined at run-time! 
### 


# TODO: We can do better... back to slides to see how!