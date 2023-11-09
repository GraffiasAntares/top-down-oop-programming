# top-down-oop-programming
Top-down oop programming example

Classes
      	 	
    builtins.object
    Seat // класс объекта место
    Van // класс объекта вагон
    Train // класс объекта поезд
     
class Seat(builtins.object)
Seat(seat_number)

 	Methods defined here:
    __init__(self, seat_number) // принимает на вход номер места
    Initialize self.  See help(type(self)) for accurate signature.
    Data descriptors defined here:
    __dict__
    dictionary for instance variables (if defined)
    __weakref__
    list of weak references to the object (if defined)
 
class Van(builtins.object)
Van(van_number)

 	Methods defined here:
    __init__(self, van_number) // принимает на вход номер вагона
    Initialize self.  See help(type(self)) for accurate signature.
    add_seat(self, seat_number) // метод добавления места
    Data descriptors defined here:
    __dict__
    dictionary for instance variables (if defined)
    __weakref__
    list of weak references to the object (if defined)

class Train(builtins.object)
Train(train_number)

    Methods defined here:
    __init__(self, train_number) // принимает на вход номер поезда
    Initialize self.  See help(type(self)) for accurate signature.
    add_van(self, van_number) // метод добавления вагона в поезд
    Data descriptors defined here:
    __dict__
    dictionary for instance variables (if defined)
    __weakref__
    list of weak references to the object (if defined)

Functions

    main() 
    create_seat(trains_list) // создает место
    create_van(trains_list) // создать вагон
    create_train(trains_list) // создает поезд
    int_input(inpt) // функция целочисленного ввода с клавиатуры
    seat_search(trains_list, seat_num) // поиск места в массиве поездов,
                                       // возвращает объект найденного места
    van_search(trains_list, van_name) // поиск вагона в массиве поездов,
                                      // возвращает объект найденного вагона
    train_search(trains_list, train_name) // поиск поезда в массиве поездов,
                                          // возвращает объект найденного поезда
    show_objects(trains_list) // вывод инфорации обо всех объектах
    train_info(train) // вывод всей информации хранящейся в объекте поезд
    van_info(van) // вывод всей информации хранящейся в объекте вагон
   