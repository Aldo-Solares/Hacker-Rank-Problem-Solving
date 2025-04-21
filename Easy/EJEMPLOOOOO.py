from itertools import cycle
a = list(range(1,5))

def cycle(iterable):
    saved = []
    for element in iterable:
        yield element
        saved.append(element)

    while saved:
        for element in saved:
            yield element

Contador = cycle(a)
print(a)
print(next(Contador))
print(next(Contador))
print(Contador.close()) 