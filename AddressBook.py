class AddressBook:
    def __init__(self):
        self.addressbookDict={}
        
    def add_contact(self,Contact_obj):
        fullname=Contact_obj.Contact_dict['first']+ " "+ Contact_obj.Contact_dict['last']
        self.addressbookDict.update({fullname:Contact_obj})
        print("Contact added in Address book")
        
    def show_addressbook(self):
        print("Below is the Address Book: ")
        print(self.addressbookDict)
        
    def edit_addressbook(self,name):
        if name in self.addressbookDict.keys():
            print(self.addressbookDict[name].show_contact())
            self.addressbookDict[name].edit_contact(name)
            print(self.addressbookDict[name].show_contact())
    def delete_cont_from_addressbook(self,name):
        if name in self.addressbookDict.keys():
            print("The below contact will be deleted from the Addressbook: ")
            print(self.addressbookDict[name].show_contact())
            del self.addressbookDict[name]
            print("Your contact has been deleted: ")
            print(self.addressbookDict)
            
            
            

class Contact:
    def __init__(self,first,last,address, city,state,zip,phone,email):
        self.Contact_dict={'first':first,'last':last,'address':address,'city':city,'state':state,'zip':zip,'phone':phone,'email':email}
    
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
    def edit_contact(self,name):
        val=input("Enter the key you want to change :  ")
        if val in self.Contact_dict:
            toval=input("Enter the value you want to change to :")
            self.Contact_dict[val]=toval
            print("your details are edited")
            # print(self.Contact_dict.show_contact())
            
        
    
if __name__=='__main__':
        print("Welcome to the Address Book management!!!")
        
        print("please add initial contact :")
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
            Address.show_addressbook()
        
        
        endit='no'
        while(endit!='yes'):    
            print("1. add another contact")
            print("2. edit a contact")
            print("3. delete a contact")
            print("   ")
            print("if you want to exit enter 'yes' to exit ")
            choice= input("Enter your choice")
            if choice == '1':
                first=input("Enter the first name: ")
                last=input("Enter the last name: ")
                address=input("Enter the address: ")
                city=input("Enter the city name: ")
                state=input("Enter the state name: ")
                zip=input("Enter the zip : ")
                phone=input("Enter the phone number: ")
                email=input("Enter the email: ")
                cont2=Contact(first,last,address,city,state,zip,phone,email)
                cont2.show_contact()
                choice=input("Add it in AddressBook? Type 'yes' or 'no'  : ")
                if choice=='yes':
                    Address.add_contact(cont2)
                    Address.show_addressbook()
                endit='no'
            if choice=='2':
                name=input("Enter the full name of the person you want to edit details of : ")
                if name in Address.addressbookDict.keys():
                    Address.edit_addressbook(name)
            if choice=='3':
                name=input("Enter the full name of the person you want to delete details of : ")
                if name in Address.addressbookDict.keys():
                    Address.delete_cont_from_addressbook(name)
                
            if choice=='yes':
                endit='yes'
                
            
    

                
        
        