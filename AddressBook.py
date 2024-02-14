class AddressBook:
    def __init__(self):
        self.AddressBook_dict={}
        
    def add_contact(self,Contact_obj):
        FullName=Contact_obj.Contact_dict['first']+Contact_obj.Contact_dict['last']
        self.AddressBook_dict.update({FullName:Contact_obj})
        print("Contact added in Address book")
        
    def ShowAddressBook(self):
        print("Below is the Address Book: ")
        print(self.AddressBook_dict)

class Contact:
    def __init__(self,first,last,address, city,state,zip,phone,email):
        self.Contact_dict={'first':first,'last':last,'address':address,'city':city,'state':state,'zip':zip,'phone':phone,'email':email}
        # self.first=first
        # self.last=last
        # self.address=address
        # self.city=city
        # self.state=state
        # self.zip=zip
        # self.phone=phone
        # self.email=email
    def show_contact(self):
        print(self.Contact_dict)
        # print(f"first name = {self.first}")
        # print(f"last name = {self.last}")
        # print(f"address = {self.address}")
        # print(f"city = {self.city}")
        # print(f"state = {self.state}")
        # print(f"zip = {self.zip}")
        # print(f"phone number = {self.phone}")
        # print(f"email = {self.email}")
 

def addCont():
    Address=AddressBook()
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
    choice=input("Add it in AddressBook? Type 'yes' or 'no'  : ")
    if choice=='yes':
        Address.add_contact(cont)
        Address.ShowAddressBook()
    else:
        exit()
    
    
if __name__=='__main__':
        addCont()
        
        
        