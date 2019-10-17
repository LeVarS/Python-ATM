from Card import Card

def main():
    print("Welcome to the ATM.")
    admin()

def admin():
    acctNum = []
    PIN = []
    accName = []
    dateMon = []
    dateDay = []
    dateYear = []
    fullDate = []
    expDate = []
    addressNums = []
    addressStreet = []
    fullAddress = []
    balance = []
    phoneNum = []

    i = 0
    cards = 0
    blocked = False

    pick = int(input("\nType 1 to continue or 2 to exit.\n"))

    while pick != 2:
        user = int(input("\nMenu options to enter:\n" +
            "1: Add a new ATM card\n" +
            "2: View ATM Machine Status\n" +
            "3: Update ATM Card\n" +
            "4: Exit\n"))
        if user == 1:
            card1 = Card()
            card1.getCardInfo()
            # print("You have entered 1 to Add a new ATM Card.")
            # cards = cards + 1
            #
            # acctNum.append(int(input("Enter new Account Number: ")))
            # PIN.append(int(input("Enter new PIN: ")))
            # accName.append(input("Enter new Account Name: "))
            # dateMon.append(int(input("Enter date of Month: ")))
            # dateDay.append(int(input("Enter date of Day: ")))
            # dateYear.append(int(input("Enter date of Year: ")))
            # fullDate.append(str(dateMon[i]) + "/" + str(dateDay[i]) + "/" + str(dateYear[i]))
            # expDate.append(str(dateMon[i]) + "/" + str(dateDay[i]) + "/" + str((dateYear[i]+10)))
            # addressNums.append(int(input("Enter the numbers of your address: ")))
            # addressStreet.append(input("Enter street name of address: "))
            # fullAddress.append(str(addressNums[i]) + " " + addressStreet[i])
            # balance.append(int(input("Enter balance on this card: ")))
            # phoneNum.append(int(input("Enter phone number for card (NO dashes): ")))
            if blocked == False:
                print("Card Status: activated")
            else:
                print("Card Status: blocked")


            #just to check for correctness
            print("Cards: " + str(cards))
            print("Accounts: " + str(acctNum))
            print("PIN: " + str(PIN))
            print("Name: " + str(accName))
            print("Date: " + str(fullDate)) #doesn't work 2nd time b/c of i (below)
            print("Exp Date: " + str(expDate)) #doesn't work 2nd time b/c of i (below)
            print("Address: " + str(fullAddress))
            print("Balance: $" + str(balance))
            print("Phone: " + str(phoneNum))
            print("i = " + str(i)) #not incrementing, always = 1
            i = i + 1
            break



        elif user == 2:
            print("You have entered 2 to view ATM Machine Status.")
            user2 = int(input("Menu options to enter:\n" +
                              "1: View ATM Address\n" +
                              "2: View ATM Machine Status\n" +
                              "3: View Last Refill Date\n" +
                              "4: View Next Refill Date\n" +
                              "5: View Minimum Balance Enquiry\n" +
                              "6: View Current Balance\n" +
                              "7: Exit\n"))
            if user2 == 1:
                print("ATM Address is 408 CCT Columbus State University")
            elif user2 == 2:
                print("ATM Machine Status is... Excellent!")
            elif user2 == 3:
                print("Last Refill Date: 11/1/2019")
            elif user2 == 4:
                print("Next Refill Date: 12/1/2019")
            elif user2 == 5:
                print("Minimum Balance Enquiry: $200")
            elif user2 == 6:
                if cards == 0:
                    print("You need to add a card!")
                else:
                    chkAcct = int(input("Which account would you like to check the balance of?"))
                    if chkAcct == cards:
                        chances = 0
                        while chances < 3:
                            chkPIN = int(input("Enter the PIN for this card: "))
                            if chkPIN == PIN[i]:
                                print("Correct!")
                                chkPhoneNum = int(input("Please enter Phone number: "))
                                if chkPhoneNum == phoneNum[i]:
                                    print("Correct!")
                                    print("Your current balance is: $" + str(balance))
                                    break
                                else:
                                    print("Wrong Phone Number.")
                                    chances = chances + 1
                            else:
                                print("Wrong PIN.")
                                chances = chances + 1
                    else:
                        print("You do not have that many cards.")
            elif user2 == 7:
                break
            else:
                print("ATM Machine Error.\n")



        elif user == 3:
            if cards == 0:
                print("You need to add a card!")
            else:
                chkAcct = int(input("Which account would you like to update: "))
                if chkAcct == cards:
                    update = int(input("\nMenu options for update:\n" +
                                       "1: Block Card\n" +
                                       "2: Activate Card\n" +
                                       "3: Reset PIN\n" +
                                       "4: Reset Phone Number\n" +
                                       "5: View History\n" +
                                       "6: Update Expiration Date\n" +
                                       "7: Exit\n"))
                    if update == 1:
                        blocked == True
                        print("Your card has been blocked.")
                    elif update == 2:
                        activate = int(input("Which card would you like to activate: "))
                        if activate == cards:
                            print("Card Activated.")
                            blocked == False
                        else:
                            print("You do not have that many cards.")
                    elif update == 3: #doesn't work
                        resetPIN = int(input("Which card would you like to reset PIN on: "))
                        if resetPIN == cards:
                            PIN[resetPIN] = int(input("What is your new PIN: "))
                        else:
                           print("You do not have that many cards.")
                    elif update == 4: #doesn't work
                        resetPhone = int(input("Which card would you like to reset PIN on: "))
                        if resetPhone == cards:
                            phoneNum[resetPhone] = int(input("What is your new" +
                                                             " phone number: "))
                        else:
                           print("You do not have that many cards.")
                    elif update == 5:
                        hist = int(input("Which account would you like to view" +
                                         " the history of: "))
                        if hist == cards:
                            #what is supposed to go here?
                            #We do not ask for deposit/withdraw.
                            print("View History.")
                        else:
                           print("You do not have that many cards.")
                    elif update == 6:
                        exp = int(input("Which card would you like to update" +
                                        " the expiration date on: "))
                        if exp == cards: #probably does not work
                            dateYear[exp] = dateYear[exp] + 10
                        else:
                            print("You do not have that may cards.")
                    else:
                        print("Back")
                else:
                    print("Account not found.")
                    break
        elif user == 4:
            break
        else:
            print("ATM Machine Error.\n")





if __name__ == "__main__":
    main()
