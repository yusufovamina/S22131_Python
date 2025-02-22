'''
#Iterator
list = [1, 2, 3]
iterator = iter(list)

print(next(iterator)) #1
print(next(iterator)) #2
print(next(iterator)) #3
print(next(iterator)) #StopIteration


for elem in iterator:
    print(elem)

for elem in iterator:
    print(elem)

    '''

'''
#Замыкание
#функция которая запоминает значение переменных из своей внешней обертки(outer)
def outer(x):
    def inner(y):
        return x + y
    return inner

closure = outer(10)
print(closure(5))
'''


#Decorator
# функция, которая принимает другие функции в качестве аргументов
# и возвращают новую функцию, изменяя или расшииряя исходную функцию
def decorator(func):
    def wrapper():
        print(func().upper())
    return wrapper()


@decorator
def greet():
    return "Murad!"
