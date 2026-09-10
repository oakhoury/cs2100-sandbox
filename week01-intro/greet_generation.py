
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
        generation = "Generation Z (\"Zoomers\")"
    else:
        generation = "Generation Alpha"

    return generation

def main():
    name = input("What is your name: ")
    year = int(input("What is your birth year: "))

    generation = get_generation(year)

    print(f"Great to meet you {name}, you are in the {generation}!")



if __name__ == '__main__':
    main()
