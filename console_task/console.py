import operator
import re

class InputError(Exception): pass

def help():
    return """Usage: N 
                     [word n]
                     ... - N
                     [word n]
                     M
                     [prompt]
                     ... - M
                     [prompt]"""


def find_suitable_words(prompt, words):
    matched = []
    regex = re.compile("^" + prompt)
    for word in words:
        match = regex.search(word[0])
        if match:
            matched.append(word[0])

    if len(matched) > 0:
        return "\n".join(matched)
    else:
        return "Nothing found."

def handle_input_lines(lines_range):
    input_list = []

    try:
        lines = int(input())
    except ValueError as e:
        return False

    if lines_range[0] <= lines <= lines_range[1]:
        for i in range(lines):
            input_list.append(input())
    else:
        return False

    return input_list


def create_word_dictionary(input_list):
    words_dictionary = {}

    for line in input_list:
        word, freq = line.split()
        if len(word) > 15:
            raise "Bad input. %s is longer than 15 letters!" % word
        if word not in words_dictionary:
            try:
                words_dictionary[word] = int(freq)
            except ValueError as e:
                raise InputError("Bad input. '%s' has wrong frequency parameter." % word )
        else:
            raise InputError("Bad input. %s already in dictionary." % word)

    sort = sorted(words_dictionary.items(),
                   key=operator.itemgetter(1),
                   reverse=True)

    return sort

def main():

    input_list = handle_input_lines([1, 10**5])
    prompts = handle_input_lines([1, 15000])

    words = create_word_dictionary(input_list)


    words_prompted = int(input())
    if 1 <= words_prompted <= 15000:
        for i in range(words_prompted):
            prompt = input()
            if len(prompt) > 15:
                return "%s is longer than 15 letters" % prompt
            prompts.append(prompt)


    for prompt in prompts:
        results = find_suitable_words(prompt, words)
        print("")
        print(results)
        print("")
    return help()

if __name__ == '__main__':
    main()
