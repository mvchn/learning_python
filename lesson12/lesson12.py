
list_example = ['value1', 'value2', 'value3']

dict_example = {
    'key0' : ['value1', 'value2', 'value3'],
    'key1' : ['value4', 'value5', 'value6'],
    'key2' : ['value7', 'value8', 'value9']
}

a = dict_example.get('key01', 0)
print(a)

del dict_example['key2']

print(dict_example)

