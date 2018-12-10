f = open(file="", mode="")  # zwraca plik
f.close()  # zamyka plik, później nie ma już do niego dostępu

# mode=
# "r" - tylko odczyt, domyślny tryb
# "w" - tylko pisanie, plik o podanej nazwie zostanie nadpisany
# "a" - pozwala dodawać dane na końcu pliku
# "r+" - pozwala odczytywać i pisać

with open(file="") as f:  # otwiera plik ale po zakończeniu poprawnie go zamyka
    size = 256  # określa jaka objętość danych zostanie wczytana (stosować do b. dużych plików)
    read_data = f.read(size)  # zwraca zawartość pliku jako string,

    f.readlines()  # zwraca listę z wszystkimi linijkami tekstu
    list(f)  # jak wyżej

    for line in f:  # jak wyżej
        print(line, end='')

    f.write("blabla")  # zapisuje string w pliku i zwraca liczbę dodanych znaków
