fio = input("Введите ваше ФИО: ")
parts = fio.split()

print("Здравствуйте,", parts[1] + "!")
first = input("Введите первый товар: ")
second = input("Введите второй товар: ")
third = input("Введите третий товар: ")

shopping_list = [first, second, third]
print("Ваш список:", shopping_list)
print("Товаров в списке:", len(shopping_list))
shopping_list.append("стакан")
print("Список после добавления подарка:", shopping_list)
shopping_list.sort()
print("Отсортированный список:", shopping_list)
initial_name = parts[1][0]
initial_patronymic = parts[2][0]

print("До свидания,", initial_name + "." + initial_patronymic + ".", parts[0] + "!")