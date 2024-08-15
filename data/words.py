from typing import List


def read_words_to_list(filepath: str) -> List[str]:
    with open(filepath, 'r') as file:
        words = [word.strip() for word in file]

    return words


def get_known_verbs() -> List[str]:
    return read_words_to_list('words/known_verbs.txt')
