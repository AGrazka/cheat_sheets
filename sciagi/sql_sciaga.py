TYPY BAZ DANYCH
hierarchiczne 			# oparte na relacjacjach rodzic-dziecko
obiektowe 				# na zasadzie programowania obiektowego
relacyjne 				# skupiają się na relacjach między danymi, trzymane w dwuwymiarowych tabelach. 
						# każda kolumna to atrybut, a rząd to dane
nierelacyjne 			# dane jako para klucz-wartość

RELACJE W BAZACH DANYCH
jeden do jednego 		# relacja w której jeden el. z jednej tabeli, ma przyporządkowany jeden element z drugiej tabeli
jeden do wielu			# uczeń-klasa, uczeń w jednej klasie, ale klasa ma wielu uczniów
wielu do wielu			# nauczyciel-klasa, nauczyciel może uczyć wiele klas, klasa może mieć wielu nauczycieli

psql -h localhost -U postgres -W  # tworzy serwer, odpala psql
psql -h localhost -U postgres -W -d database_name 

pg_dump -U [user_name] -W -h [host] database > [file].sql 	# tworzyenie backupu

psql -U [user_name] -W -f [file_name] -h [host] database_name 	# wczytuje backup

from psycopg2 import connect	# łączenie się z bazą danych, wrzucamy do pythona
cnx = connect(user=<login>,
              password=<hasło>,
              host=<ip-serwera>,
              database=<nazwa-bazy>)

cnx.close()				# zamknięcie połączenia

from psycopg2 import connect, OperationalError	# przykładowe połączenie z pythona
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
username = "postgres"
passwd = "coderslab"
hostname = "127.0.0.1"  # lub "localhost"
db_name = "sql_cwiczenia"
try:
    cnx = connect(user=username, password=passwd, host=hostname, database=db_name) # tworzymy nowe połączenie
    cnx.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)	# pozwala na automatyczne commitowanie
    print("Połączenie udane.")          # do testowania połączenia
except OperationalError:
    print("Nieudane połączenie.")


CREATE DATABASE <nazwa_nowej_bazy>;  # w psql tworzy bazę danych

cursor = cnx.cursor()	# wysyła zapytania do bazy i je odbiera
cursor.execute(quaries)	# zadaje zapytanie

sql = "CREATE DATABASE sql_cwiczenia;"	# tworzenie nowej bazy przez pythona
try:
    cursor.execute(sql)
    print("Baza założona")
except:
    print("Błąd!")
cursor.close()			# 
cnx.close()				# dodajemy na samym końcu kodu lub kiedy kończymt pracę z bazą danych

DROP DATABASE <nazwa-bazy>      # usuwa bazę danych

"\l" 		# !!BEZ CUDZYSŁOWU!! pokazuje dostępne listy
q 		# żeby zamknąć

CREATE TABLE table_name	# zapytanie SQL tworzy nową tabelę
(
nazwa_kolumny_1 typ_danych(size) [atrybuty],
nazwa_kolumny_2 typ_danych(size) [atrybuty],
nazwa_kolumny_3 typ_danych(size) [atrybuty],
....
);

size 	# rozmiar wprowadzanej danej

TYPY DANYCH
LICZBY
integear	lub int 		# liczba
bigint					# dla dużych liczb
smallint				# mała liczbowa
real     				# zmiennoprzecinkowa do 6 liczb po,
double precision		# zmiennoprzecinkowa do 15 liczb po ,
decimal(m, d)			# m cyfr z czego d po ,
numeric(m, d)			# tak jak decimal

DATA I CZAS
date 					# data w formacie RRRR-MM-DD
timestamp				# data w formacie RRRR-MM-DD GG MM SS.mmm
timestamp with timezone # jak timestamp, ale przechowuje strefę czasową
time 					# GG:MM:AA
time with timezone 		# time ze strefą czasową
SERIAL
serial					# od 1, ale zwiększa się o 1 z każdym rekordem
bigserial				# od 1, większe liczby niż serial
smallserial				# od 1, mniejsze liczby  niż serial 

NAPISY
char(m)					# napis złożony z m znaków, jak podamy krótszy to dokłada spacje
varchar(m)				# zmienna ilość znaków, max m, nie uzupełnia się spacjami
text					# pole tekstowe o nieograniczonej długości

ATRYBUTY
primary key             # jednoznaczne identyfikowanie, zazwyczaj serial
unique                  # unikalna wartość w kolumnie
default                 # domyślna wartość w kolumnie
null / not null         # pozwala / nie pozwala na wprowadzenie pustych danych w kolumnę


CREATE TABLE "users"
(
user_id serial,         # każdy wpis ma kolejny numer, 
user_name varchar(255),
user_email varchar(255) unique, # w tej kolumnie e-mail nie może pojawić się więcej niż raz
PRIMARY KEY(user_id)    # user_id będzie kluczem głównym OBOWIĄZKOWE
);

"\c" <nazwa>            # !!BEZ CUDZYSŁOWU!! łączenie się do konkretnej bazy
"\dt"                   # !!BEZ CUDZYSŁOWU!! pokazuje wszystkie tabele
--                      # komentarze w sql

INSERT INTO users VALUES (0, 'Jacek', 'jacek@gmail.com');   # podstawia dane do kolumn
INSERT INTO users(user_name, user_email) VALUES('Wojtek', 'wojtek@gmail.com'); # POJEDYNCZY CUDZYSŁÓW!!


cursor.execute()        # wykonuje zapytanie

RETURNING <nazwa kolumny>   # zwraca wartość danej kolumny

SELECT column_name, column_name     # wczytuje podane kolumny
FROM table_name                     # z tej tabeli

SELECT * FROM table_name;   # wczytuje wszystkie kolumny z tabeli

for row in cursor:        # iteruje kursor i drukuje tuple wyników
    print(row)

sql = "SELECT user_id, user_name FROM users"
cursor.execute(sql)
for (id, name) in cursor:
    print("{} ma identyfikator {}".format(name, id)) # Wojtek ma identyfikator 1


from psycopg2.extras import RealDictCursor
 
crs = cnx.cursor(cursor_factory=RealDictCursor)
sql = ("SELECT user_id, user_name"
       "FROM users")
crs.execute(sql)
for row in crs:
    print(row)              # {"id": 1, "name": "Wojtek"} 

SELECT column_name, column_name 
FROM table_name
WHERE column_name = <szukana wartość>;  # zawęża wyszukiwanie

SELECT * FROM users             # wyszukuje wszystko zzaczynające się na W
WHERE user_name LIKE 'W%'       # % oznacza dowolne znaki

PORÓWNYWANIE
=                 # Równe
<> lub !=         # Nierówne
>(>=)             # Większe niż (większe równe niż)
<(<=)             # Mniejsze niż (mniejsze równe niż)
BETWEEN a AND b   # Pomiędzy podanym zakresem (wliczając podany zakres)
LIKE              # Szuka podanego wzorca (tylko napisy)
IN(a,b,c)         # Znajduje się w zmiennych podanych w nawiasach
NOT               # Może poprzedzać inne operacje
OR / AND          # Operatory logiczne łączące poszczególne wyrażenia
is null           # to gdzie brakuje danych

SELECT column_name AS column_alias  # wyciąga tabelę i zmienia jej nazwę
FROM table_name;

ORDER BY            # sortuje wyniki
ORDER BY column_name    # sortuje po nazwie

SELECT * FROM users ORDER BY name; # wyciąga wszystko i sortuje po nazwie

ORDER BY column_name ASC|DESC,  # można rosnąca albo malejąco
column_name ASC|DESC;

!!!!!!!!!! PRZED ZMIANAMI NAJLEPIEJ SPRAWDZIĆ DANE FUNKCJĄ SELECT !!!!!!!!!!!!!!!!


UPADETE <nazwa tabeli>          # zmiana wartości danych
SET column1=value2, column1=value2
...
WHERE some_column=some_value

UPDATE movie
SET name = 'Ice Age 2'
WHERE name = 'Ice Age';

DELETE FROM table_name      # usuwa dane
WHERE some_column=some_value;

ALTER TABLE <table_name> ADD  <table_name> <datatype>; # dodanie nowej kolumny
ALTER TABLE <table_name> DROP COLUMN <column_name>; # usunięcie kolumny
np.
ALTER TABLE movie  ADD COLUMN rating int NULL;

JOIN ... ON ...         # łączy tabele
INNER       # bierze część wspólną
LEFT        # bierze wszystko z lewej i rekordy z prawej
RIGHT       # bierze wszystko z prawej i rekordy z lewej
FULL

SELECT <column_name(s)> FROM <table1>   # LEWA TABELA
JOIN <table2>                           # PRAWA TABELA
ON <table1.column_name=table2.column_name>; # warunek

RELACJE
JEDEN DO WIELU
CREATE TABLE customers(         # nadrzędna
  customer_id serial NOT NULL,
  name varchar(255) NOT NULL,
  PRIMARY KEY(customer_id)
);

CREATE TABLE orders(            # podrzędna
  order_id SERIAL NOT NULL,
  customer_id int NOT NULL,
  order_details varchar(255),
  PRIMARY KEY(order_id),
  foreign key (customer_id) references customers(customer_id)
);

SELECT id, name, price, product.description, opinions.description FROM product # wyrzuca tylko podANE tabele
INNER JOIN opinions
  ON product.id = opinions.product_id;

JEDEN DO JEDNEGO        # nadrzędna
CREATE TABLE customers(
  customer_id serial NOT NULL,
  name varchar(255) NOT NULL,
  PRIMARY KEY(customer_id)
);

CREATE TABLE orders(    # podrzędna
  order_id SERIAL NOT NULL,
  customer_id int NOT NULL UNIQUE,
  order_details varchar(255),
  PRIMARY KEY(order_id),
  foreign key (customer_id) references customers(customer_id) ON DELETE CASCADE # usuwa wszystko powiązane wpisy
);

data = cursor.fetchone()    # wyrzuca jeden element

WIELE DO WIELU
CREATE TABLE items(             # nadrzędna
  item_id serial NOT NULL,
  description varchar(255),
  PRIMARY KEY(item_id)
);
CREATE TABLE orders(            # nadrzędna
  order_id SERIAL NOT NULL,
  customer_id int NOT NULL,
  order_details varchar(255),
  PRIMARY KEY(order_id),
);
CREATE TABLE items_orders(      # podrzędna
  id serial NOT NULL,
  item_id int NOT NULL,
  order_id int NOT NULL,
  PRIMARY KEY(id),
  FOREIGN KEY(order_id) REFERENCES orders(order_id),
  FOREIGN KEY(item_id) REFERENCES items(item_id)
);


dvwa    # aplikacja do ataków