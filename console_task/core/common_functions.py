import re
import operator

from core.errors import InputError


def create_words_dictionary(input_list):
    words_dictionary = []

    for line in input_list:
        word, freq = line.split()
        if len(word) > 15:
            raise "Bad input. %s is longer than 15 letters!" % word
        if word not in words_dictionary:
            try:
                words_dictionary.append([word, int(freq)])
            except ValueError as e:
                raise InputError(
                    "Bad input. '%s' has wrong frequency parameter." % word)
        else:
            raise InputError("Bad input. %s already in dictionary." % word)

    alphabet = sorted(words_dictionary, key=operator.itemgetter(0))
    by_freq = sorted(alphabet, key=operator.itemgetter(1), reverse=True)

    return by_freq


def find_suitable_words(prompt, words):
    matched = []
    regex = re.compile("^" + prompt)
    for word in words:
        match = regex.search(word[0])
        if match:
            matched.append(word[0])

    if len(matched) > 0:
        return "\n".join(matched[:10])
    else:
        return False
