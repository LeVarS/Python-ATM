from Account import Account
import random

def main():
    print("Welcome to the ATM.")
    admin()

def admin():
    accounts = dict()
    atm_accounts = []
    i = 0
    cards = 0

    blocked = False
    running = True


    while running:
        user = int(input("\nMenu options to enter:\n" +
                         "1: Add a new ATM card\n" +
                         "2: View ATM Machine Status\n" +
                         "3: Update ATM Card\n" +
                         "4: Exit\n"))
        if user == 1:

            hasExistingAccount = input("Do you have an existing accoung? ('yes' or 'no'): ")
            while not hasExistingAccount.isalpha():
                hasExistingAccount = input("That was not a valid response.\n" +
                                           "Please enter 'yes' if you have an account. Otherwise, enter 'no': ")

            while hasExistingAccount.lower() != "yes" and hasExistingAccount.lower() != "no":
                hasExistingAccount = input("That was not a valid response.\n"+
                                           "Please enter 'yes' if you have an account. Otherwise, enter 'no': ")
                while not hasExistingAccount.isalpha():
                    hasExistingAccount = input("That was not a valid response.\n" +
                                               "Please enter 'yes' if you have an account. Otherwise, enter 'no': ")

            if hasExistingAccount.lower() == "yes":
                acc_num = input("Enter account number: ")
            else:
                acc_num = random.randint(100000, 500001)
            if acc_num not in accounts:

                print("Registering Account %s" % acc_num)
                newAccount = Account(acc_num)
                newAccount.register()
                print("\nAdding Card to Account %s" % acc_num)
                newAccount.addCard()
            else:

                print("\nAdding Card to Account %s" % acc_num)
                accounts[newAccount.acc_num] = newAccount
                newAccount.addCard()
                atm_accounts.append(newAccount)

        #     if blocked == False:
        #         print("Card Status: activated")
        #     else:
        #         print("Card Status: blocked")
        #
        #     # for i in card_list:
        #     #     i.printCardInfo()
        #
        #
        #
        # elif user == 2:
        #     print("You have entered 2 to view ATM Machine Status.")
        #     user2 = int(input("Menu options to enter:\n" +
        #                       "1: View ATM Address\n" +
        #                       "2: View ATM Machine Status\n" +
        #                       "3: View Last Refill Date\n" +
        #                       "4: View Next Refill Date\n" +
        #                       "5: View Minimum Balance Enquiry\n" +
        #                       "6: View Current Balance\n" +
        #                       "7: Exit\n"))
        #     if user2 == 1:
        #         print("ATM Address is 408 CCT Columbus State University")
        #     elif user2 == 2:
        #         print("ATM Machine Status is... Excellent!")
        #     elif user2 == 3:
        #         print("Last Refill Date: 11/1/2019")
        #     elif user2 == 4:
        #         print("Next Refill Date: 12/1/2019")
        #     elif user2 == 5:
        #         print("Minimum Balance Enquiry: $200")
        #     elif user2 == 6:
        #         if cards == 0:
        #             print("You need to add a card!")
        #         else:
        #             chkAcct = int(input("Which account would you like to check the balance of?"))
        #             if chkAcct == cards:
        #                 chances = 0
        #                 while chances < 3:
        #                     chkPIN = int(input("Enter the PIN for this card: "))
        #                     if chkPIN == PIN[i]:
        #                         print("Correct!")
        #                         chkPhoneNum = int(input("Please enter Phone number: "))
        #                         if chkPhoneNum == phoneNum[i]:
        #                             print("Correct!")
        #                             print("Your current balance is: $" + str(balance))
        #                             break
        #                         else:
        #                             print("Wrong Phone Number.")
        #                             chances = chances + 1
        #                     else:
        #                         print("Wrong PIN.")
        #                         chances = chances + 1
        #             else:
        #                 print("You do not have that many cards.")
        #     elif user2 == 7:
        #         running = False
        #     else:
        #         print("ATM Machine Error.\n")
        #
        #
        #
        # elif user == 3:
        #     if cards == 0:
        #         print("You need to add a card!")
        #     else:
        #         chkAcct = int(input("Which account would you like to update: "))
        #         if chkAcct == cards:
        #             update = int(input("\nMenu options for update:\n" +
        #                                "1: Block Card\n" +
        #                                "2: Activate Card\n" +
        #                                "3: Reset PIN\n" +
        #                                "4: Reset Phone Number\n" +
        #                                "5: View History\n" +
        #                                "6: Update Expiration Date\n" +
        #                                "7: Exit\n"))
        #             if update == 1:
        #                 blocked == True
        #                 print("Your card has been blocked.")
        #             elif update == 2:
        #                 activate = int(input("Which card would you like to activate: "))
        #                 if activate == cards:
        #                     print("Card Activated.")
        #                     blocked == False
        #                 else:
        #                     print("You do not have that many cards.")
        #             elif update == 3: #doesn't work
        #                 resetPIN = int(input("Which card would you like to reset PIN on: "))
        #                 if resetPIN == cards:
        #                     PIN[resetPIN] = int(input("What is your new PIN: "))
        #                 else:
        #                    print("You do not have that many cards.")
        #             elif update == 4: #doesn't work
        #                 resetPhone = int(input("Which card would you like to reset PIN on: "))
        #                 if resetPhone == cards:
        #                     phoneNum[resetPhone] = int(input("What is your new" +
        #                                                      " phone number: "))
        #                 else:
        #                    print("You do not have that many cards.")
        #             elif update == 5:
        #                 hist = int(input("Which account would you like to view" +
        #                                  " the history of: "))
        #                 if hist == cards:
        #                     #what is supposed to go here?
        #                     #We do not ask for deposit/withdraw.
        #                     print("View History.")
        #                 else:
        #                    print("You do not have that many cards.")
        #             elif update == 6:
        #                 exp = int(input("Which card would you like to update" +
        #                                 " the expiration date on: "))
        #                 if exp == cards: #probably does not work
        #                     dateYear[exp] = dateYear[exp] + 10
        #                 else:
        #                     print("You do not have that may cards.")
        #             else:
        #                 print("Back")
        #         else:
        #             print("Account not found.")
        # elif user == 4:
        #     running = False
        #
        # else:
        #     print("ATM Machine Error.\n")





if __name__ == "__main__":
    main()
