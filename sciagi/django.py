django-admin <command> [options]
startproject 	# tworzy nowy projekt Django,
runserver		# uruchamia serwer testowy,
startapp		# tworzy nową aplikację wewnątrz projektu,
makemigrations	# tworzy skrypt migrujący bazę danych,
migrate 		# uruchamia skrypty migrujące bazę danych.

django-admin startproject <nazwa-projektu> <ścieżka-do-projektu>	# tworzenie projektu
django-admin startproject coderslab .								# tworzenie katalogu w miejscu gdzie jeteśmy

python manage.py runserver					# uruchamia serwer testowy na porcie 8000
python manage.py runserver <numer-portu>	# uruchamia serwer testowy na podanym porcie

python manage.py runserver <ip>:<port>		# udostępnianie serwera

SETTINGS
DEBUG 			# jeśli TRUE to ustawia aplikację na tryb deweloperski, w produkcji FALSE
BASE_DIR		# ścieżka dostępu do projektu
INSTALLED_APPS	# zainstalowane aplikacje
DATABASES		# konfiguracja baz danych używanych przez projekt
STATIC_URL 		# URL pod jakim będą serwerowe pliki, assety, na pliki, które leżą obok i się nie zmieniają

python manage.py migrate			# startowe migracje dla nowego proejtku Django

sqlite3 <nazwa pliku>				# program to obsługi plików sqlite3 z terminala

python manage.py startapp <nazwa-aplikacji>	# tworzenie nowej aplikacji, nazwa musi być inna niż katalog
W setting.py do listy INSTALLED_APPS trzeba dopisać utworzoną aplikacje

w pliku views.py 
from django.http import HttpResponse

URL w urls.py
url(r'^articles$', views.articles, "articles")
re_path(r'^articles$', views.articles, "articles")
path('articles', views.articles, "articles")

STRUKTURA FOLDERÓW
_init__.py 		# standardowy plik inicjujący moduł,
admin.py 		# plik z funkcjonalnością autoadmina,
apps.py 		# plik z tzw. rejestrem aplikacji,
urls.py 		# plik z konfiguracją URL-i w aplikacji, dobrze budować dla każdej aplikacji a potem dołączać do projektu
wsgi.py 		# plik z konfiguracją WSGI (Web Server Gateway Interface), czyli interfejsu pomiędzy serwerem web a aplikacją, W trybie deweloperskim jest nieużywany.
models.py 		# plik z modelami bazy danych,
tests.py 		# plik z testami automatycznymi,
views.py 		# plik z definicjami widoków.

w models.py 
from django.db import models


TYPY PÓL  
name = models.CharField(max_length=64)
content = models.TextField()
score = models.SmallIntegerField()
price = models.DecimalField(max_digits=5, decimal_places=2)
wants_spam = models.BooleanField() # TRUE lub FALSE nie może być NULL 
					NullBooleanField() # może być NULL
					DateField()	# data
available_from = models.DateTimeField()
visits = models.IntegerField()

OPCJE PÓL 
default # ustawia domyślną wartość pola na 0 
null 	# jeśli = TRUE pole może być NULL, domyślnie jest FALSE czyli NOT NULL
choices	# krotki w krotce przechowujące możliwe wartości i ich opisy
	LIGHTSABERS = (
    (1, "Red"),
    (2, "Blue"),
    (3, "Green"),
    (4, "Purple")
)
saber = models.IntegerField(choices=LIGHTSABERS)

db_index # jeśli TRUE to pole jest indeksem w bazie danych

python manage.py makemigrations <nazwa> # migracja danych piku <nazwa>, gdy modele są gotowe
python manage.py migrate				# zakłada tabele na podstawie klas w models

python manage.py shell 


class Product(models.Model):		# klucz główny dodawany jest automatycznie podczas miggracji bazy na serwer
    name = models.CharField(max_length=64)
    description = models.TextField()
    price = models.FloatField()
    available = models.BooleanField(default=True)
    available_from = models.DateField()

DODAWANIE DANYCH 
from edu.models import Topping, Pizza
t = Topping()
t.name = "anchovies"
t.price = 3.50
t.save()
p = Pizza()
p.size = 2
p.save()
lub
t = Topping.objects.create(name="anchovies", price=3.50)
p = Pizza.objects.create(size=2)

new_band=Band()
>>> new_band.name = 'Rage Against The Machine'
>>> new_band.year = 1991
>>> new_band.save()
>>> new_band.pk 	# sprawdza primary key new_band, jakby  nie istniał, to znaczy, że nie dodało


POBIERANIE DANYCH 
najpierw trzeba zaimportować daną klasę
Model.objects.get(<nazwa_pola>)	# pobiera jeden rekord 
Topping.objects.get(pk=1)		# z tabeli Topping pobiera obiekt, którego klucz główny ma wartość 1
Topping.objects.get(name='anchovies') # jak wyżej tylko obiekt o nazwie 'anchovies', alfabetycznie
Topping.objects.get(name='-anchovies') # odwrotnie alfabetycznie

DoesNotExist	# obiekt o podanych parametrach nie istnieje
MultipleObjectsReturned # istnieje wiele obiektów o podanym parametrze

all()							# zwraca kolekcję, działą jak lista
Model.objects.all() 			# pobiera WSZYSTKIE rekordy z bazy, ostrożnie z dużą ilością danych
Topping.objects.all()			# pobiera wszystkie Topping z bazy

Model.objects.filter() 				# przyjmuje wartości związane z polami
Pizza.objects.filter(size=1)		# pobiera rekordy o argumencie size = 1
Topping.objects.filter(name="onion").filter(price=2) # pobiera rekordy o argumencie size=2 i price=2

Band.objects.filter(year__isnull=True) # pobiera to gdzie year jest null

__lt # mniej niż
Topping.objects.filter(price__lt=5)	# pobiera obiekty z ceną mniejszą od 5

__lte # mniejsze lub równe
Topping.objects.filter(price__lte=5) # pobiera obiekty z ceną mniejszą lub równą 5

__gt __gte	# jak wyżej tylko większe

__contains=value	# zwraca obiekty zawierające w polu podaną wartość
Topping.objects.filter(name__contains="onion") # zwraca wszystko gdzie występuje onion

field__in=[list]	# pobiera obiekty, których podane pole ma wartości z listy
Toppings.objects.filter(name__in=['onion', 'anchovies', 'tomatoes']) # pobiera obiekty o nazwie onion,anchovies i tomatoes

MODYFIKACJA DANYCH 
t = Topping.objects.get(name="onion")	# pobiera obiekt i zapisuje w zmiennej t
t.price = 3.0							# zmienia cenę obiektu t
t.save()								# zapisuje dane

t.update()								# updateuje

USUWANIE DANYCH 
t = Topping.objects.get(name="anchovies")	# pobiera obiekt i zapisuje w t
t.delete()									# usuwa obiekt t

RELACJE
WIELE DO JEDNEGO
related_field = models.ForeignKey(RelatedModel)	# definiowanie wiele do jednego

class Cart(models.Model):
    user = models.ForeignKey(User)	# cart będzie w relacji wiele do jednego z User

JEDEN DO JEDNEGO 
related_field =  models.OneToOneField(RelatedModel) # definiowanie jeden do jednego

class Discount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

on_delete=models.CASCADE 	# zniżka zostanie usunięta razem z User
primary_key=True 			# odnośnik do User będzie kluczem głównym tabeli

WIELE DO WIELU 
related = models.ManyToManyField(RelatedModel) # definiowanie wiele do wielu

from django.db import models
PIZZA_SIZES = (
    (1, "small"),
    (2, "medium"),
    (3, "big"),
)
class Topping(models.Model):
    name = models.CharField(max_length=32)z
    price = models.FloatField()
class Pizza(models.Model):
    size = models.IntegerField(choices=PIZZA_SIZES)
    toppings = models.ManyToManyField(Topping)	# tylko w jednym z dwóch

t1 = Toppings.objects.create(name='anchovies', price=3.50)
t2 = Toppings.objects.create(name='onion', price=2.00)
p = Pizza.objects.create(size=1)  # mała pizza
p.toppings.add(t1)		# żeby coś dodać musi się odwoływać do toppings bo tam zdefiniowaliśmy relację
p.toppings.add(t2)   	# add() dodaje obiekt do relacji

p = Pizza.objects.create(size=1)  # mała pizza
tops = [t1, t2]
p.toppings.set(tops)	# set() pozwala dodać całe zestawy

p.toppings.remove(t1)	# remove() usuwana obiekt z relacji
p.toppings.clear() 		# clear() usuwa wszystkie obiekty z relacji

related = models.ManyToManyField(RelatedModel, through=ThroughModel) # through pozwala wprowadzić dodatkowe informacje w relacji wiele do wielu

class Pizza(models.Model):
    size = models.IntegerField(choices=PIZZA_SIZES)
    toppings = models.ManyToManyField(Topping, through=PizzaTopps) # model w throuigh musi być wcześniej zdefiniowany


TOP_AMOUNT = (
    ('h', 'half'),
    ('n', 'normal'),
    ('d', 'double'),
    ('t', 'triple')
)
class PizzaTops(modelsa.Model):
    pizza = models.ForeignKey(Pizza)
    topping = models.ForeignKey(Topping)
    amount = models.CharField(max_length=1, choices=TOP_AMOUNT, default='n')

pt = PizzaTopps.objects.create(pizza=p, topping=t1, amount='n') # dodaje wartość do relacji wiele do wielu

p = Pizza.objects.get(pk=1) 	# odwoływanie się do danych z relacji wiele do wielu
p.toppings.all()
t = Topping.objects.get(pk=1)
t.pizza_set.all()			# _set wyciąga wszystkie o podanych parametrach

managy.py inspectdb 		# pobiera dane z tabeli i tworzy klasy
managed - FALSE # nie uwzlędnia danych po migracjach, cokolwiek by to nie naczyło

>>> c = Category.objects.get(id=1)
>>> c.article_set.all()				# wyciąga krtykuły dla kategorii
>>> a = Article.objects.get(id=1)
>>> a.category.all()				# wyciąga kategorie dla artykułu

Article.objects.filter(category=(1 & 3)) # wyciąga artykuły o kategorii 1 i 3

p = Person.objects.get(id=1)
p.position.salary	# jak person i position połączony w position
p.position_set.salary	# jak person i position połączony w person


HttpRequest.method		# dane przesyłane w metodach get i post
if request.method == "GET":
	pass
if request.method == "POST":
	pass


data = request.POST["blabla"]	# odczytywanie danych przesyłanych metodą post
data = request.POST.get("blabla")	# jak wyżej, zwraca None w KeyError

redirect("html") # zmienia stronę

raise Http404		# strona nie odnaleziona, można obsłużyć

HttpRequest.COOKIES	# słownik z ciasteczkami
HttpRequest.META 	# słownik z nagłówkami
CONTENT_LENGTH 		# długość całego żądania,
CONTENT_TYPE		# typ MIME przesyłanych danych,
SERVER_NAME 		# nazwa serwera,
SERVER_PORT			# port, na którym pracuje serwer.

HttpRequest 				# odpowiedź http
content_type="text/plain"	# czysty tekst, bez znaczników html - Typ MIME

response = HttpResponse()
repsonese.write("blabla")	# dodaje to co w nawiasie do response, działa jak +=

HttpResponseRedirect("/blabla")	# przekierowuje na podany adres wenętrzny lub zewnętrzny

HttpResponseNotFound("blabla")	# jak strony nie znajdzie to wyrzuca to co w nawiasie, działa jak 404 ale nie da się obsłużyć

request.META["..."] # prztrzymuje informacje
np.
if "MSIE 6.0" in request.META["User-Agent"]:
    redirect("/get-a-newer-browser")  # ;-)


response["Age"] = 120

del(response["Age"])

render(request, ...)	# do formatowania

PRZEKAZYWANIE INFORMACJI
HttpRequest.GET

http://adres?<nazwa zmiennej>=<wartość zmiennej>&<nazwa zmiennej>=<wartość zmiennej>	# przesyłanie danych
<a href="page2?foo=32&bar=Some_text"> # foo i bar to zmienne
? # rozpoczyna informacje o zmiennych
& # oddziela zmienne

def my_view(request):
    if request.method == 'GET':				# odieranie danych
        if request.GET.get("id"):
            # zrób coś z id
        if request.GET.get("muggle"):
            # zrób coś z muggle
    # dalsza część widoku

FORMULARZE - HttpRequest.GET i HttpRequest.POST 
GET 	# używamy głównie do pobierania informacji
POST 	# do wprowadzania zmian w bazie danych, logowania, modyfukacji sesji, dodawanie ciasteczek

<form action="/do-something" method="POST">	# action to adtes na który przesyłane są dane, jak się nie poda to wysyła na tę samą stronę
  <label>
  Imię:
  <input type="text"
         name="userName">
</label>
<label>
  Nazwisko:
  <input type="text"
         name="userSurname">
</label>
<label>
  <input type="submit" value="Wyślij">
</label>
<label>
  <select name="gender">					# jeden name jedna wartość
    <option value="">Select...</option>
    <option value="M">Male</option>
    <option value="F">Female</option>
  </select>
</label>
<label>
  <select multiple name="colors">			# jeden name ma wiele wartości
    <option value="">Select...</option>		# wyciągamy request.POST.getlist(name="colors")
    <option value="red">Czerwony</option>
    <option value="blue">Niebieski</option>
    <option value="green">Zielony</option>
    <option value="yellow">Żółty</option>
  </select>
</label>
<label>
    Wybierz dodatki:				
    <input type="checkbox" name="toppings" value="cheese">Dodatkowy ser 
    <input type="checkbox" name="toppings" value="ham">Dodatkowa szynka
    <input type="checkbox" name="toppings" value="pineaple">Ananas
    <input type="checkbox" name="toppings" value="tomato">Pomidor
    <input type="checkbox" name="toppings" value="salami">Salami
</label>
</form>

from django.views.decorators.csrf import csrf_exempt	# zabezpiecznie przed atakiem CSRF
@csrf_exempt											# dekorator 
def post_form(request):									# ten widok będzie obsługiwał token
    # dalsza część widoku...

{% csrf_token %}

from django.http import HttpResponse 					# odbieranie danych
def get_user_name(request):
    if request.method == "POST":
        name = request.POST.get("name")  # jeśli nie ma, to None
        surname = request.POST.get("surname")  # jeśli nie ma to None
        if name and surname:
            html = "<html><body>Zalogowany {} {}</body></html>".format(name,
                                                                       surname)
        else:
            html = "<html><body>Błąd!</body></html>"
        return HttpResponse(html)
    else:
        # wyświetl pusty formularz

request.POST.getlist(name="")		# wyciąga dane z listy wielokrotnego wyboru lub checkboxa


Movie.objects.all().order_by('title') # sortuje


SESJE I CIASTECZKA 
request.session		# tu przechowywane są dane dotyczące sesji
request.session['has_commented'] = True # zapisywanie sesji w bazie danych

def post_comment(request, new_comment):
    if request.session.get('has_commented', False):  # sprawdza czy istneieje klucz "h_c", jak nie to zwraca False
        return HttpResponse("You've already commented.")
    # tutaj funkcjonalność dotycząca zapisywania komentarza
    request.session['has_commented'] = True 		 # ustawia wartość klucza
    return HttpResponse('Thanks for your comment!')

response = HttpResponse()
response.set_cookie(key, value='', max_age=None, expires=None,	# zapisywanie ciasteczka
                        path='/', domain=None, secure=None, httponly=False) 

response.write("blabla") 		# dodaje napis do responsa

key 		# klucz, pod którym zapisywana jest jakaś wartość.

value 		# wartość tego klucza, domyślnie pusta, samo istnienie klucza często wystarcza

max_age 	# liczba sekund do wygaśnięcia ciasteczka, jeśli ustawimy None, 
			# ciasteczko będzie żyło do czasu zamknięcia przeglądarki; 
			# po ustawieniu tego parametru – parametr expires zostanie wyliczony.
			# jeśli 0, to ciasteczko, żyje do zamknięcia przeglądarki

expires 	# data wygaśnięcia ciasteczka, powinna być albo łańcuchem tekstowym 
			# w formacie "Wdy, DD-Mon-YY HH:MM:SS GMT" albo obiektem datetime.datetime. 
			# Jeśli expires jest obiektem datetime, to max_age będzie wyliczone.

path 		# ścieżka w serwisie, w której ciasteczko będzie widoczne.

domain  	# jeśli ta wartość nie zostanie ustawiona, 
			# ciasteczko będzie widoczne tylko dla domeny, która ją ustawiła.
			# Jeśli domena, która ustawiła ciasteczko, to blog.coderslab.pl, 
			# to w domenie www.coderslab.pl ciasteczko nie będzie widoczne. 
			# Aby to zmienić, trzeba ustawić ten parametr na .coderslab.pl.

secure 		# jeśli jest ustawione, wtedy teoretycznie powinno być przesyłane 
			# tylko przez bezpieczne połączenie https. Niestety, serwery często pozwalają 
			# na przesłanie takiego ciasteczka po nieszyfrowanym łączu.

httponly 	# jeśli jest to ustawione, serwer nie przesyła tego ciasteczka inaczej 
			# niż przez http(s). Uniemożliwia to dostęp do ciasteczka przez JavaScript.

def login(request):
    if "lang" in request.COOKIES:			# odczytywanie ciasteczka
        lang = request.COOKIES.get("lang") 	# pobiera wartość z ciasteczka
        # dalsza część widoku
    else:
        response.set_cookie("lang", "pl")
        # dalsza część widoku...

if "lang" in request.COOKIES:				# usuwanie ciasteczek
    response.delete_cookie("lang")


from django.template.response import TemplateResponse
defcharacter_view(request):				# szablony
ctx	= {
	"name":	"Thorin",
	"race":	"Dwarf",
	"gender":"male",
	"occupation":"king"			
}
return TemplateResponse(request, "char_data.html", ctx)	# wolniejsze, pozwala na czytanie wtyczek

from django.shortcuts import render
def character_view(request):
    ctx = {
        "name": "Thorin",
        "race": "Dwarf",
        "gender": "male",
        "occupation": "king"
    }
    return render(request,
                  "dwarf_data.html",
                  ctx)


{% for val in arr %}
  {# … #}
{% empty %}         # wykona się jak tabela jest pusta
  {# … #}
{% endfor %}

{% for post in posts %}
  {% include 'post/show.html' %}  # pzowala wykorzystywać inny szablon w tym miejscu
{% endfor %}

{% url 'school-class' school_class=nazwa.0 %}   # odwoływanie się do url name

forms.TextInput     # <input type="text" ...>
forms.PasswordInput # <input type="password" ...>
forms.TextArea      # <textarea></textarea>
forms.select        # <select><option>...</option></select>
forms.RadioSelect   # <ul><li><input type="radio" name="..."></li>...</ul>
forms.SelectMultiple # <select multiple="multiple">...</select>

forms.CharField     # Waliduje: max_length i min_length jeśli podane, 
Parametry: min_length, max_length, strip # strip usuwa białe znaki z początku i konća

forms.IntegerField  # waliduje liczbę
Parametry: min_value, max_value.

forms.ChoiceField   # waliduje czy obiet jest na liście
Parametry: choices  # przekazywany zbiór jako parametr

forms.MultipleChoiceField   # Waliduje: czy wybrane opcje są na liście opcji, 
Parametry: choices 

forms.RadioSelect
forms.CheckboxMultipleSelect

required            # domyślnie na True, czy pole jest wymagane
login = forms.CharField(required=False)

label               # opis pola
login = forms.CharField(label="Podaj swój login")

initial             # domyślna wartość, która będzie w polu
login = forms.CharField(initial="administrator")

widget              # zmienia standardowy widget
content = forms.CharField(widget=forms.Textarea)

help_text           # dodatkowy opis formularza
login = forms.CharField(help_text="Dozwolone znaki: a-z, A-Z, 0-9, . (kropka)")

disabled            # uniemożliwia edycję pola
login = forms.CharField(disabled=True)

python mange.py dbshell - odpala w konsoli psql