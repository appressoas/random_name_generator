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

if __name__ == '__main__':
    import importlib

    from namelists import *
    lib_names = [m for m in dir() if m.endswith('_myth')]

    names = []
    names_dict = {}
    myth_dict = {}
    for lib_name in lib_names:
        lib = importlib.import_module('{}.{}'.format('namelists', lib_name))
        myth_dict[lib_name] = []

        for n in lib.names:
            n = n.replace(',', '')

            if not n in names_dict:
                names_dict[n] = lib_name
                myth_dict[lib_name].append(n)
            else:
                print('Duplicate:', lib_name, n, 'allready in', names_dict[n])
        print()
        print(lib_name)
        print(myth_dict[lib_name])
