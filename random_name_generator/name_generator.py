# -*- coding: utf-8 -*-
import random
import importlib

from namelists import african_myth
from namelists import australian_myth
from namelists import aztec_myth
from namelists import carribean_myth
from namelists import celtic_myth
from namelists import christian_myth
from namelists import egyptian_myth
from namelists import etruscan_myth
from namelists import finnish_myth
from namelists import germanic_myth
from namelists import greek_myth
from namelists import incan_myth
from namelists import indian_myth
from namelists import irish_myth
from namelists import mayan_myth
from namelists import mesopotamian_myth
from namelists import native_american_myth
from namelists import norse_myth
from namelists import oceanic_myth
from namelists import roman_myth
from namelists import south_american_myth
from namelists import tech_myth
from namelists import tibetian_myth

NAMELIST_MODULES = {
    'african_myth': african_myth,
    'australian_myth': australian_myth,
    'aztec_myth': aztec_myth,
    'carribean_myth': carribean_myth,
    'celtic_myth': celtic_myth,
    'christian_myth': christian_myth,
    'egyptian_myth': egyptian_myth,
    'etruscan_myth': etruscan_myth,
    'finnish_myth': finnish_myth,
    'germanic_myth': germanic_myth,
    'greek_myth': greek_myth,
    'incan_myth': incan_myth,
    'indian_myth': indian_myth,
    'irish_myth': irish_myth,
    'mayan_myth': mayan_myth,
    'mesopotamian_myth': mesopotamian_myth,
    'native_american_myth': native_american_myth,
    'norse_myth': norse_myth,
    'oceanic_myth': oceanic_myth,
    'roman_myth': roman_myth,
    'south_american_myth': south_american_myth,
    'tech_myth': tech_myth,
    'tibetian_myth': tibetian_myth,
}
NAMELIST_MODULES_KEYS = list(NAMELIST_MODULES)


class RandomNameGenerator:
    VOWELS = 'aeiouy'
    CRAZY_VOWELS = 'éúöøæå'
    CONSONANTS = 'bcdfghjklmnpqrstvwxz'
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

    def more_often_than_average(self):
        return random.randint(1, 4) < 4

    def get_next_if_consonant(self):
        if self.more_often_than_average():
            if random.randint(1, 13) == 1:
                return random.choice(self.CRAZY_VOWELS)
            else:
                return random.choice(self.VOWELS)
        return random.choice(self.ALPHABET)

    def get_next_if_vowel(self):
        if self.more_often_than_average():
            return random.choice(self.CONSONANTS)
        return random.choice(self.ALPHABET)

    def add_next_char(self, prev_char):
        if prev_char in self.CONSONANTS:
            return self.get_next_if_consonant()
        else:
            return self.get_next_if_vowel()

    def get_next_name(self):
        generated_name = []
        for j in range(random.randint(1, 3)):
            first_char = random.choice(self.ALPHABET)
            generated_name.append(first_char.capitalize())
            name_length = random.randint(2, 7)
            for k in range(1, name_length):
                prev_char = generated_name[-1].lower()
                generated_name.append(self.add_next_char(prev_char))
            generated_name.append(' ')
        return ''.join(generated_name).strip()


def get_random_name(namelist=None):
    if not namelist:
        lib_name = random.choice(NAMELIST_MODULES_KEYS)
    lib = importlib.import_module('{}.{}.{}'.format(
            'random_name_generator', 'namelists', lib_name))
    return random.choice(lib.names)

def get_random_names(number_of_names=1):
    names = set()
    for i in range(number_of_names):
        names.add(get_random_name())
    return list(names)

def get_random_generated_names(number_of_names=1):
    name_generator = RandomNameGenerator()
    generated_names = set()
    for i in range(number_of_names):
        generated_names.add(name_generator.get_next_name())
    return list(generated_names)

def get_random_generated_name():
    name_generator = RandomNameGenerator()
    return name_generator.get_next_name()

def get_names(number_of_names=1):
    names = set()
    n = 0
    while n < number_of_names:
        if n%2 == 0:
            name = get_random_name()
        else:
            name = get_random_generated_name()
        names.add(name)
        n = len(names)
    return list(names)


if __name__ == '__main__':
    print(get_names(1000))
