#Решение с новым списком
'''my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
my_list_new = []
for i in range(len(my_list)):
    my_list_new = my_list[i].split(' ')
    for j in range(len(my_list_new)):
        my_list_new[j] = my_list_new[j].capitalize()
    print(f'Привет, {my_list_new[j]}!')'''

#Решение без создания нового списка
my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in range(len(my_list)):
    my_list[i] = my_list[i].split(' ')
    for j in range(len(my_list[i])):
        my_list[i][j] = my_list[i][j].capitalize()
    print(f'Привет, {my_list[i][-1]}!')
