# Лекция 2
   # Файлы
#    Хранение данных
#    Передача данных в клиент-серверных проектах
#    Хранение конфигов
#    Логирование действий
    #  Как работать с файлами:Связать файловую переменную с файлом, определив модификатор работы
    #  a – открытие для добавления данных
    #  r – открытие для чтения данных
    #  w – открытие для записи данных
    #  w+, r+ 


# colors = ['red', 'green', 'blue123']
# data = open('file.txt', 'a')
# #data.writelines(colors) # разделителей не будет
# data.write('\nLINE12\n')
# data.write('LINE13\n')
# data.close

# with open('file.txt', 'a') as data:
#     data.write('line3\n')
#     data.write('line4\n')

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

   # Функции

# import hello as h  # импорт функции из другого файла
# print(h.f(1))

# def new_string(symbol, count = 3):
#     return symbol * count
# print(new_string('!', 5))
# print(new_string('!'))
# print(new_string(5))

# def concatenatio(*params):
#     res = 0
#     for item in params:
#         res+= item
#     return res
# print(concatenatio('a', 's', 'd', 'w')) # asdw
# print(concatenatio('a', '1', 'd', '2')) # a1d2
#print(concatenatio(1, 2, 3, 4)) # TypeError: ...

  # Рекурсия

# def fib(n):
#  if n in [1, 2]:
#    return 1
#  else:
#    return fib(n-1) + fib(n-2)

# list = []
# for e in range(1, 10):
#  list.append(fib(e))
# print(list) # 1 1 2 3 5 8 13 21 34

   # Кортежи
   #Кортеж – это неизменяемый “список”
# (a) = (3, 1, 41, 4)   
# # print(a)
# # print(a[0])

# for item in a:
#     print(item)

# t = ()
# print(type(t)) # tuple
# t = (1,)
# print(type(t)) # tuple
# t = (1)
# print(type(t)) # int
# t = (28, 9, 1990)
# print(type(t)) # tuple
# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']
# t = tuple(colors) # преобразование списка в кортеж
# print(t) # ('red', 'green', 'blue')

# t = tuple(['red', 'green', 'blue'])
# # print(t[0]) # red
# # print(t[2]) # blue
# # # print(t[10]) # IndexError: tuple index out of range
# # print(t[-2]) # green
# # print(t[-200]) # IndexError: tuple index out of range
# for e in t:
#  print(e) # red green blue
# t[0] = 'black' # TypeError: 'tuple' object does not support item assignment


# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue)) # r:red g:green b:blue

   # Словари
    # Неупорядоченные коллекции произвольных объектов с доступом по ключу

# dictionary = {}
# dictionary = \
#     {
#         'up': '↑',
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#     }
# print(dictionary['up'])
# dictionary['up'] = 'up'
# print(dictionary['up'])
# print(dictionary)
# print(dictionary['left'])

# for k in dictionary:
#     print(k)

   # Множества

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }
# print(colors) # set()

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# print(c)
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
# print(u)
# i = a.intersection(b) # i = {8, 2, 5}
# print(i)
# dl = a.difference(b) # dl = {1, 3}
# print(dl)
# dr = b.difference(a) # dr = {13, 21}
# print(dr)

# q = a \
#  .union(b) \
#  .difference(a.intersection(b)) # {1, 21, 3, 13}

# s = frozenset(a) # неизменяемое множество

   # Списки

# list1 = [1,2,3,4,5]
# list2 = list1
# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)

# list1[0] = 123

# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e) 


# print(list1.pop(2)) # .pop удаляет последний элемент списка по умолчанию, если передать аргумент, то удалит элемент по этому индексу
# print(list1)

# list1.insert(2, 11) # добавляет элемент в список (индекс, добавляемый элемент)
# print(list1)

# list1.append(11) # .append добавляет элемент в конец списка
# print(list1)