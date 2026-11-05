# Подсчёт суммы очков
def total(*scores):
    return sum(scores)


# Разбор строки с результатами игрока
def parse_line(line):
    name, *parts = line.split()

    if not parts:
        raise ValueError("нет очков")

    scores = []

    for part in parts:
        scores.append(int(part))

    return name, scores


# Построение рейтинга
def make_rating(totals):
    rating = sorted(
        totals.items(),
        key=lambda item: (-item[1], item[0])
    )

    return rating


# Вывод рейтинга
def print_rating(rating):
    for place, (name, score) in enumerate(rating, start=1):
        print(f"{place}. {name} — {score}")


# Главная функция программы
def main():
    players = {}

    print("Вводите результаты: имя и очки через пробел.")
    print("Чтобы закончить, введите «стоп».")

    while True:
        line = input("> ")

        if line.lower().strip() == "стоп":
            break

        try:
            name, scores = parse_line(line)
            players[name] = scores

        except ValueError as error:
            print(f"Строка пропущена: {error}")

    # Подсчёт суммы очков каждого игрока
    totals = {}

    for name, scores in players.items():
        totals[name] = total(*scores)

    # Построение и вывод общего рейтинга
    rating = make_rating(totals)

    print("\n--- Рейтинг ---")
    print_rating(rating)

    # Поиск игроков, набиравших 10 очков
    top_scorers = []

    for name, scores in players.items():
        if 10 in scores:
            top_scorers.append(name)

    top_scorers.sort()

    print("\nНабирали 10 очков:", ", ".join(top_scorers))

    # Проверка наличия игроков
    if not rating:
        print("Нет игроков для отображения топа.")
        return

    # Выбор количества лучших игроков
    while True:
        try:
            count = int(input(
                f"\nСколько лучших показать (1-{len(rating)}): "
            ))

            if count < 1 or count > len(rating):
                raise ValueError(
                    f"нужно число от 1 до {len(rating)}"
                )

            break

        except ValueError as error:
            print(f"Ошибка: {error}")

    # Вывод топа
    print(f"\n--- Топ-{count} ---")
    print_rating(rating[:count])


# Запуск программы
if __name__ == "__main__":
    main()
