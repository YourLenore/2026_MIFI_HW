organizer = input("Введите ваше имя: ")

print("Здравствуйте,", organizer + "! Открываем зрительское голосование")

films = ["дюна", "аватар", "матрица", "интерстеллар", "шрек"]

print("Фильмы в программе фестиваля:", ", ".join(films))

voted_people = set()
all_liked_films = []

votes = {
    "дюна": 0,
    "аватар": 0,
    "матрица": 0,
    "интерстеллар": 0,
    "шрек": 0
}

while True:
    name = input('\nИмя зрителя (или "стоп", чтобы закончить): ')

    if name.strip().lower() == "стоп":
        break

    name = name.strip()
    normalized_name = name.lower()

    if normalized_name in voted_people:
        print(name + ", вы уже голосовали, второй голос не засчитан")
        continue

    voted_people.add(normalized_name)

    liked_input = input("Какие фильмы вам понравились (через запятую): ")

    liked_films = set()

    for film in liked_input.split(","):
        film = film.strip().lower()

        if film not in films:
            print(f"Фильма «{film}» нет в программе, голос не засчитан")
            continue

        liked_films.add(film)

    for film in liked_films:
        votes[film] += 1

    all_liked_films.append(liked_films.copy())

    print(f"Спасибо, {name}! Засчитано голосов: {len(liked_films)}")

print("\nИтоги голосования")
print("Проголосовало зрителей:", len(voted_people))

for film in films:
    print(film, "-", votes[film])

max_votes = max(votes.values())

winners = []

for film in films:
    if votes[film] == max_votes:
        winners.append(film)

for film in winners:
    print(f"Победитель: {film} ({max_votes})")

if all_liked_films:
    common_films = all_liked_films[0].copy()

    for liked_films in all_liked_films[1:]:
        common_films = common_films & liked_films

    if common_films:
        print("Понравились всем:", ", ".join(sorted(common_films)))
    else:
        print("Понравились всем: таких фильмов нет")
else:
    print("Понравились всем: нет проголосовавших зрителей")

unpopular_films = set()

for film in films:
    if votes[film] == 0:
        unpopular_films.add(film)

if unpopular_films:
    print("Не выбрал никто:", ", ".join(sorted(unpopular_films)))
else:
    print("Не выбрал никто: таких фильмов нет")

print()
print("До свидания,", organizer + "!")