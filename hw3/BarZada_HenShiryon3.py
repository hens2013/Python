"""
written by :Bar Zada and Hen Shiryon

"""


# 1
def ex1A(n):
    sum = 0
    if n == 0:
        return True
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum >= n


def ex1B(lst):
    return {key: sum(1 for item in list(
        map(lambda item: [num for num in range(1, item) if item % num == 0], list(filter(lambda x: ex1A(x), lst)))) if
                     key in item) for item in list(
        map(lambda item: [num for num in range(1, item) if item % num == 0], list(filter(lambda x: ex1A(x), lst)))) for
            key in item}


def ex1C(num):
    is_primary = True
    for i in range(2, num):
        if num % i == 0:
            is_primary = False
            break
    if is_primary:
        return False

    return (item for item in range(1, num) if num % item == 0)


def ex1():
    # activte 1 A
    print(ex1A(12))
    # activte 1 B
    print(ex1B([28, 12, 64, 32]))
    # activte 1 C
    rc = ex1C(64)
    for i in rc:
        print(i)


# 2
def ex2A(lst):
    return {'c': list(filter(lambda item: type(item) == str, lst)),
            'i': list(filter(lambda item: type(item) == int, lst)),
            'f': list(filter(lambda item: type(item) == float, lst)),
            'o': list(filter(lambda item: type(item) != str and type(item) != int and type(item) != float, lst))}


def ex2B(func_list):
    from inspect import signature
    return list(filter(lambda func: len(signature(func).parameters) <= 1, func_list))


def f1(a, b):
    pass


def a(a):
    pass


def a2(a):
    pass


def ex2():
    lst = ['a', 5, 'g', 9.4, 3, 9.9]
    print(ex2A(lst))

    func_list = [f1, a, a2]
    print(ex2B(func_list))


# 3
def decorator(func):
    avg_tupple = (0, 0)
    outPut = []
    input = []

    def wrapper(*args, **kwargs):
        nonlocal avg_tupple, outPut, input
        input.append(args[0])
        outPut.append(func(*args, **kwargs))
        avg = list(avg_tupple)
        avg[0] = sum(input) / len(input)
        avg[1] = sum(outPut) / len(outPut)

        avg = tuple(avg)
        print(avg)
        return func(*args, **kwargs)

    return wrapper


@decorator
def ex3A(num):
    return int(num)


def logged(fun):
    data = []

    def wrapper(*args, **kwargs):
        nonlocal data
        result = fun(*args, **kwargs)
        inputs = [str(arg) for arg in args] + [kwarg for kwarg in kwargs]
        data.append({"inputs": inputs, "outputs": result, "name": fun.__name__})
        print("You called {}({}) it returned {}".format(data[-1]['name'], ", ".join(data[-1]['inputs']),
                                                        data[-1]['outputs']))
        return result

    return wrapper


def f():
    print("f")


@logged
def ex3_2(a, b, c, d):
    d()
    return a + b + c


def ex3():
    for i in range(20):
        ex3A(i)

    ex3_2(1, 2, 3, f)
    ex3_2(4, 5, 6, f)


# 4
list_func = []


def print_dec(func):
    def wrapper(*args, **kwargs):
        global list_func
        list_func.append(func.__name__)

        if len(list_func) > 2:
            func_list = list_func[-3:]
            print(list_func)
        return func(*args, **kwargs)

    return wrapper


@print_dec
def f1():
    print("1")


@print_dec
def f2():
    print("2")


@print_dec
def f3():
    print("3")


@print_dec
def f4():
    print("4")


def ex4():
    f1()
    f2()
    f3()
    f4()


# 5
class Observer(object):

    def notify(self, msg):
        print(msg)


class Twitter(Observer):
    def __init__(self, name):
        self.name = name
        self.observers = []

    def follow(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        return self

    def tweet(self, msg):
        for observer in self.observers:
            observer.notify(msg)


def ex5():
    a = Twitter('Alice')
    k = Twitter('King')
    q = Twitter('Queen')
    h = Twitter('Mad Hatter')
    c = Twitter('Cheshire Cat')
    a.follow(c).follow(h).follow(q)
    k.follow(q)
    q.follow(q).follow(h)
    h.follow(a).follow(q).follow(c)

    print(f'==== {q.name} tweets ====')
    q.tweet('Off with their heads!')
    print(f'\n==== {a.name} tweets ====')
    a.tweet('What a strange world we live in.')
    print(f'\n==== {k.name} tweets ====')
    k.tweet('Begin at the beginning, and go on till you come to the end: then stop.')
    print(f'\n==== {c.name} tweets ====')
    c.tweet("We're all mad here.")
    print(f'\n==== {h.name} tweets ====')
    h.tweet('Why is a raven like a writing-desk?')


if __name__ == '__main__':
    # ex1()

    ex2()
# ex3()
# ex4()
# ex5()
