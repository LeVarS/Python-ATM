class Card:
    """
    Constructor for Card object
    Sets the variables to default values
    """
    def __init__(self):
        self.pin = 0
        self.month = 0
        self.day = 0
        self.year = 0
        self.address_num = 0
        self.address_street = ""
        self.balance = 0

    """ 
    Function to assign values to the instance variables with input from the user 
    by using helper functions that retrieve and validate the input 
    """
    def activate(self):
        self.month = self.__get_month()
        self.day = self.__get_day()
        self.year = self.__get_year()
        self.address_num = self.__get_address_num()
        self.address_street = self.__get_address_street()
        self.balance = self.__get_balance()


    def printCardInfo(self):
        print(str(self.pin) + "\t" +
              str(self.month) + "\t" +
              str(self.day) + "\t" +
              str(self.year) + "\t" +
              str(self.address_num) + "\t" +
              str(self.address_street) + "\t" +
              str(self.balance))


    """
    These functions are used to get the information from the user 
    and store it in the variables above 
    
    The underscores ("__") in front of the function names is how 
    Python makes definitions private to only the class
    
    One underscore ("_") in front of function or variable names
    is how Python makes functions or variables protected 
    so only the origin class and possible child classes can access them
    """

    def __get_pin(self):
        pin = input("Enter new PIN: ")
        while not pin.isdigit() or len(pin) != 4:
            print("Invalid PIN. Pin must be only 4 digits. ")
            pin = input("Please enter a valid PIN (4 digits only): ")
        return int(pin)



    def __get_month(self):
        month = input("Enter date of Month: ")
        while not month.isdigit():
            month = input("Please enter only digits for the month\n" +
                          "Please enter a valid month. (1-12): ")
        while int(month) < 1 or int(month) > 12:
            print("invalid month. Must be between 1 and 12.")
            month = input("Please enter a valid month. (1-12): ")
            while not month.isdigit():
                month = input("Please enter only digits for the month\n" +
                              "Please enter a valid month. (1-12): ")
        return month

    def __get_day(self):
        day = input("Enter day (1-31): ")
        while not day.isdigit():
            day = input("Please enter only digits for the day\n" +
                          "Please enter a valid day. (1-31): ")
        while int(day) < 1 or int(day) > 31:
            print("invalid day. Must be between 1 and 31.")
            day = input("Please enter a valid day. (1-31): ")
            while not day.isdigit():
                day = input("Please enter only digits for the day\n" +
                              "Please enter a valid day. (1-31): ")
        return day

    def __get_year(self):
        year = input("Enter year (2015-present): ")
        while not year.isdigit():
            year = input("Please enter only digits for the year\n" +
                          "Please enter a valid year. (2015-present): ")
        while int(year) < 2015 or int(year) > 2019:
            print("invalid month. Must be between 2015 and 2019.")
            year = input("Please enter a valid year. (2015-present): ")
            while not year.isdigit():
                year = input("Please enter only digits for the month\n" +
                              "Please enter a valid year. (2015-present): ")
        return year

    def __get_address_num(self):
        address_num = input("Enter the numbers of your street address: ")
        while not address_num.isdigit():
            print("Invalid address number. Must only be digits. ")
            address_num = input("Please enter a valid address number (digits only): ")
        return int(address_num)

    def __get_address_street(self):
        address_street = input("Enter the street name of the address: ")
        while not address_street.isalpha():
            print("Invalid street name. Must only be alphabetic characters. ")
            address_street = input("Please enter a valid street name (alphabet only): ")
        return address_street

    def __get_balance(self):
        balance = input("Enter balance on this card: ")
        while not balance.isdigit():
            balance = input("Invalid balance. Must be a positive number\n" +
                            "Please enter a valid balance (positive number): ")
        while int(balance) < 0:
            balance = input("Invalid balance. Must be a positive number\n"+
                            "Please enter a valid balance (positive number): ")
            while not balance.isdigit():
                balance = input("Invalid balance. Must be a positive number\n" +
                                "Please enter a valid balance (positive number): ")
        return int(balance)


