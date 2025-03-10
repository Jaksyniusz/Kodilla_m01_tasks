# Kodilla_m01
1st module tasks

### Zadanie 1.2
Zadanie: tworzymy raport

Czas na Twoje pierwsze samodzielne zadanie do wysyłania Mentorowi!<br>
Napisz je w edytorze Visual Studio Code. A oto zadanie:<br>
Szef organizuje przyjęcie dla klientów i wysłał Cię do sklepu z serami. Wiadomo jak to jest z tego typu instytucjami [*], czasami półki świecą pustkami, ale powiedzmy, że po długich poszukiwaniach udało Ci się znaleźć dobrze wyposażony i kupić wszystko, co potrzeba (oprócz mocno przechodzonego camemberta).<br>
"Nie bojąc się stringów ani ich formatowania, skorzystaj z dotychczasowej wiedzy i stwórz raport. Zaskocz swojego szefa rzeczową listą zakupów wraz z cenami."<br>
W Twoim koszyku znalazł się kilogram każdego z tych serów: roquefort (12,50 zł), stilton (11,24 zł), brie (9,30 zł), gouda (8,55 zł), edam (11 zł), parmezan (16,50 zł), mozzarella (14 zł) oraz hit – czechosłowacki ser z owczego mleka (122,32 zł).<br>
Stwórz odpowiednie zmienne, zarówno dla produktów, jak i cen. Umieść wszystko w jednym tekście i użyj odpowiedniego formatowania. Pamiętaj, że ceny w Polsce zwykło się podawać z dwoma miejscami dziesiętnymi po przecinku (w Pythonie, zgodnie z anglosaską tradycją, używamy kropki zamiast przecinka, więc w kodzie napiszemy 2.49, a nie 2,49).



### Zadanie 1.3
Zadanie: poszerzony raport

Mimo wielkich starań z Twojej strony szef nie był do końca zadowolony z przedstawionego raportu na temat serowych sprawunków. Zabrakło w nim kilku bardzo ważnych elementów, a przede wszystkim sumy wydatków.<br>
Ponadto po wstępnej degustacji, szef nakazał dokupienie większej ilości sera. Obecnie masz 2 kg roqueforta, 3,5 kg parmezanu, 130 dag mozzarelli, 220 dag sera owczego, oraz po kilogramie pozostałych.<br>
Po takiej uczcie, goście z pewnością docenią także deser – listek miętowy (200 g za 20 zł) [*] – link tylko dla ludzi o mocnych nerwach.<br>
Stwórz nowy plik Pythona, wklej do niego kod z poprzedniego zadania, a następnie zmodyfikuj program, by uwzględnić nową ilość produktów. Stwórz odpowiednie obliczenia w tekście, a na koniec przedstaw raport w takiej postaci:<br>

Raport z zakupów:<br>
Produkt, masa w kg, cena<br>
Produkt, masa w kg, cena<br>
...<br>
Suma zł:



### Zadanie 1.4
Zadanie: gwiazdkowe rysunki

Czas na Ciebie. Z wykorzystaniem pętli i drukowania (w technicznym aspekcie) oraz spacji i gwiazdek (jeśli chodzi o tekst) narysuj następujące wzorki:<br>
Nr 1

<pre>
* * * * * * * * * *
 * * * * * * * * * *
* * * * * * * * * *
 * * * * * * * * * *
* * * * * * * * * *
 * * * * * * * * * *
* * * * * * * * * *
 * * * * * * * * * *
* * * * * * * * * *
 * * * * * * * * * *
</pre>

Nr 2

<pre>
**
**
****
****
******
******
********
********
</pre>

Nr 3

<pre>
******
*****
****
***
**
*
</pre>



### Zadanie 1.5
Ćwiczenie

Wracamy do zakupów. Tym razem, szef wysyła Cię ponownie do sklepu i mówi, że masz kupić 1 kg sera, ale stawia pewne warunki: – Kup edam, no, chyba że nie będzie, wtedy brie. Ostatecznie starą dobrą goudę.<br>
Jak przekuć taki algorytm w kod, korzystając z wyrażeń warunkowych? Spróbuj samodzielnie.



### Zadanie 1.6
Ćwiczenie

Czas na akcję z Twojej strony. Mając wiedzę o liczbach, operacjach i pętlach przekonaj się, czy potrafisz wykonać następujące zadanie:<br>
Z zakresu liczb od 1 do 100 wypisz wszystkie, które są podzielne przez 3.<br>
Spróbuj zrobić to na dwa sposoby. Użyj pętli for, jak i pętli while. Pisząc pętlę while, wykorzystaj polecenie break.<br>
Jeśli chodzi o zadanie, podejdź do niego systemowo. Najpierw zastanów się nad tym, jak zadeklarować pętlę. Jakiej kolekcji potrzebujesz? Przed pisaniem właściwego ciała pętli zobacz czy masz poprawnie zadeklarowany początek i koniec, np. wydrukuj wszystkie elementy.<br>



### Zadanie 1.7
BONUS. Samodzielne ćwiczenia dla orłów

Na koniec mamy jeszcze coś specjalnego – jeśli chcesz ugruntować swoją wiedzę, sprawdzić się i trochę poszperać w internecie, zapraszamy do zrobienia tych ćwiczeń!<br>
Mamy też podpowiedzi, ale zajrzyj do nich dopiero, gdy czujesz, że to konieczne. Przecież chcesz się sprawdzić, prawda? ;)<br>
By wykonać ćwiczenia, konieczne jest skopiowanie kodu do swojego pliku na komputerze:<br>

text = """– Czemu tak ciągle gadasz o kobietach, Stan?<br>
– Bo chcę zostać kobietą. Chcę być kobietą. Chce żebyście od dziś mówili na mnie „Loretta”. To moje niezbywalne prawo jako mężczyzny.<br>
– Ale dlaczego chcesz zostać Lorettą, Stan?<br>
– Bo chcę mieć dzieci.<br>
– Dzieci?<br>
– Każdy mężczyzna ma prawo mieć dzieci, jeśli chce.<br>
– Przecież ty nie możesz mieć dzieci!<br>
– Nie prześladuj mnie!<br>
– Nie prześladuję cię, Stan! Nie masz macicy! Gdzie będziesz trzymał swojego embriona? W pudełku?<br>
– Mam pomysł! Przyjmijmy, że Stan nie może póki co mieć dzieci, gdyż nie ma macicy, co nie jest niczyją winą, nawet Rzymian, ale musimy przyznać, że ma prawo do dzieci!<br>
– Świetnie, Judith! Będziemy walczyć z ciemiężycielami…<br>
– Przepraszam.<br>
– A po co?<br>
– Co po co?<br>
– Po co walczyć o jego prawo do posiadania dzieci…<br>
– To symbol naszej beznadziejnej walki z najeźdźcą.<br>
– Symbol jego beznadziejnej walki z rzeczywistością."""<br>

number_of_a = 0<br>
number_of_e = 0<br>
number_of_i = 0<br>
number_of_o = 0<br>
number_of_u = 0<br>
number_of_y = 0<br>

Powodzenia.<br>

Ćwiczenie 1

Znajdź liczbę poszczególnych samogłosek Do zmiennej text przypisano kultowy fragment z filmu "Żywot Briana" autorstwa ekipy Monty Pythona.<br>
Wykorzystując utworzone zmienne:<br>
number_of_a number_of_e number_of_i number_of_o number_of_u number_of_y Policz ile poszczególnych samogłosek możemy znaleźć w cytacie przypisanym do zmiennej text.<br>
Spróbuj rozwiązać to zadanie samodzielnie.


Ćwiczenie 2

Stwórz pętlę, która wydrukuje w konsoli liczby kolejno od 10 do 1 Oczekiwany wynik w konsoli:<br>
10 9 8 7 6 5 4 3 2 1


Ćwiczenie 3

Znajdź pierwszych 30 liczb podzielnych bez reszty przez 6 Wykorzystując pętlę while zwróć w konsoli wyłącznie pierwszych 30 liczb, które możemy bez reszty podzielić przez 6.<br>
Wynik widoczny w konsoli powinien zaczynać się następująco:<br>
6 12 18 ...