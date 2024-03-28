ids = [123, 456, 789, 321, 654]
phones = [111222333, 444555666, 777888999, 999888777, 666555444]

while True:
    print("Меню:")
    print("1. Отсортировать по идентификационным кодам")
    print("2. Отсортировать по номерам телефона")
    print("3. Вывести список пользователей с кодами и телефонами")
    print("4. Выход")

    choice = int(input("Введите номер действия -> "))

    if choice == 1:
        combined_list = list(zip(ids, phones))
        sorted_list = sorted(combined_list, key=lambda x: x[0])
        print("Отсортированный список по ID -> ")

        for item in sorted_list:
            print(f"ID -> {item[0]}  Номер телефона -> {item[1]}")

    elif choice == 2:
        combined_list = list(zip(ids, phones))
        sorted_list = sorted(combined_list, key=lambda x: x[1])
        print("Отсортированный список по ID -> ")

        for item in sorted_list:
            print(f"ID -> {item[0]}  Номер телефона -> {item[1]}")

    elif choice == 3:
        print("Список пользователей с кодами и телефонами -> ")
        for i in range(len(ids)):
            print(f"ID -> {ids[i]}  Номер телефона -> {phones[i]}")

    elif choice == 4:
        print("Программа завершена")
        break
        
    else:
        print("Неверный код ")