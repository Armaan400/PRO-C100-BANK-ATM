class Atm:
    def _init_(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin
    
    def balanceinquiry(self):
        print("Your balance is $100")

    def cashwithdrawn(self,amount):
        new_amount = 100-amount
        print("YOU WITHDRAWED" +str(amount)+"REMAINING BALANCE"+str(new_amount))

def main(cardnumber,pin):
    name =input("ENTER YOUR NAME")
    print("HELLO," + name)
    cardnumber=input("INSERT YOUR CARD NUMBER")
    pin = input("ENTER YOUR PIN")
    