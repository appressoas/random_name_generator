from random_name_generator import name_generator as namegen

for n in namegen.get_random_names(111):
    print(n.encode('utf-8'))
print('-'*80)

for n in namegen.get_names(1):
    print(n.encode('utf-8'))
print('-'*80)

