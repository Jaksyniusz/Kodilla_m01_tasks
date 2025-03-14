# BONUS. Samodzielne ćwiczenia dla orłów

# numer 1
print(f"\n\nZadanie 1\n")

text = """– Czemu tak ciągle gadasz o kobietach, Stan?
– Bo chcę zostać kobietą. Chcę być kobietą. Chce żebyście od dziś mówili na mnie „Loretta”. To moje niezbywalne prawo jako mężczyzny.
– Ale dlaczego chcesz zostać Lorettą, Stan?
– Bo chcę mieć dzieci.
– Dzieci?
– Każdy mężczyzna ma prawo mieć dzieci, jeśli chce.
– Przecież ty nie możesz mieć dzieci!
– Nie prześladuj mnie!
– Nie prześladuję cię, Stan! Nie masz macicy! Gdzie będziesz trzymał swojego embriona? W pudełku?
– Mam pomysł! Przyjmijmy, że Stan nie może póki co mieć dzieci, gdyż nie ma macicy, co nie jest niczyją winą, nawet Rzymian, ale musimy przyznać, że ma prawo do dzieci!
– Świetnie, Judith! Będziemy walczyć z ciemiężycielami…
– Przepraszam.
– A po co?
– Co po co?
– Po co walczyć o jego prawo do posiadania dzieci…
– To symbol naszej beznadziejnej walki z najeźdźcą.
– Symbol jego beznadziejnej walki z rzeczywistością."""

number_of_a = 0
number_of_e = 0
number_of_i = 0
number_of_o = 0
number_of_u = 0
number_of_y = 0

for letter in text.lower():
    if letter == "a":
        number_of_a = number_of_a + 1
    elif letter == "e":
        number_of_e = number_of_e + 1
    elif letter == "i":
        number_of_i = number_of_i + 1
    elif letter == "o":
        number_of_o = number_of_o + 1
    elif letter == "u":
        number_of_u = number_of_u + 1
    elif letter == "y":
        number_of_y = number_of_y + 1
    else:
        pass

print("a = " + str(number_of_a))
print("e = " + str(number_of_e))
print("i = " + str(number_of_i))
print("o = " + str(number_of_o))
print("u = " + str(number_of_u))
print("y = " + str(number_of_y))

# numer 2
print("\n\nZadanie 2\n")

result = ""

for i in range (1,11):
    result = result + str(i) + " "

print(result)


# numer 3
print("\n\nZadanie 3\n")

result = ""
check_number = 30
my_number = 0

while True:
    my_number = my_number + 1
    division_result = my_number % 6
    if check_number > 0:
        if ((division_result == 0) and (check_number == 1)):
            result = result + str(my_number)
            check_number = check_number - 1
        elif division_result == 0:
            result = result + str(my_number) + ", "
            check_number = check_number - 1
        elif division_result != 0:
            pass
    elif check_number <= 0:
        break

print(result)


# alternatywa
result = ""
check_number = 30
my_number = 0

while check_number > 0:
    my_number = my_number + 1
    division_result = my_number % 6
    if ((division_result == 0) and (check_number == 1)):
        result = f"{result}{str(my_number)}"
        check_number = check_number - 1
    elif division_result == 0:
        result = f"{result}{str(my_number)}, "
        check_number = check_number - 1
    elif division_result != 0:
        pass

print(result)