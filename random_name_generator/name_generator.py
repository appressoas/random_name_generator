import random
import importlib

NAMELIST_MODULES = [
    'african_myth',
    'australian_myth',
    'aztec_myth',
    'carribean_myth',
    'celtic_myth',
    'christian_myth',
    'egyptian_myth',
    'etruscan_myth',
    'finnish_myth',
    'germanic_myth',
    'greek_myth',
    'incan_myth',
    'indian_myth',
    'irish_myth',
    'mayan_myth',
    'mesopotamian_myth',
    'native_american_myth',
    'norse_myth',
    'oceanic_myth',
    'roman_myth',
    'south_american_myth',
    'tech_myth',
    'tibetian_myth',
    'faked_myth',
]


class RandomNameGenerator:
    VOWELS = 'aeiouy'
    CRAZY_VOWELS = 'éúöøæå'
    CONSONANTS = 'bcdfghjklmnpqrstvwxz'
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

    def more_often_than_average(self):
        return random.randint(1, 4) < 4

    def get_next_if_consonant(self):
        if self.more_often_than_average():
            if random.randint(1, 10) == 1:
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
        lib_name = random.choice(NAMELIST_MODULES)
    lib = importlib.import_module('{}.{}'.format('namelists', lib_name))
    return random.choice(lib.names)

def get_list_of_random_names(number_of_names=1):
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


if __name__ == '__main__':
    for n in get_random_generated_names(10):
        print(n)

    for i in range(100):
        print(get_random_name())

    print(get_list_of_random_names(200))
