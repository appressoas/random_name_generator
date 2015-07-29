import random


def get_random_word(*namelists, exclude=None):
    namelist = random.choice(namelists)
    word = random.choice(namelist)
    if exclude and word in exclude:
        return get_random_word(*namelists, exclude=exclude)
    return word


def generate_name(*namelists, words=1):
    name = ''
    picked_words = set()
    for wordindex in range(words):
        picked_word = get_random_word(*namelists, exclude=picked_words)
        picked_words.add(picked_word)
        name = '{} {}'.format(name, picked_word)
    return name
