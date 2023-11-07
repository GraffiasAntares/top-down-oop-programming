class Seat:
    def __init__(self, seat_number):
        self.seat_number = seat_number


class Van:
    def __init__(self, van_number):
        self.van_number = van_number
        self.seats = []

    def add_seat(self, seat_number):
        seat = Seat(seat_number)
        self.seats.append(seat)


class Train:
    def __init__(self, train_number):
        self.train_number = train_number
        self.vans = []

    def add_van(self, van_number):
        van = Van(van_number)
        self.vans.append(van)


def create_train(trains_list):
    print("\nВведите название поезда\n")
    train_name = input("...").replace(" ", "")

    if len(train_name) != 0 and train_search(trains_list, train_name) == object:
        trains_list.append(Train(train_name))

    else:
        return print("\nНекорректный ввод или поезд уже добавлен\n")


def create_van(trains_list):
    if len(trains_list) != 0:
        print("\nВведите поезд и номер вагона через пробел\n")
        try:
            train_name, van_name = input("...").split()
        except Exception:
            return print("\nОшибка ввода\n")

        train_name = train_name.replace(" ", "")
        van_name = van_name.replace(" ", "")
        train = train_search(trains_list, train_name)
        van = van_search(trains_list, van_name)
        if train != object and van == object:
            train.add_van(van_name)
        else:
            print("\nНекорректный ввод или вагон уже добавлен\n")
    else:
        print("\nСначала добавьте поезд\n")


def create_seat(trains_list):
    if len(trains_list) != 0 and len(trains_list[0].vans) != 0:
        print("\nВведите поезд, номер вагона и номер места через пробел\n")
        try:
            train_name, van_name, seat_num = input("...").split()
        except Exception:
            return print("\nОшибка ввода\n")

        train = train_search(trains_list, train_name)
        van = van_search(trains_list, van_name)
        seat = seat_search(trains_list, seat_num)
        if train != object and van != object and seat == object:
            van.add_seat(seat_num)
        else:
            print("\nНекорректный ввод или место уже добавлено\n")
    else:
        print("\nСначала добавьте поезд и вагон\n")


def show_objects(trains_list):
    if len(trains_list) != 0:
        for train in trains_list:
            print(f"Поезд: {train.train_number}")
            for van in train.vans:
                print(f"\tВагон: {van.van_number}")
                print("\t\tМеста: ", end="")
                for seat in van.seats:
                    print(f"{seat.seat_number}", end=" ")
                print("")
            print("")
    else:
        print("\nСначала добавьте поезд\n")


def train_info(train):
    if train != object:
        for van in train.vans:
            print(f"Вагон: {van.van_number}")
            print(f"\tМеста: ", end="")
            for seat in van.seats:
                print(f"{seat.seat_number}", end=" ")
            print("\n")
    else:
        print("\nПоезд не найден\n")


def van_info(van):
    if van != object:
        print("Места: ", end="")
        for seat in van.seats:
            print(f"{seat.seat_number}", end=" ")
        print("\n")
    else:
        print("\nВагон не найден\n")


def train_search(trains_list, train_name):
    for train in trains_list:
        if train.train_number == train_name:
            return train
    return object


def van_search(trains_list, van_name):
    for train in trains_list:
        for van in train.vans:
            if van.van_number == van_name:
                return van
    return object


def seat_search(trains_list, seat_num):
    for train in trains_list:
        for van in train.vans:
            for seat in van.seats:
                if seat.seat_number == seat_num:
                    return seat
    return object


def int_input(inpt):
    if inpt.replace(" ", "").isdigit():
        return int(inpt)
    return 0


def main():
    trains_list = []
    while True:
        print("\n"
              "[1] Создать объект\n"
              "[2] Вывод содержимого объектов\n"
              "[3] Вывод конкретного объекта\n"
              "[4] Завершение программы\n")
        user_input = int_input(input("..."))

        match user_input:
            case 1:
                print("\n"
                      "Выберите объект\n"
                      "[1] Поезд\n"
                      "[2] Вагон\n"
                      "[3] Место\n")
                user_input = int_input(input("..."))

                if user_input == 1:
                    create_train(trains_list)

                elif user_input == 2:
                    create_van(trains_list)

                elif user_input == 3:
                    create_seat(trains_list)

                else:
                    print("\nОшибка ввода\n")
            case 2:
                show_objects(trains_list)
                input("Нажмите Enter, чтобы продолжить...")
            case 3:
                print("\n"
                      "[1] Вывести инфрмацию о поезде\n"
                      "[2] Вывести информацию о вагоне\n")
                user_input = int_input(input("..."))

                if user_input == 1:
                    print("\nВведите название поезда\n")
                    train_name = input("...").replace(" ","")
                    train = train_search(trains_list, train_name)
                    train_info(train)
                    input("Нажмите Enter, чтобы продолжить...")

                elif user_input == 2:
                    print("\nВведите номер вагона\n")
                    van_name = input().replace(" ","")
                    van = van_search(trains_list, van_name)
                    van_info(van)
                    input("Нажмите Enter, чтобы продолжить...")

                else:
                    print("\nОшибка ввода\n")
            case 4:
                exit()
            case _:
                print("\nОшибка ввода\n")


if __name__ == "__main__":
    main()


