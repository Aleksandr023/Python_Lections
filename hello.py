# Лекция 1
    # Типы данных, переменные
# типы данных : int- целые числа, float- с плавающей точкой, boolean- логические, str- строки, list- массивы

#value = None
# print(type(a)) # type показывает тип переменной
# print(type(b))
#value = 12334
# print(type(value))
#a = 123
#b = 1.23
# s = 'hello, world' #\n - переход на новую строку, \' - добавит ' в строку
# print(s)
#print(a, '-', b, '-', s)
#print("{} - {} - {}".format(a, b, s))
#print(f"{a} - {b} - {s}")
#print("{1} - {2} - {0}".format(a, b, s))#

#f = True
# print(f)

# list = ['1', '2', '3'] # в массив можно включать переменнные разных типов, но лучше так не делать
#col = ['hello', 3.5, 45, True]
# print(list)
# print(col)

   # Ввод и вывод данных: print, input

# print("Введите a")
# a = input()
# print("Введите b")
# b = input()
# print(a,b)
# print("{} {}".format(a, b))
# print(f"{a} {b}")
# print(a, " + ", b, " = ", a+b)
# print("Введите a")
# a = int(input())
# print("Введите b")
# b = int(input())
# print(a, " + ", b, " = ", a+b)

   # Арифметические операции:
   # +, -, *, /, %, //, **

#  нет ограничений по хранению данных
# a = 1.31232
# b = 3
# c = round(a * b, 7) # округляет значение, по умолчанию по математическим правилам, можно передать аргумент(количество знаков после запятой)
# print(c)

# a = 3
# a = a + 5
# a +=5 # сокращенная операция присваивания, действительно для любых арифметических действий
# print(a)

   # Логические операции

# a = 1<4
# b = 1<4 and 5>2
# c = 1 != 2
# print(a, b, c)

# a = [1, 2] #"qwe"
# b = [1, 2] #"qwe"
# print(a == b)

# a = 1<3<5<4

# func = 1
# T = 4
# x = 2

# f = 1>2 or 4<6  # Дизюнкцией двух высказываний называется высказывание истинное тогда и только тогда, когда хотя бы одно из высказываний верно
# f = [1,2,3,4]
# print(f)
# print(not 2 in f)

# is_Odd = not f[0] % 2
# print(is_Odd)

    # Управляющие конструкции: if, if-else, while, for

   # if, if-else:

# a = int(input("a = "))
# b = int(input("b = "))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if username == 'Маша':
#  print('Ура, это же МАША!')
# elif username == 'Марина':
#  print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#  print('Ильнар - топ)')
# else:
#  print('Привет, ', username)

   # WHILE:

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //=10
#     print(original)
# else:
#     print("Пожалуй хватит)")
# print(inverted)

   # for:     for i in enumeration(i счетчик)

# list = [1,2,3,4, 10,5]
# r = range(10)
# for i in range(1, 10, 2):
#     print(i)

# r = range(100, 0, -20) # range(100, 0, -20) показывает i по убыванию с шагом -20
# for i in r:
#  print(i)
# # 100 80 60 40 20

   # Вложенные циклы:

# line = ""
# for i in range(5):
#   line = ""
#   for j in range(5):
#    line += "*"
#   print(line)

   # СТРОКИ

# text = 'съешь ещё этих мягких французских булок'
# print(len(text)) # 39 (len показывает длину, количество символов)
# print('ещё' in text) # True (показывает наличие подстроки в строке)
# print(text.isdigit()) # False (isdigits проверяет являются ли все знаки строки числами)
# print(text.islower()) # True (islower проверяет являются ли все символы строки символами нижнего регистра)
# print(text.replace('ещё','ЕЩЁ')) # (replace заменяет один элемент на другой)

# for c in text:
#  print(c)

# text = 'съешь ещё этих мягких французских булок'
# # print(text[0]) # c
# # print(text[1]) # ъ
# # print(text[len(text)-1]) # к
# # print(text[-5]) # б
# # print(text[:]) # print(text)
# # print(text[:2]) # съ
# # print(text[len(text)-2:]) # ок
# # print(text[2:9]) # ешь ещё
# # print(text[6:-18]) # ещё этих мягких
# # print(text[0:len(text):6]) # сеикакл
# # print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ..
# print(text)

   # СПИСКИ

# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# ran = range(1, 6)
# print(type(ran))
# num = list(ran)
# print(type(num))
#print(list(range(1, 6)))

# print(f'{len(numbers)} len')
# for i in numbers:
#     i*=2
#     print(i)
# print(numbers)

# colors = ['red', 'green', 'blue']
# for e in colors:
#   print(e) # red green blue

# for e in colors:
#   print(e*2) # redred greengreen blueblue

# colors.append('gray') # добавить в конец

# print(colors)# == ['red', 'green', 'blue', 'gray']) # True

# colors.remove('red') #del colors[0] # удалить элемент
# del colors[0] # удалить элемент
# print(colors)

    # ФУНКЦИИ

#def function_name(x):

def f(x):
    if x == 1:
        return "Целое"
    elif x == 2.3:
        return 23
    else:
        return


# arq = 2
# print(f(arq))
# print(type(f(arq)))




