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
    pass


def create_van(trains_list):
    pass


def create_seat(trains_list):
    pass


def show_objects(trains_list):
    pass


def train_info(train):
    pass


def van_info(van):
    pass


def main():
    pass


if __name__ == "__main__":
    main()


