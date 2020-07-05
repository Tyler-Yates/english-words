import re

NON_ALPHA_REGEX = re.compile(r"[^a-z]")


def _is_normal_word(word: str, case_sensitive=True) -> bool:
    if not case_sensitive:
        word = word.lower()

    match = NON_ALPHA_REGEX.search(word)
    return match is None


def _is_at_least_length(word: str, length=3) -> bool:
    return len(word) >= length


def main():
    with open("input.txt", mode='r') as input_file:
        for line in input_file.readlines():
            line = line.strip()
            word = line.split('/')[0]
            if _is_normal_word(word) and _is_at_least_length(word, 3):
                print(word)


if __name__ == '__main__':
    main()
