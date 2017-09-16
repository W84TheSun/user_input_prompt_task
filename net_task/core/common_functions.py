import re
import operator

from core.errors import InputError

def create_words_dictionary(input_list):
    words_dictionary = {}

    for line in input_list:
        word, freq = line.split()
        if len(word) > 15:
            raise "Bad input. %s is longer than 15 letters!" % word
        if word not in words_dictionary:
            try:
                words_dictionary[word] = int(freq)
            except ValueError as e:
                raise InputError(
                    "Bad input. '%s' has wrong frequency parameter." % word)
        else:
            raise InputError("Bad input. %s already in dictionary." % word)

    sort = sorted(words_dictionary.items(),
                  key=operator.itemgetter(1),
                  reverse=True)

    return sort


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
