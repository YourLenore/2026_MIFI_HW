from pathlib import Path
# Загрузка каталога из файла
def load_catalog(filename):
    catalog = {}

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                try:
                    book_id, title, price, quantity = line.split(";")

                    book_id = int(book_id)
                    price = int(price)
                    quantity = int(quantity)

                    if book_id < 1 or price <= 0 or quantity < 0:
                        print(f"Некорректные данные: {line}")
                        continue

                    if book_id in catalog:
                        print(f"Повторяющийся ID: {book_id}")
                        continue

                    catalog[book_id] = (title, price, quantity)

                except ValueError:
                    print(f"Ошибка в строке: {line}")
                    continue

    except FileNotFoundError:
        print(f"Файл {filename} не найден.")

    return catalog


# Сохранение каталога в файл
def save_catalog(filename, catalog):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for book_id, (title, price, quantity) in sorted(catalog.items()):
                file.write(f"{book_id};{title};{price};{quantity}\n")

        print(f"Каталог сохранён в файл {filename}.")

    except OSError:
        print(f"Не удалось сохранить файл {filename}.")


# Вывод каталога
def print_catalog(catalog):
    if not catalog:
        print("Каталог пуст.")
        return

    print("\nКаталог:")

    for book_id in sorted(catalog):
        title, price, quantity = catalog[book_id]

        if quantity == 0:
            print(f"{book_id}. {title} — {price} руб., нет в наличии")
        else:
            print(f"{book_id}. {title} — {price} руб., остаток: {quantity}")


# Добавление книги
def add_book(catalog):
    try:
        book_id = int(input("ID новой книги: "))

        if book_id < 1:
            print("ID должен быть положительным числом.")
            return False

        if book_id in catalog:
            print("Книга с таким ID уже существует.")
            return False

        title = input("Название: ").strip()

        if not title:
            print("Название не может быть пустым.")
            return False

        price = int(input("Цена: "))

        if price <= 0:
            print("Цена должна быть больше нуля.")
            return False

        quantity = int(input("Количество: "))

        if quantity < 0:
            print("Количество не может быть отрицательным.")
            return False

        catalog[book_id] = (title, price, quantity)

        print(f"Книга «{title}» добавлена.")
        return True

    except ValueError:
        print("ID, цена и количество должны быть целыми числами.")
        return False


# Удаление книги
def delete_book(catalog):
    try:
        book_id = int(input("ID книги для удаления: "))

        if book_id < 1:
            print("ID должен быть положительным числом.")
            return False

        if book_id not in catalog:
            print("Книга с таким ID не найдена.")
            return False

        title = catalog[book_id][0]

        del catalog[book_id]

        print(f"Книга «{title}» удалена.")
        return True

    except ValueError:
        print("ID должен быть целым числом.")
        return False


# Изменение цены
def change_price(catalog):
    try:
        book_id = int(input("ID книги: "))

        if book_id < 1:
            print("ID должен быть положительным числом.")
            return False

        if book_id not in catalog:
            print("Книга с таким ID не найдена.")
            return False

        new_price = int(input("Новая цена: "))

        if new_price <= 0:
            print("Цена должна быть больше нуля.")
            return False

        title, old_price, quantity = catalog[book_id]

        catalog[book_id] = (title, new_price, quantity)

        print(f"Цена книги «{title}» изменена на {new_price} руб.")
        return True

    except ValueError:
        print("ID и цена должны быть целыми числами.")
        return False


# Изменение количества
def change_quantity(catalog):
    try:
        book_id = int(input("ID книги: "))

        if book_id < 1:
            print("ID должен быть положительным числом.")
            return False

        if book_id not in catalog:
            print("Книга с таким ID не найдена.")
            return False

        new_quantity = int(input("Новое количество: "))

        if new_quantity < 0:
            print("Количество не может быть отрицательным.")
            return False

        title, price, old_quantity = catalog[book_id]

        catalog[book_id] = (title, price, new_quantity)

        print(f"Количество книги «{title}» изменено на {new_quantity}.")
        return True

    except ValueError:
        print("ID и количество должны быть целыми числами.")
        return False


# Главная функция программы
def main():
    filename = Path(__file__).resolve().parent / "catalog.txt"

    catalog = load_catalog(filename)

    print(f"Файл {filename} загружен. Книг в каталоге: {len(catalog)}")

    while True:
        print("\nМеню:")
        print("1 — показать каталог")
        print("2 — добавить книгу")
        print("3 — удалить книгу")
        print("4 — изменить цену")
        print("5 — изменить количество")
        print("0 — сохранить и выйти")

        try:
            choice = int(input("Выберите пункт: "))

        except ValueError:
            print("Введите число от 0 до 5.")
            continue

        if choice == 1:
            print_catalog(catalog)

        elif choice == 2:
            add_book(catalog)

        elif choice == 3:
            delete_book(catalog)

        elif choice == 4:
            change_price(catalog)

        elif choice == 5:
            change_quantity(catalog)

        elif choice == 0:
            save_catalog(filename, catalog)
            print("До свидания!")
            break

        else:
            print("Такого пункта меню нет.")


# Запуск программы
if __name__ == "__main__":
    main()
