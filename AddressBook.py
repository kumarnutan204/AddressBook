class Contact:
    def __init__(self,first,last,address, city,state,zip,phone,email):
        self.Contact_dict={'firstname':first,'lastname':last,'address':address,'city':city,'state':state,'zip':zip,'phone':phone,'email':email}
    
    def show_contact(self):
        print(self.Contact_dict)
        
    def edit_contact(self):
        key_val=input("Enter the key you want to change :  ")
        if key_val in self.Contact_dict:
            new_val=input("Enter the value you want to change to :")
            self.Contact_dict[key_val]=new_val
            print("your details are edited")
            # print(self.Contact_dict.show_contact())
            



class AddressBook:
    def __init__(self, name):
        self.name = name
        self.addressbookDict={}
    
    def get_Contact(self, name): 
        return self.addressbookDict.get(name)
        
    def add_contact(self,Contact_obj):
        fullname=Contact_obj.Contact_dict['firstname']+ " "+ Contact_obj.Contact_dict['lastname']
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
            

class MultipleAddressBook:
    def __init__(self):
        self.multiple_addressbook_dict={}  
    
    
    def show_addressbook_system(self):
        print("Below is the Address Book: ")
        print(self.multiple_addressbook_dict)
        
    def get_book(self, name): 
        return self.multiple_addressbook_dict.get(name)
    
    def add_addressbook_to_sys(self,Addressbook_obj):
        self.multiple_addressbook_dict.update({Addressbook_obj.name:Addressbook_obj})
        # print("Addressbook added in AddressBook System")
        
        
        
        
        
          
    
if __name__=='__main__':
    print("Welcome to the Address Book management!!!")
    addressbook_sys=MultipleAddressBook()
    
    while True:
        print("press 1 to add a book to Addressbook: ")
        print("press 2 to find a book in Addressbook to edit/update:  ")
        print("Enter 'ex' to exit the program : ")
        choice = (input('Enter a choice: '))
        
        if choice == '1':
            book_name = input('Enter book name:')
            book = addressbook_sys.get_book(book_name)
            if not book:
                book = AddressBook(book_name)
            
            first=input("Enter the first name: ")
            last=input("Enter the last name: ")
            address=input("Enter the address: ")
            city=input("Enter the city name: ")
            state=input("Enter the state name: ")
            zip=input("Enter the zip : ")
            phone=input("Enter the phone number: ")
            email=input("Enter the email: ")
            contact=Contact(first,last,address,city,state,zip,phone,email) 
            # contact = Contact('Nutan', 'Kumar', 'Hostel', 'Chennai', 'Tamil Nadu', '456635', '234567898', 'nk676@gmail.com')
            book.add_contact(contact)
            addressbook_sys.add_addressbook_to_sys(book)
            # book_choice=int(input("Enter a choice to continue"))
            print(addressbook_sys.multiple_addressbook_dict)
        if choice == '2':
            book_name = input('Enter book name:')
            book = addressbook_sys.get_book(book_name)
            print(book.show_addressbook())
            
            book_loop='yes'
            while(book_loop!='no'):
                
                book_loop=input("Press yes to work on current book:  ")
                if book_loop =='yes':
                    print("Here is the current book : " )
                    print(book.show_addressbook())
                    print("1. add another contact")
                    print("2. edit a contact")
                    print("3. delete a contact")
                    print("Enter 'ex' to exit the program ")
                    
                    choice=input("Enter choice: ")
                    
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
                            book.add_contact(cont2)
                            book.show_addressbook()
                        endit='no'
                    if choice=='2':
                        name=input("Enter the full name of the person you want to edit details of : ")
                        if name in book.addressbookDict.keys():
                            book.edit_addressbook(name)
                    if choice=='3':
                        name=input("Enter the full name of the person you want to delete details of : ")
                        if name in book.addressbookDict.keys():
                            book.delete_cont_from_addressbook(name)
                    
                    if choice=='ex':
                        exit()
                
                else:
                    break
        
        if choice=='ex':
            exit()            
                    
        
         