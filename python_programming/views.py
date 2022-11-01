class Star_Cinema:
    _hall_list = []

    def entry_hall(self, hall):
        Star_Cinema._hall_list.append(hall)


class Hall(Star_Cinema):
    _seats = {}
    _show_list = []

    def __init__(self, rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self._seats = Hall._seats
        self._show_list = Hall._show_list

    def entry_show(self, id, movie_name, time):
        Hall._show_list.append((id, movie_name, time))
        Hall._seats[id] = []
        tmp = 65
        for i in range(self.rows):
            tmpList = []
            for j in range(self.cols):
                strSeat = f"{chr(tmp)}{j + 1}"
                tmpList.append(strSeat)
            tmp += 1
            Hall._seats[id].append(tmpList)

    def book_seats(self, customer_name, phone_number, id, seats):
        booked_seat_list = []
        for k in self._hall_list:
            for seat in k['_seats'][id]:
                for i in seats:
                    try:
                        row = ord(i[0]) - 65
                        col = int(i[1]) - 1
                        if k['_seats'][id][row][col] != 'X':
                            k['_seats'][id][row][col] = 'X'
                            booked_seat_list.append(i)
                        else:
                            print(f"THIS SEAT {i} IS ALREADY BOOKED!!")
                    except:
                        print(f"THIS {i} SEAT IS NOT FOUND!!")
                break
        if len(booked_seat_list) != 0:
            print('-' * 110)
            print(f"YOU HAVE SUCCESSFULLY BOOKED THESE SEAT {booked_seat_list}")
            print()
            print(f"Name : {customer_name}\t\t Phone Number : {phone_number}")
            print('-' * 110)

    def view_show_list(self):
        print("." * 110)
        for hall in self._hall_list:
            for show in hall['_show_list']:
                print(f"\tMOVIE NAME : {show[1]}\t\tSHOW ID : {show[0]}\t\tSHOW TIME : {show[2]}")
        print("." * 110)

    def view_available_seats(self, id):
        isFound = True
        print('*' * 68)
        for listn in self._hall_list:
            if id in listn['_seats']:
                for yy in listn['_show_list']:
                    if id == yy[0] and isFound:
                        print(f"MOVIE NAME : {yy[1]}\t\tTIME : {yy[2]}")
                        isFound = True
            else:
                print("\tId didn't match with any show!")
                isFound = False
                break
        if isFound == True:
            print("\t\tX for already booked seats")
        print('*' * 68)
        if isFound == True:
            for k in self._hall_list:
                for seat in k['_seats'][id]:
                    for i in seat:
                        print(i, end="\t\t")
                    print()


hall = Hall(5, 5, 1)
hall.entry_show("M353", "The Old Man", "Sat Oct 29 10:00 AM")
hall.entry_show("M333", "Interstellar", "Sun Oct 29 12:00 PM")
hall.entry_hall(vars(hall))

while True:
    print("1. VIEW ALL SHOWS TODAY ")
    print("2. VIEW AVAILABLE SEATS ")
    print("3. BOOK TICKET ")
    getOption = input("ENTER OPTION: ")
    if getOption == "1":
        hall.view_show_list()
    elif getOption == "2":
        id = input("ENTER SHOW ID: ").upper()
        hall.view_available_seats(id)
    elif getOption == "3":
        customer_name = input("ENTER CUSTOMER NAME : ").upper()
        customer_phone = input("ENTER CUSTOMER PHONE NUMBER : ")
        show_id = input("ENTER SHOW ID : ").upper()
        total_ticket = int(input("ENTER NUMBER OF TICKETS : "))
        n = 1
        booked_seat = []
        for k in range(total_ticket):
            seat_number = input(f"ENTER {n}. NO. SEAT NAME : ").upper()
            n += 1
            booked_seat.append(seat_number)
        hall.book_seats(customer_name, customer_phone, show_id, booked_seat)
    else:
        break

