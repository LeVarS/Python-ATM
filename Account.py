from Card import Card
class Account:


    def __init__(self, acc_num):
        self.acc_num = acc_num
        self.acc_name = ""
        self.phone = ""
        self.__cards = []
        self.__history = []

    def register(self):
        # self.acc_num = self.__get_acc_num()
        self.acc_name = self.__get_acc_name()
        self.phone = self.__get_phone_num()

    def addCard(self):
        newCard = Card()
        newCard.activate ()
        self.__cards.append(newCard)

    # def __get_acc_num(self):
    #     acc_num = input("Enter new Account Number: ")
    #     while not acc_num.isdigit():
    #         print("Invalid Account Number. Must only be digits. ")
    #         acc_num = input("Please enter a valid Account Number (digits only): ")
    #     return int(acc_num)

    def __get_acc_name(self):
        acc_name = input("Enter new Account Name: ")
        while not acc_name.isalpha():
            print("Invalid Account Name. Must only be alphabetic characters. ")
            acc_name = input("Please enter a valid Account Name (alphabet only): ")
        return acc_name

    def __get_phone_num(self):
        phone_num = input("Enter phone number for account: ")
        while not phone_num.isdigit() or len(phone_num) != 10:
            phone_num = input("Invalid phone number. Must be a 10-digit number\n" +
                              "Please enter a valid phone number (10-digit number): ")
        return phone_num