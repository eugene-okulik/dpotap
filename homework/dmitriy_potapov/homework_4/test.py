my_dict = {
    'tuple': (2, 4, 6, 8, 10),
    'list': [1, 3, 5, 7, 9],
    'dict': {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5},
    'set': {10, False, "text", 20, True}
}
print("Последний элемент в кортеже:", my_dict['tuple'][-1])

my_dict['list'].append(60)
poped = my_dict['list'].pop(1)

my_dict['dict'][('i am a tuple',)] = 'value'
popedd = my_dict['dict'].pop('two')

my_dict['set'].add("text_2")
my_dict['set'].remove(True)

print(my_dict)
