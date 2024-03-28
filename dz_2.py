books = ["Python для начинающих",
         "Война и мир",
         "Алиса в стране чудес",
         "Алгоритмы и структуры данных",
         "Какая то книжка"]
years = [2000, 1998, 2010, 2005, 2020]

while True:
    print("Меню:")
    print("1. Отсортировать по названию книг")
    print("2. Отсортировать по годам выпуска")
    print("3. Вывести список книг с названиями и годами выпуска")
    print("4. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        combined_list = list(zip(books, years))
        sorted_list = sorted(combined_list, key=lambda x: x[0])
        print("Отсортированный список по названию книг:")
        for item in sorted_list:
            print("Название книги:", item[0], "Год выпуска:", item[1])

    elif choice == "2":
        combined_list = list(zip(books, years))
        sorted_list = sorted(combined_list, key=lambda x: x[1])
        print("Отсортированный список по годам выпуска:")
        for item in sorted_list:
            print("Название книги:", item[0], "Год выпуска:", item[1])
    elif choice == "3":
        print("Список книг с названиями и годами выпуска:")
        for i in range(len(books)):
            print("Название книги:", books[i], "Год выпуска:", years[i])
    elif choice == "4":
        print("Выход из программы")
        break
    else:
        print("Неверный ввод. Пожалуйста, выберите пункт из меню.")
