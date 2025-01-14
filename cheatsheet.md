## crash course

## https://ehmatthes.github.io/pcc_3e/new_in_3e/

# p 180/218

# LISTS

list=['item1', 23]

## ajout éléments

list[0]='modifie 1er item'
list.append('item') -> ajoute à la fin
list.insert(0, 'item')

## retrait

del list[0] -> retire 1er item
list.pop() -> enlève dernier
liste.remove('item')

## organiser liste

liste.sort(reverse=True or False) -> tri définitif
sorted(liste) -> tri non définitif
liste.reverse() -> inverse ordre items

## functions

Utiliser copie d'une liste dans une fonction

function_name(list_name[:])

Nombre arguments inconnu :
def nom_fonction(arg1, *args):
Nombre d'arguments name:value pairs inconnu
def nom_fonction(arg1, **kwargs):
ex : user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')

...
for key, value in dict.items():
object_dic[key]=value
...

import module fonction
from pizza import make_pizza as mp