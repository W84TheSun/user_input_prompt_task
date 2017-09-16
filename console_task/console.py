from core.errors import RangeError
from core import create_words_dictionary, find_suitable_words

def help():
    return """Usage: N 
                     [word n]
                     ... - N
                     [word n]
                     M
                     [prompt]
                     ... - M
                     [prompt]"""


def handle_input_lines(lines_range):
    input_list = []

    try:
        lines = int(input())
    except ValueError as e:
        raise e

    if lines_range[0] <= lines <= lines_range[1]:
        for i in range(lines):
            input_list.append(input())
    else:
        raise RangeError

    return input_list


def main():

    input_list = handle_input_lines([1, 10**5])
    prompts = handle_input_lines([1, 15000])

    words = create_words_dictionary(input_list)

    for prompt in prompts:
        results = find_suitable_words(prompt, words)
        print("")
        print(results)
        print("")


if __name__ == '__main__':
    main()
