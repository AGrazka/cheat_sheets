s = "abc"
it = iter(s)  # tworzy iterator
next(it)  # wywołuje kolejny element iteratora


def reverse(data):  # tworzy generator
    for index in range(len(data)-1, -1, -1):
        yield data[index]


for char in reverse('golf'):
    print(char)
