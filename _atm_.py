from datetime import datetime
stamp = datetime.now().strftime("%d-%m-%y %H:%M")
n=3
opin = 1234
balance = 5000
def verify_pin(pin):
    return pin == "1234"
def show_balance(balance):
    print("Balance:",balance)
while True:
    pin = int(input("Please enter your pin: "))
    if pin == opin:
        print("Your pin is valid")
        while True:
            Action = str(input("What would you like to do (W/D/E)"))
            print("Your balance is: ",balance)
            if Action == "W":
                if balance>0:
                    withdraw = int(input("How much would you like to withdraw: "))
                    if balance>=withdraw:
                        balance = balance-withdraw
                        print("Your balance is ",balance)
                        print("Reciept time: ",stamp)
                    else:
                        print("You dont have enough balance in your account")
                elif balance<=0:
                    print("You cannot make a withdrawal")
            elif Action == "D":
                deposit = int(input("How much would you like to deposit: "))
                balance = balance+deposit
                print("Your balance is ",balance)
                print("Recipet time: ",stamp)
            elif Action == "E":
                i =n
                break
    elif pin != opin:
        print("Please enter a valid pin")
        break
