
# Словарь товаров и цен
prices = {
    "хлеб": 50,
    "молоко": 90,
    "сыр": 400,
    "яблоки": 120,
    "кофе": 350
}


# Вывод списка товаров 
def print_menu(prices):
    print("Товары в продаже:")

    for product, price in prices.items():
        print(f"  {product} — {price} руб.")


# Запрос количества товаров
def ask_quantity(product):
    quantity = int(input(f"Сколько «{product}»? "))
    return quantity


# Расчёт стоимости товара
def item_cost(price, quantity):
    return price * quantity


# Вывод чека на печать
def print_receipt(cart):
    print("\n--- Чек ---")

    total = 0

    for number, (product, quantity, cost) in enumerate(cart, start=1):
        print(f"{number}. {product} × {quantity} = {cost} руб.")
        total += cost

    print(f"Сумма: {total} руб.")
    return total


# Расчёт скидки
def apply_discount(total, card=False):
    if card:
        discount = int(total * 0.10)
    elif total >= 1000:
        discount = int(total * 0.05)
    else:
        discount = 0

    final_total = total - discount

    return discount, final_total


# Основная часть программы
cart = []

cashier = input("Введите имя кассира: ").strip().title()

print(f"Здравствуйте, {cashier}! Касса открыта")

print_menu(prices)

while True:
    product = input('\nТовар (или "оплата", чтобы перейти к оплате): ').strip().lower()

    if product == "оплата":
        break

    if product not in prices:
        print(f'Товара «{product}» нет в продаже')
        continue

    quantity = ask_quantity(product)

    cost = item_cost(prices[product], quantity)

    cart.append((product, quantity, cost))

    print(f"Добавлено: {product} × {quantity} = {cost} руб.")


card_answer = input("\nЕсть карта магазина? (да/нет): ").strip().lower()
has_card = card_answer == "да"

total = print_receipt(cart)

discount, final_total = apply_discount(total, card=has_card)

print(f"Скидка: {discount} руб.")
print(f"К оплате: {final_total} руб.")

unique_products = set()

for product, quantity, cost in cart:
    unique_products.add(product)

print(f"Разных товаров в чеке: {len(unique_products)}")

print(f"\nСпасибо за работу, {cashier}!")
