print("Wprowadź dwie liczby celem ich dodania")
while True:
    try:
        num1 = int(input("Pierwsza liczba: "))
        num2 = int(input("Druga liczba: "))
        print("Wynik dodawania podanych liczb to: ", num1 + num2)
        break
    except ValueError:
        print("Wprowadź dane liczbowe!")
