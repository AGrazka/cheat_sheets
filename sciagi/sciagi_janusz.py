# Formularze

## Tworzenie formularza

```py
class NazwaFormularza(form.Forms):
    pole_pierwsze = forms.CharField(
        label = 'Labelka do pola
        max_lenght=100,
    )
```

## Wyświetlenie formularza

```py
class MojWidok(View):
    def get(self, requesst):
        form = NazwaFormularza()
        return render(request,
            template_name="szablon.html",
            context={'form': form}
        )
```

## Walidacja formularza

```py
class MojWidokView():
    ###Wile linii kodu dalej
    def post(self, request):
        form = NazwaFormularza(request.POST)
        if form.is_valid():
            # Formularz poprawny jesteśmy szczęśliwy

        #Jak formularz jest niepoprawny to wyświetlamy formularz jeszcze raz tym razem formularz będzie wzbogacony o zawartość pól, które wstawiliśmy dodatkowo wyświetlone zostaną przy polach informacje o błędach.
        return render(request,
            template_name="szablon.html",
            context={'form': form}
        )
```

## Dobieranie się do zawartości formularza
```py
form.cleaned_data['nazwa_pola']
# Lub
form.cleaned_data.get('nazwa_pola') # tu nie rzuci wyjątkiem jak będzie brakować danego pola z formularza
```

## Wyświetlenie formularza w szablonie
```twig
{{ form }} <- domyslny wygląd formularza
{{ form.as_p }} <- wyświetlenie kolejnych kontrolek w pragrafach
{{ form.as_table }} <- wyświetlenie formularza w tabeli
{{ form.as_ul }} <- wyświetlenie formularza jako listy


<form action="{% url 'nazwa routa/etykiety' %}" method='POST'>
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="Wyślij">
</form>
```

## Inicjowanie formularza (pól formularza)

```py
form = NazwaFormularza(initial={'pole1': 'Jakaś wartość'})
```

## Dodawanie wigdetu do pola formularza

```py
class NazwaFormularza(forms.form):
    pole1 = forms.ChoiseField(widget=forms.RadioSelect)
```

## Dodatkowy tekst do pola formularza

```py
class NazwaFormularza(forms.form):
    pole1 = forms.ChoiseField(help_text="Dodatkowa informacja")
```

# Obsługa błędów

## Wyświetlanie błedów w szablonie

```twig
{% if form.login.errors %}
  <ol>
  {% for err in form.login.errors %}
    <li>
      <strong>
        {{ err|escape }}
      </strong>
    </li>
  {% endfor %}
  </ol>
{% endif %}
```

## Prosty walidator

```py
def validate_even(value):
  if value % 2 != 0:
    raise ValidationError("{} nie jest parzyste!".format(value))
```

## Dodawanie walidatora do pola formularza

```py
class NazwaFormularza(forms.form):
    pole1 = forms.ChoiseField(validators=[validate_even])
```

## Życie jest prost MODELFORM

```py
class ToppingForm(ModelForm):
    class Meta:
        model = Topping
        #Model
        fields = ['name', 'price'] # wybranie pola name i price
        #lub
        fields = '__all__' # wybranie wszystkich pól z modelu
        #lub
        exclude = ['name'] # wybranie wszystkich pól oprócz name
```

## Inicjowanie danych w MODELFORM

```py
class MojWidok(View):
    def get(self, request, student_id):
        s = Student.objects.get(pk=student_id)
        form = NazwaFormularza(instance=s)
        return render(request,
            template_name="szablon.html",
            context={'form': form}
        )
```

## Zapis formularza do bazy danych

```py
class MojWidokView():
    ###Wile linii kodu dalej
    def post(self, request):
        form = NazwaFormularza(request.POST)
        if form.is_valid():
            form.save()
```

## Aktualizacja rekordu przez formularz
```py
class MojWidokView():
    ###Wile linii kodu dalej
    def post(self, request, student_id):
        s = Student.objects.get(pk=student_id)
        form = NazwaFormularza(request.POST, instance=s)
        if form.is_valid():
            form.save()
```

# Widoki generyczne

Aby działały widoki generyczne Update oraz Delete w naszym routingu musimy im ustawić pk lub sluga

```py
url(r'^notice/delete/(?P<pk>(\d)+)$', DeleteNoticeView.as_view(),
        name='remove-notice'),
```

---

## CreateView

```py
class AuthorCreate(CreateView):
  # model z które ma skorzystać
  model = Author
  # pola z modelu
  fields = ['name']
  # link na jaki ma przekierować po poprawnym wysłaniu formularza
  success_url = reverse_lazy("/author-list")
```

---

## UpdateView

```py
class AuthorUpdate(UpdateView):
  model = Author
  fields = ['name']
  template_name_suffix = '_update_form'
```

---

## DeleteView

```py
class AuthorDelete(DeleteView):
    model = Author
    success_url = '/author-list'
```

## Widoki, które nie zostały ujęte w materiałach a są fajne i przydatne

### ListView

```py
class AuthorListView(ListView):
    model = Author
    paginate_by = 100
```

Taki widok wyświetli listę autorów maksymalnie 100, jeśli jest ich więcej niż 100 to wyświetli się na dole stronicowanie.

### DetailView

```py
class AuthorDetailView(DetailView):
    model = Author
```

Widok ten pozwoli na wyświetlenie pojedynczego autora, trzeba zadbać, aby podobnie do UpdateView i DeleteView w url przekazać jako parametr id authora.