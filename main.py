# main.py
from racunske_operacije import Calculator

def main():
    while True:
        # Pitanje za unos dva broja
        num1 = float(input("Unesite prvi broj: "))
        num2 = float(input("Unesite drugi broj: "))

        # Kreiranje instance kalkulatora
        calc = Calculator(num1, num2)

        # Pitanje za izbor operacije
        print("\nIzaberite operaciju:")
        print("1. Sabiranje")
        print("2. Oduzimanje")
        print("3. Množenje")
        print("4. Deljenje")
        print("5. Izlaz")

        choice = input("Unesite broj operacije: ")

        if choice == '1':
            print(f"Rezultat: {calc.add()}")
        elif choice == '2':
            print(f"Rezultat: {calc.subtract()}")
        elif choice == '3':
            print(f"Rezultat: {calc.multiply()}")
        elif choice == '4':
            print(f"Rezultat: {calc.divide()}")
        elif choice == '5':
            print("Izlaz iz aplikacije. Hvala!")
            break
        else:
            print("Nevažeći izbor, pokušajte ponovo.")

        # Pitanje za nastavak ili izlaz
        continue_choice = input("Želite li da nastavite? (da/ne): ").lower()
        if continue_choice != 'da':
            print("Izlaz iz aplikacije. Hvala!")
            break

if __name__ == "__main__":
    main()
