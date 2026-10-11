last_name = input("Введите вашу фамилию: ")
first_name = input("Введите ваше имя: ")

print("Добро пожаловать,", first_name + "! Начинаем приём заявок")

total = 0
accepted = 0

while True:
    applicant = input('Фамилия абитуриента (или "завершить", чтобы закончить приём): ')

    if applicant == "завершить":
        break

    score = int(input("Балл абитуриента: "))
    olympiad = input("Есть ли диплом олимпиады? (да/нет): ")

    total += 1

    if score >= 220 or (olympiad == "да" and score >= 180):
        print(applicant + ": заявка одобрена")
        accepted += 1
    else:
        print(applicant + ": заявка отклонена")
print()
print("Рассмотрено абитуриентов:", total)
print("Зачислено:", accepted)
print()
print("До свидания,", first_name + "!")