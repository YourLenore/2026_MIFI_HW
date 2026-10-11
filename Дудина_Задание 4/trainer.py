last_name = input("Введите вашу фамилию: ")
first_name = input("Введите ваше имя: ")

print("Добро пожаловать,", first_name + "! Начинаем принимать зачёт")

athletes_count = int(input("Сколько спортсменов сдают зачёт: "))
attempts_count = int(input("Сколько подходов делает каждый: "))

athletes = []
results = []
completed_count = 0

for athlete_number in range(athletes_count):
    print(f"\n--- Спортсмен {athlete_number + 1} ---")

    surname = input("Фамилия спортсмена: ")
    athletes.append(surname)

    total_pullups = 0

    for attempt_number in range(attempts_count):
        pullups = int(input(f"Подход {attempt_number + 1}: "))
        total_pullups += pullups

    results.append(total_pullups)

    if total_pullups >= 30:
        print(f"{surname}: всего {total_pullups} — норматив выполнен")
        completed_count += 1
    else:
        print(f"{surname}: всего {total_pullups} — норматив не выполнен")

print("\nИтоговая таблица:")

for i in range(len(athletes)):
    print(f"{i + 1}. {athletes[i]} — {results[i]}")

print()
print(f"Норматив выполнили: {completed_count} из {athletes_count}")
print(f"Всего подтягиваний группы: {sum(results)}")

print()
print("До свидания,", first_name + "!")