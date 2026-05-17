   # VIEW ALL RECORDS
    def records(self):
        try:
            print(open(self.rf).read())

        except:
            print("No records")

    # VIEW MY BOOKS
    def mybooks(self, u):

        found = False

        try:
            for line in open(self.rf):

                b = line.strip().split(",")

                if b[0] == u:
                    found = True
                    print(f"{b[1]} | {b[2]} | {b[3]}")

            if not found:
                print("No borrowed books")

        except:
            print("No records")

    # MAIN PROGRAM
    def run(self):

        while True:

            print("\n1.Login\n2.Exit")

            try:
                c = int(input("Choice: "))

                if c == 2:
                    break

                if c != 1:
                    print("Invalid option")
                    continue

                user = self.login()

                if not user:
                    continue

                while True:

                    # LIBRARIAN MENU
                    if user.r == "librarian":

                        print("\n1.View")
                        print("2.Add")
                        print("3.Update")
                        print("4.Delete")
                        print("5.Search")
                        print("6.Records")
                        print("7.Logout")

                    # MEMBER MENU
                    else:

                        print("\n1.View")
                        print("2.Search")
                        print("3.Borrow")
                        print("4.Return")
                        print("5.My Books")
                        print("6.Logout")

                    try:

                        x = int(input("Choice: "))

                        if x == 1:
                            self.books()

                        elif x == 2:
                            self.add() if user.r == "librarian" else self.search()

                        elif x == 3:
                            self.update() if user.r == "librarian" else self.borrow(user.u)

                        elif x == 4:
                            self.delete() if user.r == "librarian" else self.return_book(user.u)

                        elif x == 5:
                            self.search() if user.r == "librarian" else self.mybooks(user.u)

                        elif x == 6:

                            if user.r == "librarian":
                                self.records()
                            else:
                                break

                        elif x == 7 and user.r == "librarian":
                            break

                        else:
                            print("Invalid option")

                    except:
                        print("Enter number only")

            except:
                print("Enter number only")


Library().run()
