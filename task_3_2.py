num = 'Six'
str_num_dict = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'}
if num in str_num_dict:
    print(str_num_dict[num])
for i in str_num_dict:
    if i.title() == num:
        print(str_num_dict)

