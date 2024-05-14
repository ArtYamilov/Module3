# Пространство имен.
a = 15  # находятся в глобальном пространстве имен.
b = 25


def printer():
    global a, b
    a = 'Str'  # из локального пространства имен можно обращаться в глобальное.
    b = 'Str 2'
    c = 20
    d = 40
    print(c, d, 'local')  # локальное пространство имен.
    print(a, b, 'global')


print(a, b)  # глобальное пространство имен.
printer()
print(a, b)


# Способы вызова функции по умолчанию
def print_params(a, b, c):
    print(a, b, c)


print_params('True', True, 1)


def print_params(a=1, b=2, c=3):
    print(a, b, c)


print_params()


def print_params(a=1, b=2, c=3):
    print(a, b, c)


print_params(3, 2, 1)  # переопределение параметров, позиционные параметры - в случае записи по порядку.


def print_params(a=1, b=2, c=3):
    print(a, b, c)


print_params(2, 5, c='String')  # c - именованный параметр.


def print_params(a, *, b, c):  # * - означает, что параметр a - позиционный параметр, остальные именованные.
    print(a, b, c)


print_params(2, b=5, c='String')  # c - именованный параметр.


# Домашняя работа.
def test():
    a = 'dc'
    b = 'marvel'
    print(a, b)


test()


def test2(me, you):
    print(me, you)


test2('student', 'mentor')
