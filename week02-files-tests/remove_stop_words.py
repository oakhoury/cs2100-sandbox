
STOP_WORDS = [ # all in lowercase
    "a", "an", "the",                              # articles
    "in", "on", "of", "at", "by", "to", "for", "from", "with", # prepositions
    "and", "but", "or", "because", "as",           # conjunctions
    "he", "she", "it", "they", "them", "i", "you", # pronouns
    "is", "am", "are", "was", "were", "be", "do", "have",  "had", "has", # common verb conjugations
    "that", "his", "her", "their"
    ]

SUFFIX = '.txt'

def get_filename(prompt : str, filename_suffix : str) -> str:
    '''Returns the name of the file the user enters when presented with the prompt 
    and which needs to end with the `filename_suffix`

    Parameters
    ----------
    prompt : str 
        the message to display to the user with brief instructions on what to enter
    filename_suffix : str
        the suffix that the user's input needs to have for a valid filename 

    Returns
        the name of the file entered by the user that has the suffix specified
    '''

    filename : str = ""

    while not filename.endswith(filename_suffix):
        filename = input(prompt)

    return filename

def remove_stop_words(filename : str) -> str:
    '''Reads from a text file and removes words matching those in `STOP_WORDS`.

    Returns
    -------
    str
        the contents of the text file but with stop words removed from it.
    '''

    with open(filename, 'r', encoding="utf-8") as file:
        contents_cleaned : str = ''
        for line in file.readlines():
            for word in line.split():
                if word.lower() not in STOP_WORDS:
                    contents_cleaned += ' ' + word
            contents_cleaned += "\n"

        contents_cleaned.rstrip()
        return contents_cleaned


def write_story_to_file(story : str, filename : str) -> None:
    '''Writes story to a file.

    Parameters
    ----------
    story : str
        the text of the story to be saved/written
    filename : str
        the name of the file into which story is to be saved
    
    Raises
    ------
    ValueError
        if the story is empty
    '''

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(story)

def main() -> None:
    '''Program asking user for a story, removing stop words, writing it to another file.'''
    story_filename = get_filename(
        f"Enter a text file with the story (name must end with {SUFFIX}): ", SUFFIX)
    brief_story = remove_stop_words(story_filename)

    new_story_filename = get_filename(
        f"Enter name of new file for the brief story (name must end with {SUFFIX}): ", SUFFIX)

    write_story_to_file(brief_story, new_story_filename)


if __name__ == '__main__':
    main()
