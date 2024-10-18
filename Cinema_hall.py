class Star_Cinema:
    _hall_list = []

    def entry_hall(self, rows, cols, hall_no=None):
        hall = Hall(rows, cols, hall_no)
        self._hall_list.append(hall)


class Hall(Star_Cinema):

    def __init__(self, rows, cols, hall_no):
        self._rows = rows
        self._cols = cols
        self.hall_no = hall_no
        self._show_list = []
        self._seats = {}

    def entry_show(self, id, movie_name, time):
        lst = (id, movie_name, time)
        self._show_list.append(lst)
        seat = self.make_seat()
        self._seats[id] = seat

    def make_seat(self):
        seats_mat = []
        for i in range(self._rows):
            row_list = []
            for j in range(self._cols):
                row_list.append(0)
            seats_mat.append(row_list)
        
        return seats_mat


    def book_seats(self, id, lst):
        if id in self._seats:
            matrix = self._seats[id]
            seats = [tuple(map(int, seat.split(','))) for seat in lst.split()]
            for seat in seats:
                if len(seat) == 2:
                    i, j = seat
                    i -= 1
                    j -= 1
                    if 0 <= i < self._rows and 0 <= j < self._cols:
                        if matrix[i][j] == 1:
                            print(f"Seat [{i+1}, {j+1}] is not available")
                        else:
                            matrix[i][j] = 1
                            print(f"Seat [{i+1}, {j+1}] is Booked")
                    else:
                        print(f"Seat [{i+1}, {j+1}] is not available")
                else:
                    print(f"Invalid seats")
        else:
            print("Not available.")


    def view_show_list(self):
        if len(self._show_list) == 0:
            print("Show not available")
        else:
            for show in self._show_list:
                print(f"Show ID: {show[0]}, Movie Name: {show[1]}, Time: {show[2]}")


    def view_available_seats(self, id):
        if len(self._show_list) == 0:
            print("\nShow not available")
        else:
            if id in self._seats:
                matrix = self._seats[id]
                cnt = 0
                for li in matrix:
                    for j in li:
                        if j == 0:
                            cnt += 1
                print(f"\nAvailable Seat: {cnt} and Total Seats: {self._cols * self._rows}\n")
                for li in matrix:
                    lst = []
                    for j in li:
                        lst.append(j)
                    print(lst)
                    print()
            else:
                print("\nInvalid ID")




star_cinema = Star_Cinema()
star_cinema.entry_hall(6, 7)
star_cinema.entry_hall(4, 5)

hall1 = star_cinema._hall_list[0]
hall1.entry_show(len(hall1._show_list) + 1, "Arya 2", "6:00 PM")
hall1.entry_show(len(hall1._show_list) + 1, "International Khiladi", "8:00 PM")

hall2 = star_cinema._hall_list[1]
hall2.entry_show(len(hall2._show_list) + 1, "Tur naam", "6:00 PM")
hall2.entry_show(len(hall2._show_list) + 1, "Premi", "9:00 PM")

print("*****WELCOME!*****")



def counter():
    run = True
    while run:
        print()
        print("Options:")
        print("1: View Show List")
        print("2: View available seats")
        print("3: Book Seats")
        print("4: Exit")


        n = int(input("Enter hall number (1 or 2): "))
        if n not in [1, 2]:
            print("Invalid hall number.")
            continue
        hall = star_cinema._hall_list[n - 1]

        ch = int(input("Enter your Option between (1 to 4): "))

        if ch == 1:
            hall.view_show_list()
        elif ch == 2:
            if len(hall._show_list) == 0:
                print("\nShow not available")
            else:

                id = int(input("Enter show id: "))
                hall.view_available_seats(id)

        elif ch == 3:
            if len(hall._show_list) == 0:
                print("\nShow not available")
            else:

                hall.view_show_list()

                id = int(input("Enter show id: "))

                valid = id in [show[0] for show in hall._show_list]
                if valid:
                    hall.view_available_seats(id)
                    print(f"How many seats you want : ")
                    x = input("Enter you seat number : ")
                    seats = input(f"Enter seat numbers, for examle 1,1 1,2 1,3 : ")

                    hall.book_seats(id, seats)
                else:
                    print("\nInvalid Id")

        elif ch == 4:
            break
        else:
            print("Invalid Option.")
            continue





while True:
    print("\nOptions:")
    print("1: View Hall")
    print("2: Exit")
    ch = int(input("Enter your option (1/2): "))

    if ch == 1:
        for i in range(len(star_cinema._hall_list)):
            print(f"{i + 1}: hall {i + 1}")
        x = int(input(f"Enter your Option (1 to {len(star_cinema._hall_list)}): "))
        hall = star_cinema._hall_list[x - 1]
        counter()
    elif ch == 2:
        print("Thank you for using our booking system")
        break
    else:
        print("Invalid option")