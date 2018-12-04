# LISTS
lis = []

lis.append("x")         # dodaje na końcu listy
lis.extend(["y"])       # rozszerza o inny iterowalny element
lis.insert(1, "x1")     # dodaje na konkretną pozycję
lis.remove("y")         # usuwa konkretny element
lis.pop(0)              # usuwa element z podanej pozycji i go zwraca
lis.clear()             # usuwa wszystkie elementy
lis.count("x")          # zlicza wystąpienia podanego elementu
lis.index("x1", 4)      # zwraca pozycję pierwszego elementu równego podanej wartości zaczynając od poz 4
lis.sort()              # sortuje elementy
lis.reverse()           # odwraca tabele
lis.copy()              # kopiuje tabele
del lis[0]              # usuwa element z pozycji 0

"""
stack - "last-in, first-out", używamy append i pop
queue - "first-in, first-out", from collections import deque, używamy append i popleft
list comprehensions - [x**2 for x in range(10) - składanie list
list comprehensions z warunkiem - [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

"""
# TUPLE
tup = ()                # tuple są niemodyfikowalne
tup += ("a", "b")       # dodawanie do tupli

# SETS
a = set("abacadb")      # zwraca zbiór znaków {'a', 'b', 'c', 'd' ale nie dubluje
b = set("dbxy")
print(a - b)            # zwraca litery z, których nie ma w b
print(a | b)            # zwraca litery z a lub b lub obu
print(a & b)            # zwraca litery występujące w a i b
print(a ^ b)            # zwraca litery z a i b, oprócz występujących w obydwu naraz
a = {x for x in 'abracadabra' if x not in 'abc'}  # set comprehension

# DICTIONARIES
dic = {1: "a"}

print(dic[1])           # zwraca wartość elementu o podanym kluczu
dic[2] = "b"            # dodaje element o kluczu 2 i wartości "b"
del dic[2]              # usuwa elementy o kluczu 2
list(dic)               # tworzy listę z kluczy
sorted(dic)             # sortuje elemnty listy ze słownika

dict([(1, "a"), (2, "b"), (3, "c")])  # tworzy słownik {1: "a", 2: "b", 3: "c"}


# SPOSOBY UŻYWANIA PĘTLI
for k, v in dic.items():  # pozwala dostać się do klucza i wartości jednocześnie
    print(k, v)

for i, v in enumerate(['a', 'b', 'c']):  # wypisuje z kolejnymi numerami
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):    # iteruje przez dwie pętle naraz
    print(f'What is your {q}?  It is {a}.')

for i in reversed(range(1, 10, 2)):  # iteruje od końca
    print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):   # iteruje przez posortowaną listę, nie zmienijąc początkowej
    print(f)

if __name__ == "__main__":
    print(lis.index("x1"))

