#    Лекция № 4


x = 0
y = 0

def init(a, b):
    global x    # global x нужен что бы мы могли взаимодействовать с x вне функции
    global y 
    x = a
    y = b

def do_it():
    return x+y



