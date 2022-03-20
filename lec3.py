#   Лекция №3
#      lambda

# def f(x):
#     return x**2
# # g = f
# # print(f(2))
# # print(g(2))

# def calc1(x):
#     return x+10
# # print(calc1(10))

# def calc2(x):
#     return x*10
# # print(calc2(10))

# def math(op, x):         # передаем функцию в качестве аргумента другой функции
#     print(op(x))

# math(calc1, 10)
# math(calc2, 10)


# def sum(x, y):
#     return x + y

# sum = lambda x, y: x + y

# def mylt(x, y):
#     return x * y    

# def calc(op, a, b):
#     # return op(a,b)
#     print (op(a,b))

# calc(lambda x, y: x + y,4,5)

#        List Comprehension

# list = []

# for i in range(1, 101):
#     #if(i%2 == 0):
#     list.append(i)

# print(list)

# def f(x):
#     return x**3

# list = [(i, f(i)) for i in range(1,21) if i%2==0]
# print(list)

# path = 'C:\\Users\\Семья\\Desktop\\Study\\05_Python\\Lections\\file.txt'
# f = open(path, 'r')                                                   # это не работает?
# data = f.read() + ' '
# f.close()

# numbers = []

# while data != ' ':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos+1:]

# out = []
# for e in numbers:
#     if not e%2:
#         out.append((e, e**2))
# print(out)

# def select(f, col):                                      # эта функция не нужна при использовании функции map
#     return[f(x) for x in col]

# def where (f, col):
#     return [x for x in col if f(x)]                      # эта функция заменяется готовой функцией filter

data = '1 2 3 5 8 15 23 38'.split()

res = map(int, data)
res = filter(lambda x: not x%2, res)
res = list(map(lambda x: (x, x**2), res))
print(res)

# li = [x for x in range(1, 21)]
# li = list(map(lambda x:x+10, li))

#                   Функция map
#         применяет указанную функцию к каждому элементу итерируемого объекта и возвращает итератор с новыми объектами

# data = list(map(int, '1 2 3'.split()))

# for e in data:
#     print (e)

# print('--')

# for e in data:
#     print (e)

#                 Функция filter

# data = [x for x in range(10)]
# res = list(filter(lambda x: not x%2, data))
# print(res)

#                Функция zip  
#    применяется к набору итерируемых объектов и возвращает итератор с кортежами из элементов входных данных. 
#    Количество элементов в результате равно минимальному количеству элементов входного набора.

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111,222,333]
data = list(zip(users, ids, salary))
print(data)

#              Функция enumerate
#     применяется к итерируемому объекту и возвращает новый итератор с кортежами из индекса и элементов входных данных

data = list(enumerate(users))
print(data)

