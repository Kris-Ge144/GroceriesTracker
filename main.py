stock = {"Milch": 2, "Äpfel": 4, "Bananen": 3, "Avocados": 1, "Gurken": 1, "Tomaten": 2}
buy = {}

def show_stock(stock):
    print("\nVorhandene Produkte:")
    for item, amount in stock.items():
        print(item, "-", amount)

def show_buy(buy):
    if not buy:
        print("\nEinkaufsliste ist leer!")
        return

    print("\nEinkaufsliste:")
    for item, amount in buy.items():
        print(item, "-", amount)


def add_stock(stock):
    item = input("Produkt: ").strip()
    amount = int(input("Menge: "))

    if item in stock:
        stock[item] += amount
        print("\nEs wurden ", amount,"", item," hinzugefügt!")
    else:
        stock[item] = amount
        print("\nEs wurden ", amount,"", item," hinzugefügt!")


def remove_stock(stock, buy):
    used_item = input("Produkt benutzen: ").strip()
    used_amount = int(input("Benutzte Menge: "))

    if used_item not in stock:
        print("Lebensmittel nicht vorhanden!")
        return

    if used_amount > stock[used_item]:
        print("Es sind nur ", stock[used_item], "", used_item, "vorhanden!")
        return

    if used_item in stock and used_amount < stock[used_item]:
        stock[used_item] -= used_amount

    elif used_item in stock and used_amount >= stock[used_item]:
        stock.pop(used_item)

        if used_item in buy:
            buy[used_item] += 1
        else:
            buy[used_item] = 1

def add_buy(buy):
    buy_item = input("Produkt kaufen: ").strip()
    buy_amount = int(input("Menge kaufen: "))

    if buy_item in buy:
        buy[buy_item] += buy_amount
    else:
        buy[buy_item] = buy_amount

def bought(buy, stock):
    bought_item = input("Produkt gekauft: ").strip()
    bought_amount = int(input("Menge gekauft: "))

    if bought_item  in buy:
        if bought_amount >= buy[bought_item]:
            buy.pop(bought_item)
        else:
            buy[bought_item] -= bought_amount

    if bought_item in stock:
        stock[bought_item] += bought_amount
    else:
        stock[bought_item] = bought_amount

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
            show_stock(stock)
        elif choice == "2":
            add_stock(stock)
        elif choice == "3":
            remove_stock(stock, buy)
        elif choice == "4":
            show_buy(buy)
        elif choice == "5":
            add_buy(buy)
        elif choice == "6":
            bought(buy, stock)
        elif choice == "0":
            print("Programm beendet.")
            break
        else:
            print("Ungültige Auswahl. Bitte 0-6 eingeben.")

if __name__ == "__main__":
    main()









