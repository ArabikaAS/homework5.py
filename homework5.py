

immutable_var = "student", 10, 25, True
print(immutable_var)
#immutable_var [0] = "new" # кортеж не поддерживает обращение по элементам
#print(immutable_var) #ошибка

mutable_list = ["zero", 1, 2, True]
mutable_list[3] = "new3"
print(mutable_list)