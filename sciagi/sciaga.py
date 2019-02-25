print ('...')						# wypisywanie

%									# reszta z dzielenia

**									# potęgowanie

False = 0 = "" = None = [] = {}		# logiczna wartość fałsz

round(co, do którego miejsca)		# zaokrąglanie

int(..)								# zmienia string na zmienną całkowitą
float(..)							# zmiana liczby na zmiennoprzecinkową
list(..)							# lista z liter ze słowa
str(..)								# słowo z liczby, lub listy

string * n 							# wyświetli string n razy

def nazwa(x,y):						# definicje
	return

def nazwa(x,y, z=2):					# definicje, z jest parametrem opcjonalnym, 
	return							# jak mu nic nie przypiszemy to przyjmuje wartość podaną
	

while warunek:						# wykonuje instrukcje dopóki spełniony jest warunek
	pass	

if warunek:							# wykonuje instrukcje jeśki spełniony jest warunek
	pass							# pozwala ominąć blok, nic nie robi, pomija
else:								# jeśli piewrszy jest niespełniony
	pass
elif warunek:					    # jeśli nie spełnia pierwszego a spełnia podane
	pass

break								# wychodzi z pętli

continue							# pomija jeeden cykl pętli

len(..)								# liczba elementów w liście

<list>.append(..)					# dodaje element do listy

+									# łączy listy

x.find(a, n)						# szukanie "a" w 'x' od miejsca n

for x in list:						# wykonuje operacje dla kolejnych elementów listy
	pass

"\n".join(list)                     # łaczy wszystko z listy w napis i wyrzuca w różnych linijkach                   

x.union(y)							# łączy listy, ale nie dubluje elementów

list.index(..)						# zwraca pozycję elementu w liście

.. in ..							# sprawdza czy element jest w liście (True/False)

.. not in .. = not..in..			# sprawdza czy elementu ma w liście

list.pop()							# przypisuje ostatni element i usuwa go z listy
list.pop(pos)							# wyciąga element z pozycji 

<string>.split()					# zwraca listę ze słowami ze string

# blabla							# dodaje komentarz, DWIE SPACJE JEZELI JEST ZA INSTRUKCJĄ

"""		
	...								# komentarze w kilku liniach 
		"""

for x in range(1,10):
for x in range(start,stop-1)		# wykonuje insstrukcje dla elementów z zakresu
	pass

Dictionaries						# słownik przypisują każdy element ma przypisaną wartość
nazwa = {							# jest nieuporządkowana
	el1:1, 
	el2:2, 
	el3:3
}

nazwa['el1']						# zwraca wartość dla elementu
nazwa['el4'] = 4					# dodaje nowy elememt
nazwa['el'][pozycja]				# zwraca element na pozycji w liście "el"

del()								# usuwa wszwystko w pythonie, nawiasy nie są konieczne
		
ord(litera)							# zmienia znak na liczbę
chr(liczba)							# zmienia liczbę na znak

#!/usr/bin/python					# magiczny komentarz, instrukcja do uruchomienia pliku konkretnym programem

a = input("Input something: ")		# pozwala wprowadzić dane z klawiatury i przypisać im zmienną

instrukcje
XOR									# zwraca True jeśli jeden z dwóch jest spełniony, inaczej False

a = (1, 2, 3)						# tupla, krotka, tylko do odczytywania
*args								# tupla, kolekcja, pozwala wprowadzić wiele danych do funkcji
									# może być tylko jeden, z dowolną nazwą i zawsze na końcu

def suma(*args):					# można wprowadzić wiele danych do funkcji
	result=0
	for element in suma:
		result += element
	return result
		
**kwargs							# słownik, nazwa argumentu z wartością, można podawać kilka	

/<znak>								# kolejny znak po "/" jest wyświetlany taki jaki jest

global zmienna						# używa globalnej zmiennej, a nie tej z funkcji

lista[początek:koniec]				# pobiera fragment listy, lewostronnie zamknięty, z prawej nie bierze końca

lista[początek:koniec:skok]			# pobiera dany co skok
lista[początek:koniec:-1]			# pobiera dane od końca
lista[::-1]							# odwraca tabelę

lista[index] = nowa_wartość			# podmiena wartość argumentu
lista.append(nowa_wartość)			# dodaje nową wartość do listy

a = [to_co_robimy_z_kolejnymi_elementami for i in range(0,20)]		# tworzy listę i z zakresu

[i for i in range(0, 18) if i % 3 == 0] 	# wyświetla liczby z zakresu podzielne przez 3

for h in star_wars:					# wypisuje klucz, a za nim wartość
	print(h, star_wars[h])

print(a, b, sep=": ")				# separator

# -*- coding: utf-8 -*-				# magiczny komentarz do pythona2, które wczytuje polskie znaki

shift + f6							# w pycharmie pozwala zmienić nazwę zmiennej wszędzie gdzie występuje

FORMATOWANIE NAPISÓW
PYTHON2
tpl = "%s is a %s"					# do %s wstawiane są wartości z tupli po %
tpl = "%s is a %s" % ("Harry", "wizard")

hobbit = {							# to samo co wyżej tylko dla słowników
    "name": "Bilbo Baggins",
    "occupation": "burglar"
}
description = "%(name)s is a %(occupation)s." % hobbit

PYTHON2 I PYTHON35
description = "{} is a {}.".format("Gandalf The Grey", "wizard")
	
PYTHON36
name = "Han Solo"
occupation = "smuggler"
description = f"{name} is a {occupation}."

MODUŁY								# normalny plik pythona, przyjmuje nazwę pliku bez rozszerzenia
									# pozwala wykorzystywać dane, funkcje z innego pliku

import <nazwa>						# importowanie modułu

nazwa_moduł↓.funkcja_z_modułu(parametry)			# wywołuje funkcję z modułu

from nazwa_moduł↓ import funkcja1_z_modułu, funkcja2_z_modułu 			# importuje konkretną funkcję z moduł↓ 

funkcja_z_modułu(parametry)			# po wywyłaniu konkretnej funkcji z modułu

import nazwa as nazwa2				# importuje bibliotekę ale zmienia jej nazwę

__name__							# dunder name, zmienna magiczna,  tylklo do odczytywania, przyjmuje nazwę modułu
									# lub nazwę modułu w którym się odwołujemy do innych plików

if __name__ == "__main__":			# pozwala na wykonywanie programu tylko jak jest on uruchomiony, a nie wczytywany
	pass 							# z modułu, może służyć do uruchamiania testów

pip freeze > requirements.txt		# w terminalu tworzy plik z biobliotekami
pip install -r <nazwa-pliku>		# w terminalu, instaluje bibliotekami

BIBLIOTEKA 
my_package
  +-- __init__.py
  +-- my_module1.py
  +-- my_module2.py
  +-- my_module3.py


ŚRODOWISKO WIRTUALNE
python2 - virtualenv <nazwa_katalogu>		# tworzy środowisko wirtualne
python3 - virtualenv -p python3 <nazwa_katalogu>	

source <nazwa_katalogu>/bin/activate		# aktywuje środowisko wirtualne, zmieniając ścieżkę dostępu do programu
. <nazwa_katalogu</bin/activate

BLĘDY I WYJĄTKI
try:								# pozwala wykonać osobne instrukcje dla 
	instrukcje, które mogą
	spowodować błąd
except <typ-błędu>:					# reakcja na konkretny typ błędu
	instrukcje, które reagują
	na błąd
np.
array = [1, 2]
try:
    print(array[5])
except IndexError:  
    print("Element nie istnieje.")

except (ValueError, ZeroDivisionError):		# można kumulować błędy w tupli, jeżeli mają dawać ten sam wynik
    return None

raise <typ-błędu>("komunikat błędu")		# wyrzuca wyjątek, prokuruje bład, zgłaszax

DEKORATORY								# trochę jak moduły, dodatkowe funkcje
@<nazwa_decoru>						# rozszerza zachowanie funkcji w trakcie działania programu
def fun():
	result = None
	# instrukcje
	return result
np.									# przed instrukcją sprawdza czy użytkownik jest zalogowany,
@login_required						# jak nie to wykonuje funkcję z dekoratora
def home(request)					# jak tak to pozwala na dostęp
	return (...)

DOCSTRINGS							# do tworzenia dokumentacji kodu
def jedi_farewell(name):
    """Return jedi farewell.		# w komentarzu piszemy co funkcja robi
 
    :param name: string				# typ wprowadzanej danej
    :return: farewell with name 	# w PyCharmie trzy " i enter
    """
    return "May the Force be with you, " + name


PROGRAMOWANIE OBIEKTOWE
class ClassName:					# klasa w pythonie zawsze PascalCasem
	# tutaj znajdzie się ciało klasy
	pass
s = Sith()							# dodaje obiekt s do klasy Sith
n = Sith()							# dodaje obiekt n do klasy Sith

s.name = "jakaś nazwa"				# tworzy atrybut name dla obiektu klasy
print(s.name)						# odwołanie do atrybutu

class Sith:							# domyślny atrubut KLASY, który obiekty przyjmują na start
	force_side = "dark"				# jak się zmieni później atrybut el. to nie pobiera tego domyślnego


class ClassName:					# klasa w pythonie zawsze PascalCasem
	def print_info(self): 			# metoda klasy (self) jest OBOWIĄZKOWE, jest adresem zwrotnym
		print("Sith!")

class Sith:
    name = "Sheev Palpatine"
    job = "chancellor"
    __sith_name = "Darth Sidious"
    def print_info(self):			# wydrukuje podane niżej
    	print("Sith!")
        print(self.name, self.job)	# odwołanie to samej siebie

MAGICZNE METODY
def __init__(self):					# jest "konstruktorem"(inicjalizator), jest wywoływana pza każdym razem jak dodamy nowy obiekt
	pass

def __str__(self):					# nadpisuje funkcje str() 
	pass

def __str__(self):                  # jak drukujemy model, to wyświetli jego name
    return self.name

def __init__(self, x, y, color):	# definiuje dane na start
    self.x = x
    self.y = y
    self.color = color

DZIEDZICZENIE						
class Book:							# tworzy klasę Book i przypisuje wartości
    name = "Hobbit"
    price = 35.95
    author = "John R.R. Tolkien"
class Ebook(Book):					# przejmuje wszystkie atrybuty klasy Book i dodaje swoje
    size_in_mb = 12					# jak nie ma swojego konstruktora to używa konstruktora rodzica

def __init__(self, title, author, size):			# wymusza użycie konstruktora rodzica, atrybuty rodzica i te dodatkowe
    super(EBook, self).__init__(title, author)		# wywołujemy rodzica klasy EBook, w miejscu gdzie jesteśmy

def print_book_info(self):
        super(EBook, self).print_book_info()	# bierze metodę z rodzica, w tym przypadku drukuje, tytuł autora i cenę
        print(self.size_in_mb)					# drukuje dodatkową informację o rozmiarze

MODYFIKATORY DOSTĘPU 				# wszystkie są publiczne w pythonie, ma na to wpływ konwencja
public								# dostępny z każdego miejsca
_protected							# dostępny w klasie i podklasach
__private							# niedostępny z zewnątrz ani podklasach

GETTERY I SETTERY
class Human:						# tworzenie danej tylko do odczytu
    def __init__(self, bt):
        self.__blood_type = bt
    def get_blood_type(self):		
        return self.__blood_type

class Human:						# w pythonie robimy tak
    def __init__(self, bt):
        self.__blood_type = bt
    @property						# dekorator, który pozwala dostać się do metody jak do właściwość
    def blood_type(self):			# bardzo użyteczne, dynamicznie zmienia wartość, jak zmienimy składowe
        return self.__blood_type	# np. przy zmianie nazwiska  
    @blood_type.setter 				# setter, nie wiem co tu napisać, pozwala zmieniać wartość
    	pass 

METODY KLASOWE I STATYCZNE
@classmethod						# metoda klasowa, wywołujemy ją na klasie, nie na obiekcie
def get_name(cls):					# można wykorzystywać zmiennd klasowd
	print(cls.name)

@staticmethod						# metoda statyczna, lokalna dla klasy, działa jak zwykła funkcja
def function():
	pass

ITERATORY							# klasa po której można iterować
__iter__()							# zwraca instancje iteratora
__next__()							# ma zwracać kolejny element z listy
raise StopIteration					# wyjątek o końcu iteratora

class Numbers:						# klasa Numbers jest iteratorem zwracającym liczby od 1 do 5
    def __iter__(self):
        self.counter = 0
        return self
    def __next__(self):
        if self.counter >= 5:
            raise StopIteration
        self.counter += 1
        return self.counter
for num in Numbers():
    print(num)

GENERATORY							# generator jest jednorazowy, wyrzuca dane i trzeba go na nowo definiować
def jedi_generator():				# tworzy generator który wyrzuca imiiona jedi
    jedis = ["Obi-Wan",
             "Anakin",
             "Qui-Gon",
             "Yoda",
             "Luke"]
    for person in jedis:			# tworzy yield dla każdej person
        yield person				# yield jak return, który nie końcczy funkcji
 
for jedi in jedi_generator():
    print(jedi)

def generate_numbers():				# 
	yield 1
	yield 2
	yield 3
a = generate_numbers()
for x in a:
	print(x)

power = (2 ** i for i in range(0, 11))	# to samo co funkcja wcześniej
for element in power:
    print(element)


tuple(fib(16))[-1]
import re

WYRAŻENIA REGULARNE					# inaczej regex, do wyszukiwania łańcuchów tekstowych
a 			# szuka literki a, każdy znak reprezentuje sam siebie
ab 			# szuka łancucha ab dokładnie w takiej kolejności
.  			# dowolny znak z wyjątkiem nowej linii
ci.			# np. cię, cił
.ja 		# np. oja, _ja
[a-c]		# przedział od a do c
ci[ęł]		# cię, cił, ale nie cis
[a-ząłć]	# od a do z i dodatkowo ą ł ć
[^...]		# dowolny znak z wyjątkiem
[^abc]		# dowolny znak wyjątkiem a b c 
|			# lub
a|b|c 		# a lub b lub c
^			# początek wiersza, stringa
$ 			# koniec wiersza
*			# zero lub więcej wystąpień
[abc]*		# zero lube więcej znaków ze zbioru a, b, c
+			# jedno wystąpienie lub więcej poprzedzającego wyrażenia
[abc]+		# jedno lub więcej znaków ze zbioru a b c
?			# nie ma albo jest raz
CUDZYSŁÓW JEST NIEPOTRZEBNY W NASTĘPNYCH
"\."		# to szukanie kropki \. 
"\.+"		# więcej niż jedna kropka,
"\d"		# Dowolna cyfra
"\D"		# Dowolny znak niebędący cyfrą
"\s"		# Dowolny znak biały (np. spacja, tabulator)
"\S"		# Dowolny znak niebędący znakiem białym
"\w"		# Dowolny znak wyrazu
"\W"		# Dowolny znak niebędący znakiem wyrazu
"\n"		# Nowa linia
"\t"		# Tabulator
"\r"		# Powrót karetki
{N}			# Dokładnie N wystąpień
{N,}		# Co najmniej N wystąpień
{N,M}		# Od N do M wystąpień

r"1. Linia\n2. Linia" # raw string

re.search	# moduł i unkcja do wyszukiwania
line = "Luke, I am your father!"
result = re.search(r'your', line)	# szuka słowa your w line
print(result)						# <_sre.SRE_Match object; span=(10, 14), match='your'>
print(result.group())				# grupa to wyrażenia ograniczpne () w regexie

line = "Luke, I am your father!"
result = re.match(r'Luke', line)	# sprawdza tylko pierwszy element
print(result)
print(result.group())
 
result = re.match(r'your', line)	# ja nie ma na pierwszym miejscu to zwraca None
print(result)

result = re.findall(r'\d', line)	# wyszukuje wszystkie wystąpienia i zwraca listę wyników
print(result)

(?P<etykieta>...) 					# przypisuje etykiety
(?P=etykieta)						# odwołanie do etykiety

result = re.search(r'luke', line, re.I)	# re.I - ignorecase, ignoruje wielkość znaku
print(result)						# wyszuka Luke


