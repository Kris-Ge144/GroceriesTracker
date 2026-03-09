import json

DATA_FILE = "data.json"

def save_data(stock, buy):
    data = {
        "stock": stock,
        "buy": buy,
    }
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def load_data():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data["stock"], data["buy"]
    except FileNotFoundError:
        return {
            "Milch": 2,
            "Apfel": 4,
            "Banane": 3,
            "Avocado": 1,
            "Gurke": 1,
            "Tomate": 2,
        }, {}

stock, buy = load_data()

def show_stock(stock, buy):
    print("\nVorhandene Produkte:")
    for item, amount in stock.items():
        print(item, "-", amount)

def show_buy(stock, buy):
    if not buy:
        print("\nEinkaufsliste ist leer!")
        return

    print("\nEinkaufsliste:")
    for item, amount in buy.items():
        print(item, "-", amount)


def add_stock(stock, buy):

    item = input("Produkt: ").strip()
    if not item:
        print("Produktname darf nicht leer sein.")
        return

    try:
        amount = int(input("Menge: "))
    except ValueError:
        print("Bitte eine Zahl eingeben.")
        return

    if amount <= 0:
        print("Menge muss größer als 0 sein.")
        return

    if item in stock:
        stock[item] += amount
    else:
        stock[item] = amount

    print("Produkt zum Vorrat hinzugefügt:",item,"-",amount)

    save_data(stock, buy)


def remove_stock(stock, buy):

    used_item = input("Produkt benutzen: ").strip()
    if not used_item:
        print("Produktname darf nicht leer sein.")
        return

    try:
        used_amount = int(input("Benutzte Menge: "))
    except ValueError:
        print("Bitte eine Zahl eingeben.")
        return

    if used_amount <= 0:
        print("Menge muss größer als 0 sein.")
        return

    if used_item not in stock:
        print("Lebensmittel nicht vorhanden!")
        return

    if used_amount > stock[used_item]:
        print("Es sind nur ", stock[used_item], "", used_item, "vorhanden!")
        return

    if used_amount < stock[used_item]:
        stock[used_item] -= used_amount
    else:
        stock.pop(used_item)
        buy[used_item] = buy.get(used_item, 0) + 1

    print("Produkt aus Vorrat genommen:", used_item, "-", used_amount)

    save_data(stock, buy)

def add_buy(stock, buy):

    buy_item = input("Produkt kaufen: ").strip()
    if not buy_item:
        print("Produktname darf nicht leer sein.")
        return

    try:
        buy_amount = int(input("Menge kaufen: "))
    except ValueError:
        print("Bitte eine Zahl eingeben.")
        return

    if buy_amount <= 0:
        print("Menge muss größer als 0 sein.")
        return

    if buy_item in buy:
        buy[buy_item] += buy_amount
    else:
        buy[buy_item] = buy_amount

    print("Zur Einkaufsliste hinzugefügt:", buy_item, "-", buy_amount)

    save_data(stock, buy)

def bought(stock, buy):

    bought_item = input("Produkt gekauft: ").strip()
    if not bought_item:
        print("Produktname darf nicht leer sein.")
        return

    try:
        bought_amount = int(input("Menge gekauft: "))
    except ValueError:
        print("Bitte eine Zahl eingeben.")
        return

    if bought_amount <= 0:
        print("Menge muss größer als 0 sein.")
        return

    if bought_item  in buy:
        if bought_amount >= buy[bought_item]:
            buy.pop(bought_item)
        else:
            buy[bought_item] -= bought_amount

    if bought_item in stock:
        stock[bought_item] += bought_amount
    else:
        stock[bought_item] = bought_amount

    print("Zum Vorrat hinzugefügt: ", bought_item, "-", bought_amount)

    save_data(stock, buy)

def main():
    while True:
        print("\n=== GroceryTracker ===")
        print("\n1 - Vorrat anzeigen")
        print("2 - Vorrat hinzufügen")
        print("3 - Vorrat verbrauchen")
        print("4 - Einkaufsliste anzeigen")
        print("5 - Zur Einkaufsliste hinzufügen")
        print("6 - Gekauft (Zum Vorrat hinzufügen)")
        print("0 - Beenden")

        choice = input("\nAuswahl: ").strip()

        if choice == "1":
            show_stock(stock, buy)
        elif choice == "2":
            add_stock(stock, buy)
        elif choice == "3":
            remove_stock(stock, buy)
        elif choice == "4":
            show_buy(stock, buy)
        elif choice == "5":
            add_buy(stock, buy)
        elif choice == "6":
            bought(stock, buy)
        elif choice == "0":
            print("Programm beendet.")
            break
        else:
            print("Ungültige Auswahl. Bitte 0-6 eingeben.")

if __name__ == "__main__":
    main()
