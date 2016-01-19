# Random name generator for python

```sh
pip install git+ssh://git@github.com/appressoas/random_name_generator.git
```

## Examples


```python
from random_name_generator import name_generator

# Single
get_random_generated_name()
Hogm Wuwyduc Uzh

# Multiple
get_random_generated_names(4)
['Ep Re', 'Bydu Kupeqy Osy', 'Sd', 'Mi Bige Zolo']

# Single
get_random_name()
Diancecht

# Multiple
get_random_names(4)
['Apulu', 'Hippolytos', 'Aku', 'Tamendonare']

# Multiple
get_names(6)
['Arsenius the Great', 'Sopdet', 'Heket', 'Kabundungulu', 'Quinuama']

# Single
pick_random_name_from_list(['Snoop', 'Notorious'], ['Dolly'])
Notorious

# Multiple
pick_random_list_of_names_from_list(['Snoop', 'Notorious'], ['Dolly', 'Carl'], number_of_names=2)
['Snoop', 'Notorious']


```
