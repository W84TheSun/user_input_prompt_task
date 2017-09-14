import operator
import re

def help():
    return "Usage: N [word M]"


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

def main():
    words_founded = int(input())
    words_dictionary = {}
    prompts = []
    if 1 <= words_founded <= 10 ** 5:
        for i in range(words_founded):
            word, freq = input().split()
            if len(word) > 15:
                return "%s is longer than 15 letters!" % word
            if word not in words_dictionary:
                words_dictionary[word] = int(freq)
    words_prompted = int(input())
    if 1 <= words_prompted <= 15000:
        for i in range(words_prompted):
            prompt = input()
            if len(prompt) > 15:
                return "%s is longer than 15 letters"
            prompts.append(prompt)

    words = sorted(words_dictionary.items(),
                   key=operator.itemgetter(1),
                   reverse=True)

    for prompt in prompts:
        results = find_suitable_words(prompt, words)
        print("")
        print(results)
        print("")
    return help()

if __name__ == '__main__':
    main()
