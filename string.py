x = "blabla\n"
f"{x}"
"{}".format(x)

repr(x)  # zwraca dokładnie to co w x czyli np.: "" dla str

f"{x:10}"  # 10 po : oznacza minimalną wyświetlaną liczbę znaków po
f"{x:10d}"  # 10 po : oznacza minimalną wyświetlaną liczbę znaków przed


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098
Sjoerd: 4127
Dcab: 8637678


x.rjust(1)  # wyrównuje string do prawej w nawiasie
x.ljust(1)  # wyrównuje string do lewej
x.center(1)  # wyrównuje string do środka

