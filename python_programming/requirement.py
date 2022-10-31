class Star_Cinplex:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)
        # print("Hall information entry successfully\n")


class Hall(Star_Cinplex):
    def __init__(self, rows, cols, hall_no, ):
        self.seats = {}
        self.show_list = [] # ('abc', 'def', 'ghi')
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.entry_hall(self)
        self.seat = ["Empty" for i in range(20)]


    def entry_show(self, idd, movie_name, time):
        # new_obj = (idd, movie_name, time)
        self.show_list.append((idd, movie_name, time))
        # self.arr = ([[f"empty" for i in range(self.rows)] for j in range(self.cols)])
        # self.seats[idd] = self.arr
        self.seats[idd] = ([[f"empty" for i in range(self.rows)] for j in range(self.cols)])

    def show_seats(self):
        show_id = 'ae123'
        print("Ok")
        print(type(show_id))
        print("ID matched")

        for i in range(1, len(self.seats['ae50'])):
            for j in range(1, len(self.seats['ae50'][i])):
                print(f"({i},{j}).", self.seats['ae50'][i][j], end=" ")
            print()
        print()

    def book_seats(self):
        show_id = input("Enter Bus No : ")
        if show_id in self.seats:
            passenger = input("Enter YOur name : ")
            seat_no = int(input("Enter seat No : "))
            if seat_no > 20:
                print("Seats only 20")
            elif self.seat[seat_no] != "Empty":
                print("Seat Already Booked")
            else:
                self.seat[seat_no - 1] = passenger
        else:
            print("No bus available")

    def reservation(self, idd, seat_no):
            # idds = input("Enter show id: ")
            if idd in self.seats:
                # print(self.seats[idd])
                seat_no = int(input("Enter seat no: "))
                if seat_no > self.seats[idd]:
                    print("No seats available")
                # for i in range(1, self.rows + 1):
                #     for j in range(1, self.cols + 1):
                #         print(f"empty", end=" ")
                #     print()

                # for i in range(1, len(self.seats[idd])):
                #     for j in range(1, len(self.seats[idd][i])):
                #         print(f"({i},{j}).", self.seats[idd][i][j], end=" ")
                #     print()
                # print()

    def show(self):
        show_id = input("Enter bus number : ")
        for idd, movie_name, time in self.show_list:
            if idd == show_id:
                print('*' * 50)
                print()
                print(f"{' ' * 10} {'#' * 10} BUS INFO {'#' * 10}")
                print(f"Bus number : {show_id} \t\tDriver : {time}")
                # print(
                #     f"Arrival : {w['arrival']} \t\t\tDeparture Time : {w['departure']} \nFrom : \t{w['from_des']} \t\t\tTo : \t{w['to']}")
                # print()
                a = 1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}. {w['seat'][a - 1]}", end="\t")
                        a += 1
                    for j in range(2):
                        print(f"{a}. {w['seat'][a - 1]}", end="\t")
                        a += 1
                    print()
                print('*' * 50)
            else:
                print("No bus available")
                break

    def view_show_list(self):
        if len(self.show_list) == 0:
            print("No Show available")
        else:
            print()
            print('-' * 70)
            print()
            for idd, movie_name, time in self.show_list:
                # print(f"{' '*10} {'#'*10} SHOW LIST {'#'*10}")
                print(f"MOVIE NAME: {movie_name} \t\t SHOW ID: {idd} \t\t TIME: {time}")
            print('_' *70)


while True:
    obj = Hall(4, 4, 1111)
    obj2 = Star_Cinplex()
    obj.entry_show('ae123', 'Black Adam', 'Nov 04 2022 10:AM')
    obj.entry_show('ae50', 'Superman', 'Nov 04 2022 8: PM')
    print("1. VIEW ALL SHOWS TODAY\n2. VIEW AVAILABLE SEATS \n3. BOOK TICKET\n")
    user_input = int(input("Enter your option : "))
    if user_input == 1:
        obj.view_show_list()
        print("Seats list:: ")
        print(obj.seats)
        print("seats in row wise: :")
        print(obj.show_list)
        # obj.show_seats()

    elif user_input == 2:
        show_id = input("Enter Show ID: ")
        # all movie info will show(movie_name, time) and available seats will be shown
        # obj.seats
        # b.create_account()
    elif user_input == 3:
        # customer_name = input("Enter Customer name: ")
        # phone_number = input("Enter Phone number: ")
        # show_id = input("Enter Show ID: ")
        # no_of_ticket = int(input("Enter no of ticket: "))
        # seat_no = int(input("Enter seat No : "))
        # idd = input("Entre show idd: ")
        obj.book_seats()
        print("Successfully Booked")

        # after enter this info successfully: it will show:
        '''user name:   phone, movie name, movie time: '''
        '''ticket no: \n Hall NO: '''

    elif user_input == 4:
        # show_id = input("Enter id no: ")
        # # print(obj.show_list)
        # obj.reservation(show_id, seat_no)

        obj.book_seats()







    # obj2.entry_hall(112, 1510334, 'hall123')
    # print(Star_Cinema.hall_list)
    # print(obj2.hall_list)
    # print(obj.hall_list)

    # obj.entry_show()
    # obj.book_seats(
    # obj.book_seats()

    # print(obj.show_list)
    # print(obj.seats)

    # print(obj.view_show_list())

    # obj.book_seats()
    # print(vars(obj))


# obj.entry_show('Black Adam', 'ae123', 'Nov 04 2022 10:AM')
# # obj.entry_show('Superman', 'ae50', 'Nov 04 2022 8: PM')
# print(obj.movie_name)
# print(obj.id)
# print(obj.time)


