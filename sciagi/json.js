json.loads(json_string)	// dekodowanie danych
json.dumps(serializable_object) // kodowanie danych

ZAWSZE PODWÓJNY CUDZYSŁÓW

WCZYTYWANIE:
json_str = """{"books": [{"title": "Hobbit", 
"author": "J.R.R. Tolkien", "year": 1935 },
{"title": "Harry Potter and Goblet of Fire",
"author": "J.K. Rowling", "year": 2000}]}"""

import json
data = json.loads(json_str)
print(data["books"][1])

{'title': 'Harry Potter and Goblet of Fire',
 'year': 2000,
 'author': 'J.K. Rowling'}

ZAPISYWANIE
 data = {
    "movie_title": "Rogue 1.",
    "year": 2016,
    "vader_present": True,
    "characters": ["Jyn", "Cassian", "Chirrut", "Baze", "K-2SO"]
}

import json
data = json.dumps(data)
print(data)

'{"characters": ["Jyn", "Cassian", "Chirrut", "Baze", "K-2SO"],
"movie_title": "Rogue 1.", "year": 2016, "vader_present": true}'

Klient – serwer
Zasada mówiąca, że strona kliencka jest całkowicie odseparowana od strony serwerowej.

Bezstanowość
Architektura REST nie przetrzymuje żadnych informacji między zapytaniami.

Warstwowość
Klient nie powinien być w stanie powiedzieć, czy jest podłączony bezpośrednio do serwera, czy do pośrednika.

Cacheable
Strona kliencka powinna być w stanie przetrzymywać zasoby po swojej stronie.

Jednolity interfejs
Systemy REST powinny utrzymywać jednolity interfejs dla wszystkich swoich zasobów.


pip install djangorestframework // instaluje Django REST Frameworka, trzeba dodać do app

serializer zmienia typy na ten używany w bazie lub w drugą stronę

w pliku serializers.py
class BookSerializer(serializers.Serializer):
    author = serializers.CharField(max_length=200)
    title = serializers.CharField(max_length=200)
    . . .

from .models import Book
from rest_framework import serializers
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "author", "title", "isbn", "publisher", "genre")
        ;



class BookView(APIView):
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404
    def get(self, request, id, format=None):
        book = self.get_object(id)
        serializer = BookSerializer(book, context={"request": request})
        return Response(serializer.data)
    def delete(self, request, id, format=None):
        book = self.get_object(id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



CRUD *
Create
Read
Update
Delete

