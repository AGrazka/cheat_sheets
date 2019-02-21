s = "abc"
it = iter(s)  # tworzy iterator
next(it)  # wywołuje kolejny element iteratora


def reverse(data):  # tworzy generator
    for index in range(len(data)-1, -1, -1):
        yield data[index]


for char in reverse('golf'):
    print(char)


test = "test abc cba brrrum aaa aaa czz asc"


def my_split(tekst):
    result = []
    blank = tekst.index(" ")
    while blank != -1:
        result.append(tekst[:blank])
        tekst = tekst[blank+1:]
        try:
            blank = tekst.index(" ")
        except ValueError:
            break

    result.append(tekst)

    return result


print(my_split(test))
