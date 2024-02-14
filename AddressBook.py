class AddressBook:
    pass

class Contact:
    def __init__(self,first,last,address, city,state,zip,phone,email):
        self.first=first
        self.last=last
        self.address=address
        self.city=city
        self.state=state
        self.zip=zip
        self.phone=phone
        self.email=email
    def show_contact(self):
        print(f"first name = {self.first}")
        print(f"last name = {self.last}")
        print(f"address = {self.address}")
        print(f"city = {self.city}")
        print(f"state = {self.state}")
        print(f"zip = {self.zip}")
        print(f"phone number = {self.phone}")
        print(f"email = {self.email}")
 

def addCont():
    first=input("Enter the first name: ")
    last=input("Enter the last name: ")
    address=input("Enter the address: ")
    city=input("Enter the city name: ")
    state=input("Enter the state name: ")
    zip=input("Enter the zip : ")
    phone=input("Enter the phone number: ")
    email=input("Enter the email: ")

    cont=Contact(first,last,address,city,state,zip,phone,email)
    cont.show_contact()
    
if __name__=='__main__':
        addCont()
        