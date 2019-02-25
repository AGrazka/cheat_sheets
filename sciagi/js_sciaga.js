/*
   Komentarz, który wykorzystuje
   więcej niż
   jedną linię
*/

// Komentarz w jednej linii
 
var nazwaZmiennej = 6;			// definiowanie zmiennej, nie trzeba określać ich typu
nazwaZmiennej = 6 				// zmienna będzie globalna

2 + 2 + "2" = "42"				// cudawianki w js

console.log(instrukcja);			// logowanie do konsoli

var nazwa = {					// obiekt
	klucz1: "wartość 1"
	klucz2: "wartość 2"
}

var nazwa = [el1, el2, el3]		// tablica

typeof <jakiś element>;			// zwraca typ elementu

parseInt(string, system liczbowy(2-36)) 	//konwersja stringów do liczb

vat foo = null					// pusta wartość

var foor;						// nundefined
s
if (warunek, warunek stopu, kolejny krok) {					// pętla if 
	instrukcja
} else if (warunek) {
	instrukcja
} else {
	instrukcja
}

var expression = 3;
switch (expression) {			// wyszukuje wyrażenie z nawiasu i dopasowuje instrukcje 
    case 1: 					// jeśli wartość expression jest 1
        console.log("Today is Mon."); // instrukcja do wykonania
	break;
    case 2:
        console.log("Today is Tue.");
	break;
    case 3:
        console.log("Today is Wed.");
	break;
    default:
        console.log("Wrong day number");
}

i++ 							// powiększanie liczby o 1
i--								// pomniejszanie liczby o 1

++i 							// najpierw dodaje 1 do zmiennej, a później wykonuje instrukcje
-- i 							// najpierw odejmuje 1 od zmiennej, a później wykonuje instrukcje

while (warunek) {				// pętla whi
	instrukcja	
}

Math.random()					// losowa liczba 0 do 9
Math.floor(liczba)				// zaokrągla w dół
Math.pow()						// potęguje

do {							// najpierw wykona instrukcje po "do", a poźniej while
	instrukcja
}
while (warunek) {
instrukcja
}

break 							// przerywa pętle


liczba1 == "liczba2"			// sprawdza tylko wartość
liczba1 === "liczba2"			//  sprawdza wartość i typ
liczba1 !== "liczba2"			// sprawdza wartość i typ

&& 								// logiczne AND
||								// logiczne OR
!								// logiczne NOT
^								// XOR - tylko jeden warunek może być prawdziwy

function nazwa(parametry) {		// funkcja jak def w pythonie
	instrukcja
}
nazwa() 						// wywołanie funkcji, można wywołać przed zdefiniownaiem funkcji

var foo = function (){}			// przypisanie funkcji do zmiennej, można wywołać poprzez zmienną

var teacher = {
    name: "Janusz",
    surname: "Kowalski",
    subject: "Programowanie JS",
    teach: function(){
        return "Uczę programowania";
    },
    aboutMe: function(){
        console.log(this.name);	// this odnosi się do obiektu samego w sobie
        console.log(this.surname);
        console.log(this.subject);
    },
};

nazwa_obiektu.nazwa_atrybutu; 	// wywoływanie atrybutów obiektu
console.log(teacher.name);

nazwa_obiektu.nazwa_metody();	// wywoływanie metod obiektu
console.log(teacher.teach());

var teacher = {
    name: "Janusz",
    surname: "Kowalski",
    subject: "Programowanie JS"
};	
teacher.students = ["Ala","Jan","Ada"]; // dodaje atrubyt
console.log(teacher.students); 

var Car = function(type, hp, color) {	// konstruktor obiektu
    this.type = type;
    this.hp = hp;
    this.color = color;
};
var bmw = new Car("bmw", 125, "blue");	// tworzenie obiektu o podanych atrybutach
console.log(bmw.type);
console.log(bmw.hp);
console.log(bmw.color);

var Car = function(carType, carHp, carColor) {
    this.hp = carHp;
    this.type = carType;
    this.color = carColor;
    this.km = 0;
};
Car.prototype.drive = function(km){		// prototyp, funkcja, której bedzie mógł użyc każdy obiekt car
    console.log(this.color + " " + this.type + " drives for " + km  + "km");
    this.km += km;
}

var mercedes = new Car("Mercedes", 120, "Black");
var trabant = new Car("Trabant", 40, "Grey");
trabant.drive(10);type
mercedes.drive(40);

var nums = [5, 2, 20, 19, 4];			// sortowanie w js WTF
nums.sort(function(a, b){
    return a - b;
});

var timeout = setTimeout(function () { 	// punkcja opóźniająca
  console.log('I will be invoked in 5s');
}, 5000);
clearTimeout(timeout);					// czysczenie zmiennych


var interval = setInterval(function () {	// funkcja która co 5s coś zwraca, działa w nieskończonośc
  console.log('I will be invoked every 5s');
}, 5000);
clearInterval(interval);				// czyści i zeruje interval


DOM
WYSZUKIWNIE								
document.querySelector("selector");		// wyszukuje selektor, jak jest wiele to zwraca pierwszy

document.getElementById("id");			// wuszykuje po id elementu, lepeij po id

document.querySelectorAll("selector");	// zwraca wiele elementów w tablicyS

document.getElementsByTagName("tag"); 	// wyszukuje wiele po nazwie tagu w tablicy

document.getElementsByClassName("className"); // wyszukuje wiele po nazwie klasy w tablicy

var foo = document.getElementById("glink"); 
var fooHeader = foo.querySelector("h1");	// wyszukuje w elemencie foo, 



document.addEventListener("DOMContentLoaded", function(){ // czeka aż się wszystko zaalduje
};	 



// <a href="http://wp.pl" class="foo bar" id="glink" data-foo="1"<h1>WP.PL</h1></a>

link.classList;							// ["foo", "bar"]
link.className;							// "foo bar"
link.id;								// "glink"
link.innerHTML;							// "<h1>WP.PL</h1>"
link.id = 'newId';						// nadpisujemy id nową wartością
link.className = 'newClass1 newClass2'; // nadpisujemy listę klas nowa wartością
link.outerHTML;							// "<a href="http://wp.pl" class="foo bar" id="glink" data-foo="1"> <h1>WP.PL</h1> </a>"
link.innerText; 						// "WP.PL"
link.tagName;							// "A" – nazwa zwracana jest dużymi literami
link.dataset;							// { foo: "1" }



element.style.backgroundColor;			// wyciąŋą kolor tła elementu, można też zmienniać z =
element.style.fontSize;					// wyciąga wielkość fontu
element.style.padding;					// 

console.log(element.classList);			// wyciąga lisßę klas elementu
console.log(element.className);			// wyciąga wartość class=""
element.classList.add("<nazwa klasy>");		// dodaje klasę do listy
element.classList.remove("<nazwa klasy>");		// usuwa daną klasę z listy
element.classList.toggle("<nazwa klasy>");	// jak klasa istnieje to ją usuwa, jak nie istnieje to ją dodaje
element.dataset.<nazwa> = "<wartośc>";	// ustawianie atrybutu data-

np:
console.log(element.dataset);			// wyświetla wszystkie data elementu
console.log(element.dataset.id);  
console.log(element.dataset.user);  
console.log(element.dataset.dateOfBirth);

el.hasAttribute(<nazwa>);				// sprawdz czy ma podaną wartość
el.getAttribute(<nazwa>);				// pobiera wartość 
el.removeAttribute(<nazwa>);			// usuwa atrybut o podanej zmiennej
el.setAttribute(<nazwa>, <wartość>);	// nastawia wartość danego atrubytu

el.innerText = <wartość>;				// ustawia wartość ekstu wenwątrz elementu

addEventListener(eventName, callback)	// dodawanie eventów

// Kod HTML
// <button id="counter">Click me!</button>
Kod Javascript
var button = document.querySelector("button");
var clickCount = 0;
button.addEventListener("click", function (event) {	// przekazanie funkcji anonimowej
    clickCount += 1;
    console.log("Click number", clickCount);
});

// Kod HTML
// <button id="counter">Click me!</button>
Kod Javascript
var clickCount = 0;
function clickCounter(event) {
    clickCount += 1;
    console.log('Click number', clickCount);		// przekazanie zdefiniowanej funkcji
}
var button = document.querySelector("button");
button.addEventListener('click', clickCounter);


function randomWord (event) {						
    var myWord = randomWords[Math.floor(Math.random() * randomWords.length)];
    console.log(myWord);
}
button.addEventListener('click', clickCounter);		// dodawanie eventów do elementu
button.addEventListener('click', randomWord);	


removeEventListener(event, callback).				// usuwanie eventu


LISTA EVENTÓW
mouse: mousedown, mouseup, click, dblclick, mousemove, mouseover, mouseout, mousecenter

key: keydown, keypress, keyup

touch: touchstart, touchmove, touchend, touchcancel

control: resize, scroll, focus, blur, change, submit

no arguments: load, unload, DOMContentLoaded

document.addEventListener("DOMContentLoaded", function() {}); // oczekiwanie na wczytanie całej strony

event.button 						// zwraca przycisk myszki, który został naciśnięty,
event.clientX 						// zwraca koordynat X (horyzontalny) myszki, relatywnie do górnego, lewego rogu strony,
event.clientY 						// zwraca koordynat Y (wertykalny) myszki relatywnie do górnego, lewego rogu strony,
event.screenX 						// zwraca koordynat X (horyzontalny) myszki, relatywnie do górnego, lewego rogu okna,
event.screenY						// zwraca koordynat Y (wertykalny) myszki, relatywnie do górnego, lewego rogu okna.

event.altKey 						// zwraca true, jeżeli alt był naciśnięty,
event.ctrlKey 						// zwraca true, jeżeli ctrl był naciśnięty
event.shiftKey 						// zwraca true, jeżeli shift był naciśnięty.
event.key 							// zwraca wartość klawisza, który wywołał event, np: d, Escape, c, ArrowUp, ArrowLeft
event.code 							// zwraca kod klawisza, który wywołał event, np: KeyD, Escape, KeyC, ArrowUp, ArrowLeft

event.currentTarget 				// zwraca element, na którym wywołany został event,
event.target 						// zwraca element, który spowodował wywołanie eventu,
event.timeStamp						// zwraca czas, w którym został wywołany event,
event.type 							// zwraca typ eventu (jako string).
event.preventDefault() 				// anuluj oryginalną akcję,
event.stopPropagation() 			// anuluj wszystkie eventy tego samego typu z elementów nadrzędnych,
event.stopImmediatePropagation() 	// anuluj wszystkie eventy tego samego typu przypięte do tego elementu oraz wszystkich elementów nadrzędnych.

document.addEventListener("DOMContentLoaded", function() {  	// zlicza kliknięcie
    var parent = document.getElementById("bubblingButtons");
    parent.addEventListener('click', function (e) {

        var child = e.target;
        child.dataset.counter = parseInt(child.dataset.counter) + 1;
    });
});


el.parentElement 						// zwraca rodzica elementu

el.previousElementSibling; 				// zwraca poprzednie eodzeństwo
el.nextElementSibling; 					// zwraca następne rodzeństwo

el.children; 							// zwraca wszystkie dzieci
el.firstElementChild; 					// zwraca pierwsze dziecko
el.lastElementChild; 					// zwraca ostatnie dziecko	

el.createElement("div"); 				// tworzenie nowego elementu i zapisanie do zmiennych
el.cloneNode(deep);						// klonowanie deep true(klonuje z całym poddrzewem) lub false
el.appendChild(nowyElement)				// dodaj element jako ostatnie dziecko danego węzła,
el.insertBefore(nowyElement, dziecko) 	// dodaj element przed jednym z podanych dzieci,
el.replaceChild(nowyElement, dziecko) 	// zamień podane dziecko.
el.removeChild(element)					// usuwanie 

FORMULARZE
form.action 			// adres URL, do którego prowadzi formularz,
form.method 			// metoda, którą wysyłany jest formularz,
form.elements 			// kolekcja elementów należących do tego formularza (w kolejności wpisanej w kodzie HTML).

EVENTY FORMULARZY
submit 					// jest wywoływany przed wysłaniem Wysyłanie możemy zablokować przez preventDefault() albo zwrócenie false z tego eventu,
reset 					// wywoływane po zresetowaniu formularza (rzadko używane).

input.value				// zwraca wartość inputu, Może służyć też do nastawienia wartości.
input.type 				// typ inputu. Można go też łatwo zmienić na inny.
input.disabled 			// zwraca wartość boolowską, która oznacza, czy element jest włączony czy nie. Możemy ją zmieniać.
input.checked (tylko checkboksy) // zwraca wartość boolowską, która oznacza, czy element jest zaznaczony czy nie.
option.selected (tylko elementy option) // zwraca wartość boolowską, która oznacza, czy dany element jest wybrany czy nie.

blur 					// wywoływany, gdy użytkownik opuści pole,
focus					// wywoływany, gdy użytkownik zaznaczy pole,
change 					// wywoływany, gdy zmieni się wartość pola,
keydown, keyup, keypress // eventy związane z pisaniem na klawiaturze.



jQuery
$(function() {
    /* tu nasz kod */
});
/* lub */
$(document).ready(function() {
     /* tu nasz kod */
});

$('#top');			// wyszukiwanie
$('li');      
$('ul li');   
$('.boxes'); 
$('.menu').find('a');
$('a', $('.menu'));
$('#menu a');

var linksOnTop = $('.someList li');	// to będą obiekty jQuery nie JS
var thirdLi = linksOnTop[2];		// to będzie js
var thirdLi = linksOnTop.eq(2);		// to będzie jQuery

Wykonuj dla wszystkic nie trzeba iterować
$('.menu').find('a').css('color', 'red'); 			// dodaje/nadpisuje własność css o podanej wartości
$('.menu').find('a').addClass('crazyColors');		// dodaje klase
$('.menu').find('a').removeClass('crazyColors');	// usuwa klase z el/ów 
$('.menu').find('a').toggleClass('crazyColors');	// przełącza klasę
$('.menu').hasClass('crazyColors'));				// sprawdza czy ma klasę
$('.menu').find('a').fadeIn('slow');				// pojawianie
$('.menu').find('a').fadeOut(1000);					// znikanie

fadeIn() 	// pojawienie się ukrytego elementu z efektem przenikania
fadeOut() 	// zniknięcie widocznego elementu z efektem przenikania

find() 		// znajduje elementy, które są zagnieżdżone w innym
closest() 	// znajduje elementy najbliższe idąc w górę drzewa DOM
children() 	// znajduje wszystkie dzieci danego elementu
parent() 	// znajduje rodzica elementu
siblings() 	// znajduje rodzeństwo elementu
next() 		// znajduje następny element
prev() 		// znajduje poprzedni element

el.attr('type');				// zwracanie atrybutu
el.attr('type', 'password');	// ustawianie atrybutu

el.each(function (index, element) // coś użytecznego, ale nie mam pojęcia dlaczego
{}

on(event, function) 			// pozwala na dodanie callbacka do eventu,
one(event, function) 			// pozwala na zapięcie nowego eventu, który zadziała tylko raz, po czym zostanie automatycznie usunięty,
off(event, function) 			// usuwa wszystkie callbacki, które były podpięte pod dany event (nawet te anonimowe).
{}
stopPropagation() 				// zatrzymuje propagacje eventu w górę drzewa DOM (callbacki rodziców nie zostaną uruchomione).
stopImmediatePropagation() 		// zatrzymuje propagacje eventu oraz każdy inny event, który powinien zostać uruchomiony.

event.preventDefault()			// zapobiega domyślnej akcji eventu


$(elements).on(events [, selector] [, data], handler)	// zaczepienie eventu do elementu
events  		//typ eventu, może być jeden lub więcej,
selector 		// to opcjonalny parametr, określa selektory, na których możemy zaczepić event, a których np. nie ma jeszcze w dokumencie,
data 			// to również opcjonalny parametr. Możemy przekazać do funkcji handler jakieś dane np. {foo: "bar"},
handler			// to funkcja, która zostanie wykonana w momencie wywołania eventu.

Mouse Events
click 			// kliknięcie
dblclick 		// podwójne kliknięcie
mouseenter 		// najechanie
mouseleave 		// zjechanie

KeyBoard Events
keypress 		// wciśnięty klawisz
keydown 		// wciśnięty klawisz (działa na klawisze specjalne)
keyup 			// zwolniony klawisz

Form Events
submit			// kliknięty submit
change 			// zmiana elementu
focus 			// focus na elemencie
blur 			// utrata eventu focus

Document/Window Events
load 			// ładowanie dokumentu
resize 			// zmiana wielkości okna
unload 			// event po opuszczeniu przez użytkownika strony (blokowany przez niektóre przeglądarki, możesz użyć onbeforeunload)
scroll 			// scrollowanie

attr(name, newValue) 	// pobierz lub ustaw atrybut elementu,
removeAttr(name) 		// usuń atrybut elementu,
prop(name) 				// sprawdza własności (properties) elementu.
data(dataSet, value)	// nastawianie i odczytywanie data
html() 					// wstawia/ustawia tekst lub HTML (zrenderowany)
text() 					// wstawia/ustawia tekst lub HTML (jako string, np. Tekst )

$("tag")				// tworzenie elementu html
before()				// wstawianie przed
after()					// wstawianie po
append(newElement) 		// wstaw nowy element na koniec dzieci już istniejącego elementu,
appendTo(oldElement) 	// odwrotność (czyli wywołujemy na nowym elemencie i podajemy, gdzie ma się dodać).
prepend(newElement) 	// wstaw nowy element na początek dzieci już istniejącego elementu,
prependTo(oldElement) 	// odwrotność.
remove() 				// usuń element,
detach() 				// wypnij element z drzewa DOM bez usuwania go i zwróć go (np. żebyśmy mogli zapisać go do zmiennej),
empty() 				// usuń wszystko ze środka elementu