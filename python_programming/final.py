class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        # self.entry_hall(self)
        self.seats = {}
        self.show_list = []

    def entry_show(self, idd, movie_name, time):
        self.show_list.append((idd, movie_name, time))
        # self.seats[idd] = ([[f"empty" for i in range(self.rows)] for j in range(self.cols)])
        self.seats[idd] = []
        chr_val = 65
        for i in range(self.rows):
            seat_list = []
            for j in range(self.cols):
                seat_no = f"{chr(chr_val)}{j + 1}"
                seat_list.append(seat_no)
            chr_val += 1
            self.seats[idd].append(seat_list)

    def book_seats(self, customer_name, phone_number, idd, book_seats):
        booked_seat_list = []
        for hall in self.hall_list:
            for hall_seat in hall['seats'][idd]:
                for i in book_seats:
                    try:
                        row = ord(i[0]) - 65
                        col = int(i[1]) - 1
                        if hall['seats'][idd][row][col] != 'X':
                            hall['seats'][idd][row][col] = 'X'
                            booked_seat_list.append(i)
                        else:
                            print(f"THIS SEAT {i} IS ALREADY BOOKED!!")
                            print()
                    except:
                        print(f"THIS SEAT {i} NOT FOUND")
                        print()
                break
        if len(booked_seat_list) != 0:
            print('-' * 110)
            print(f"{'#'*12}YOU HAVE SUCCESSFULLY BOOKED THESE SEAT {'#'*12}")
            print()
            print(f"Name : {customer_name}\t\t Phone Number : {phone_number}")
            print(f"Hall: {hall_obj.hall_no}")
            print()
            idd_list = list(filter(lambda x: x[0] == idd, self.show_list))
            # movie_name = [x[1] for x in self.show_list if x[0] == idd] # show value in a list

            for idd, movie_name, time in idd_list:
                print("Movie Name: ", movie_name, '\t\t\t', "Time: ", time)
            print("\n")
            print(f"YOU HAVE SUCCESSFULLY BOOKED THESE SEAT {booked_seat_list}")
            print('\n')
            print('-' * 110)

    def view_available_seats(self, idd):
        flag = True
        print('-' * 50)
        for hall in self.hall_list:
            if idd in hall['seats']:
                for show in hall['show_list']:
                    if idd == show[0] and flag:
                        print(f"MOVIE NAME : {show[1]}\t\tTIME : {show[2]}")
                        flag = True
            else:
                print("\tId didn't match with any show!")
                flag = False
                break
        if flag == True:
            print("\t\tX for already booked seats")
            print('*' * 50)
        if flag == True:
            for hall in self.hall_list:
                for seat in hall['seats'][idd]:
                    for i in seat:
                        print(i, end="\t\t")
                    print()


    def book_seat(self, customer_name, phone_no, idd, ticket_amount):
        if idd in self.seats:
            # amount_ticket = int(input("Enter amount of tickets: "))
            seat_list = []
            for i in range(ticket_amount):
                # seat_row = int(input(f"row: "))
                # seat_col = int(input(f"col: "))
                seat_row, seat_col = map(int, input("Enter seat row and column no: ").split())
                seat_tuple = tuple((seat_row, seat_col))
                seat_list.append(seat_tuple)

            print()
            print(f"{'#' * 12} TICKET BOOKED SUCCESSFULLY!! {'#' * 12}")
            print(f"{'-' * 70}")
            print()
            print(f"Name: {customer_name}")
            print(f"Phone Number: {phone_number}")
            print()
            idd_list = list(filter(lambda x: x[0] == idd, self.show_list))
            # movie_name = [x[1] for x in self.show_list if x[0] == idd] # show value in a list

            for idd, movie_name, time in idd_list:
                print("Movie Name: ", movie_name, '\t\t\t', "Time: ", time)

            print('Tickets: ', seat_list)
            print(f"Hall: {obj.hall_no}")
            print("\n")
            print(f"YOU HAVE SUCCESSFULLY BOOKED THESE SEAT {booked_seat_list}")
            print(f"{'-' * 70}")
            print()

            # obj.book_seat(customer_name, phone_no, idd, ticket_amount)
        else:
            print("Show Id is not available.")
        #
        # if idd in self.seats:
        #     # print(self.seats[idd])
        #     seat_no = int(input("Enter seat no: "))
        #
        #     for i in range(1, len(self.seats[idd])):
        #         for j in range(1, len(self.seats[idd][i])):
        #             print(f"({i},{j}).", self.seats[idd][i][j], end=" ")
        #         print()
        #     print()

    def view_show_list(self):
        if len(self.show_list) == 0:
            print("No Show available")
        else:
            print()
            print('-' * 70)
            print()
            for idd, movie_name, time in self.show_list:
                print(f"MOVIE NAME: {movie_name} \t\t SHOW ID: {idd} \t\t TIME: {time}")
            print('_' * 70)


hall_obj = Hall(5, 5, 123)
obj2 = Star_Cinema()
hall_obj.entry_show('ae123', 'Black Adam', 'FRI NOV 04 2022 10:00 AM')
hall_obj.entry_show('ae50', 'Superman', 'FRI NOV 04 2022 8:00 PM')
hall_obj.entry_hall(vars(hall_obj))

while True:
    print("1. VIEW ALL SHOWS TODAY\n2. VIEW AVAILABLE SEATS \n3. BOOK TICKET\n")
    user_input = int(input("ENTER YOUR OPTION : "))
    if user_input == 1:
        hall_obj.view_show_list()
        # print(obj.seats)
        # print(obj.show_list)
        # obj.show_seats()

    elif user_input == 2:
        show_id = input("Enter SHOW ID: ")
        hall_obj.view_available_seats(show_id)
    elif user_input == 3:
        customer_name = input("Enter Customer name: ")
        phone_number = input("Enter Phone number: ")
        show_id = input("Enter Show id: ")
        amount_of_ticket = int(input("Enter amount of tickets: "))
        booked_seats = []
        for seat in range(amount_of_ticket):
            seat_number = input(f"Enter for {seat + 1}. No seat : ").upper()
            booked_seats.append(seat_number)
        hall_obj.book_seats(customer_name, phone_number, show_id, booked_seats)

    else:
        break
