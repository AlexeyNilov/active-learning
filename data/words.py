from typing import List


def read_words_to_list(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        words = [word.strip() for word in file]

    return words


def get_known_verbs() -> List[str]:
    return read_words_to_list('words/known_verbs.txt')


def get_ignore_list() -> List[str]:
    return read_words_to_list('words/ignore.txt')
