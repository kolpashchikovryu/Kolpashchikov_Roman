my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for i in range(len(my_list)):
    #print(i)
    my_list[i] = list(my_list[i])
    #print(len(my_list[i]))
    #print(my_list[i])
       for j in my_list[i]:
           if '0' < j < '9':
               if len(my_list[i]) <= 2:
                print(j)
        #print(my_list[i])
    #print(type(my_list[i]))

