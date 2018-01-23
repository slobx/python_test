Teorijski deo
---

Dati sto konciznije odgvore u formi prosto prosirenih recenica na svako od sledecih pitanja.

01. Sta je to JSON?
	***JSON je princip cuvanja i slanja podataka koji olaksava razmenu podataka izmedju klijentske masine i servera i obrnuto.
	Funkcionise na principu objekata kao i key i value cuvanja podataka unutar objekata***
02. Sta je to XML?
	***XML je markup jezik za cuvanje podataka. Koristi tagove sa cuvanje podataka, atribute za blize odredjivanje elementa kao i same elemente.***
03. Sta je to URL?
	***URL ili veb adresa sluzi kao putanja ka resursu na interenetu koji korisnik zeli da pronadje. Uglavnom se koristi da ukazuje na http stranice***
04. Sta je to HTTP?
	***HTTP je protokol za transfer podataka izmedju klijentske i serverske masine, omogucava prikaz HTML dokumenata***
05. Sta je to RESTful API?
	***RESTful API je web servis i sluzi za handle-ovanje HTTP metoda***
06. Koje HTTP metode imamo?
	***GET, POST, DELETE, PUT, HEAD, OPTIONS, CONNECT, PATCH***
07. Sta je to DNS?
	***DNS - Domain name system - sluzi za prevodjenje IP adresa u domene i obrnuto***
08. Sta je to private IP?
	***private IP su IP adrese lokalnog tipa koje se koriste u lokalnim (kucnim ili poslovnim) mrezama. Pocinju sa 10.0...., 172.16....., 192.168.....)***
09. Sta je to AJAX?
	*** AJAX je tehnologija koja omogucava pristup web serveru direktno sa web stranice. Prednost koriscenja AJAX-a je to sto web servisi mogu asinhrono (u pozadini) da salju/primaju podatke bez menjanja trenutnog prikaza i ponašanja stranice***
10. Sta je to TCP/IP?
	***TCP/IP je komunikacijski protokol koji odredjuje kako se podaci transferuju putem interneta. Koristi klijent/server model komunikacije***
11. Sta je to kes memorija?
	***Kes memorija je deo RAM memorije koja je brze i lakse dostupna procesoru na koriscenje od standardne RAM memorije. Uglavnom je integrisana direktno na cip procesora***
12. Koja je razlika izmedju klase i objekta?
	***Klasa sire odredjuje grupu objekata a objekat je instanca klase kojoj pripada***

Backend
---

1. U `models.py` fajlu implementirati `Comment` model (klasu) u Python-u koja sadrzi atribute:
- `text`: sam komentar, i
- `date`: datum komentara u formatu `YYYY-MM-DD`
"Override"-ovati `__repr__` metod.

2. U `models.py` fajlu definisati `COMMENTS` varijablu koja sadrzi niz od 3 elementa koji su tipa `Comment`. 

3. U `app.py` fajlu napraviti Flask applikaciju koja ima `index` "view" funkciju koja handle-uje `/` route. Funkcija bi trebalo da vraca HTML string koji u `body`-ju sadrzi heading "Welcome!".

4. U `app.py` dodati `comments` "view" funkciju koja handle-uje `/comments` route. Funkcija bi trebalo da vraca HTML koji u `body`-ju sadrzi tabelu komentara. Koristiti Flask template.

5.  U `app.py` dodati `api_comments` "view" funkciju koja handle-uje `/api/v1.0/comments` route. Funkcija bi trebalo da vraca JSON reprezentaciju `COMMENTS` niza.

Frontend
---

U `home.html` fajlu imlementirati jednostavnu klijent aplikaciju kojom moze da testira prethodno implementirani API end point. Koristiti `form` i `iframe`.

Algoritmi
---

Napisati i JavaScript i Python funkciju koja predstavlja resenje sledeceg zadataka:

Write a program that prints the numbers from 1 to 100. But for multiples of three print `Fizz` instead of the number and for the multiples of five print `Buzz`. For numbers which are multiples of both three and five print `FizzBuzz`.

Uputstvo
---

Resenja i odgovore predati u okviru GitHub repozitorijuma.
