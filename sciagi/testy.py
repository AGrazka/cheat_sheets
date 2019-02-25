i = 0
while True:
    i += 1
    assert i < 3, "Za duża liczba"		# służy do sprawdzania
    print("i = %s, idę dalej." % i)


def add(a, b):	# definicja funkcji
    return a + b
 
def test_add():	# definicja programu testującego
    assert add(2, 2) == 4
 
test_add()		# wywołanie testu

test1.py 		# odpalamy: python3 test.py
import unittest	
class MyFirstTest(unittest.TestCase): # musi dziedziczyć po klasie TestCase
    def test_to_fail(self):		# testy dobrze nazywać tak żeby było wiadomo co poszło nie tak
        self.assertTrue(False)	# assertTrue() jest obowiązakowe
    def test_to_be_ok(self):	# nazwa zaczyna się od 'test'
        self.assertEqual(2 * 2, 4)	# assertEqual() jest obowiązkowe
if __name__ == "__main__":
    unittest.main()

.F 		# kropka oznacza, że test zwróicł pożądaną wartość, F, że nie zwrócił pożądanej wartości
========================================
FAIL:test_to_fail (__main__.MyFirstTest)
----------------------------------------
Traceback (most recent call last):
File "test1.py",line 6, in test_to_fail
  self.assertTrue(False)
AssertionError: False is not true
-----------------------------------------
Ran 2 tests in 0.000s
FAILED (failures=1)

assetTrue # sprawdza czy podany argument zwraca True
assertRaises(exc, fun, *args, **kwargs) # sprawdza czy fun(*args, **kwargs) wyrzuca wyjątek
assertRaisesRegex(exc, r, fun, *args, **kwargs) # sprawdza czy fun(), zwraca wyjątek pasująy do wyrażenia regularnego r


Programowanie TDD (zwinne):
1. test automatyczny
2. program, który przejdzie testy
3. poprawianie kodu, aż spełni wszystkie wymagania

Cztery złote zasady TDD:
1. Dodawaj kod, gdy czerwone
2. Usuwaj kod, gdy zielone
3. Usuwaj duplikaty
4. Poprawiaj złe nazwy

Dorbe testy:
1. Niezależne od środowiska i innych testów
2. Szybkie
3. Powtarzalne, zwracające te same wyniki
4. Na bieżąco z kodem (gdy zmienia się funkcjonalność, zmieniają się testy)
5. Krótkie
6. Odporne na zmiany innych części naszej aplikacji


class TestExc1(TestCase):	# do testowania na obiekcie, FIKSTURA
def setUp(self):	# tworzy obiekt do testu
    self.padawan = Padawan.objects.create(name="Anakin",year_at_academy=1,
                                          is_active=True)

def test_padawans_name(self):	# wykonuje test
    self.assertEqual(self.padawan.name, "Anakin")

def tearDown(self):	#usuwa obiekt testowy
    self.padawan = None

from django.test import Client
c = Client() # tworzy obiekt Client
response = c.post('/login/', {'username': 'anakin', ... 'password': 'P@dme01'}) # twprzy argumenty
response.status_code # wysłanie danych logowania postem
200	# odpowiedź ok
response = c.get('/academy/exams/')
response.content # wysyła dane getem
b'<!DOCTYPE html...'

response = c.get('/jedi/details/', {'name': 'anakin'}) # żadanie getem

response = c.post('/jedi/remove/',{'name': 'ahsoka.tano'}) # tworzy żadanie post

c.login(username='obi.wan', password='maul.sucks') # symuluje logowanie
c.force_login(user='obi.wan') # loguje bez sprawdzania hasła
c.logout() wylogowuje 

import unittest			# testy na kliencie
from django.test import Client
class SimpleTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()  # Każdy test potrzebuje klasy Client().
    def test_details(self):
        response = self.client.get('/sith/list/')  # Pobieramy stronę metodą GET.
        self.assertEqual(response.status_code, 200) # Czy odpowiedź HTTP to 200 OK.
        # Czy widok zwrócił w kontekście DOKŁADNIE 2 Sithów?
        self.assertEqual(len(response.context['sith']), 2)

python -m unittest test_module1 test_module2 # uruchamia testy z dwóch modułów
python -m unittest test_module.TestClass # uruchamia testy z klasy w module
python -m unittest test_module.TestClass.test_method # uruchamia metode klasy z moduł↓


class MyTestCase(unittest.TestCase):
    @unittest.skip("Tak działa przeskakiwanie testów") # omija testy
    def test_nothing(self):
        self.fail("powinien zostać ominięty")
    @unittest.skipIf(mylib.__version__ < (2, 0),"Nie wykonuje się w wersji < 2.0")
    def test_format(self):
        pass
    @unittest.skipUnless(sys.platform.startswith("win"), "tylko dla Windows")
    def test_windows_support(self):
        pass