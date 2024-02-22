import json


class Contact:
    def __init__(self,firstname,lastname,address, city,state,zip,phone,email):
        self.contact_dict={'firstname':firstname,'lastname':lastname,'address':address,'city':city,'state':state,'zip':zip,'phone':phone,'email':email}
    
    def show_contact(self):
        print(self.contact_dict)
        
    def edit_contact(self):
        key_val=input("Enter the key you want to change :  ")
        if key_val in self.contact_dict:
            new_val=input("Enter the value you want to change to :")
            self.contact_dict[key_val]=new_val
            print("your details are edited")
            # print(self.contact_dict.show_contact())
            



class AddressBook:
    def __init__(self, b_name):
        self.name = b_name
        self.addressbook_dict={}
    
    def get_Contact(self, name): 
        return self.addressbook_dict.get(name)
        
    def add_contact(self,Contact_obj):
        fullname=Contact_obj.contact_dict['firstname']+ " "+ Contact_obj.contact_dict['lastname']
        self.addressbook_dict.update({fullname:Contact_obj})
        print("Contact added in Address book")
        
    def display_addressbook(self):
        print("Below is the Address Book: ")
        return self.addressbook_dict
        
    def edit_addressbook(self,name):
        if name in self.addressbook_dict.keys():
            print(self.addressbook_dict[name].show_contact())
            self.addressbook_dict[name].edit_contact(name)
            print(self.addressbook_dict[name].show_contact())
            
    def delete_cont_from_addressbook(self,name):
        if name in self.addressbook_dict.keys():
            print("The below contact will be deleted from the Addressbook: ")
            print(self.addressbook_dict[name].show_contact())
            del self.addressbook_dict[name]
            print("Your contact has been deleted: ")
            print(self.addressbook_dict)
            

class MultipleAddressBook:
    def __init__(self):
        self.multiple_addressbook_dict={}  
    
    
    def show_addressbook_system(self):
        print("Below is the Address Book: ")
        print(self.multiple_addressbook_dict)
        
    def get_book(self, name): 
        return self.multiple_addressbook_dict.get(name)
    
    def delete_book(self,name):
        del self.multiple_addressbook_dict[name]
        print(self.multiple_addressbook_dict)
    
    def add_addressbook_to_sys(self,Addressbook_obj):
        self.multiple_addressbook_dict.update({Addressbook_obj.name:Addressbook_obj})
        # print("Addressbook added in AddressBook System")
        
    def add_to_json(self):
        for book in self.multiple_addressbook_dict.values():
            json_data = {book.name : {}}
            cont_dict = json_data[book.name]
            for i in book.addressbook_dict.values():
                print(i.contact_dict)
                print("Next item\n")
                cont_dict.update({i.contact_dict['firstname']+ " "+ i.contact_dict['lastname']:i.contact_dict})
        
        with open('contacts.json', 'w') as file:
                data = (json_data)
                json.dump(data, file, indent=4)
                    
        
        
        
          
    
if __name__=='__main__':
    print("Welcome to the Address Book management!!!")
    addressbook_sys=MultipleAddressBook()
    print(vars(addressbook_sys))
    while True:
        print("press 1 to add a new book to Addressbook: ")
        print("press 2 to find a book in Addressbook to edit/update:  ")
        print("press 3 to delete a book: ")
        print("press 4 to show all the books in the system: ")
        print("press 5 to create a json of the addressbook system :")
        
        
        print("Enter 'ex' to exit the program : ")
        choice = (input('Enter a choice: '))
        
        if choice == '1':
            book_name = input('Enter book name:')
            book = addressbook_sys.get_book(book_name)
            if not book:
                book = AddressBook(book_name)
            
            # first=input("Enter the first name: ")
            # last=input("Enter the last name: ")
            # address=input("Enter the address: ")
            # city=input("Enter the city name: ")
            # state=input("Enter the state name: ")
            # zip=input("Enter the zip : ")
            # phone=input("Enter the phone number: ")
            # email=input("Enter the email: ")
            # contact=Contact(first,last,address,city,state,zip,phone,email) 
            contact1 = Contact('Nutan', 'Kumar', 'Hostel', 'Chennai', 'Tamil Nadu', '456635', '234567898', 'nk676@gmail.com')
            contact2= Contact('Naveen', 'Jack', 'Abodde', 'Chennai', 'Tamil Nadu', '456423', '242342898', 'nj676@gmail.com')
            book.add_contact(contact1)
            book.add_contact(contact2)
            addressbook_sys.add_addressbook_to_sys(book)
            # book_choice=int(input("Enter a choice to continue"))
            print(addressbook_sys.multiple_addressbook_dict)
        if choice == '2':
            book_name = input('Enter book name:')
            book = addressbook_sys.get_book(book_name)
            print(book.display_addressbook())
            
            book_loop='yes'
            while(book_loop!='no'):
                
                book_loop=input("Press yes to work on current book:  ")
                if book_loop =='yes':
                    print("Here is the current book : " )
                    print(book.display_addressbook())
                    print("1. add another contact")
                    print("2. edit a contact")
                    print("3. delete a contact")
                    print("4. show all contacts in the current book")
                    print("5. to return back to editing books")
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
                            print(book.display_addressbook())
                        endit='no'
                    if choice=='2':
                        name=input("Enter the full name of the person you want to edit details of : ")
                        if name in book.addressbook_dict.keys():
                            book.edit_addressbook(name)
                    if choice=='3':
                        name=input("Enter the full name of the person you want to delete details of : ")
                        if name in book.addressbook_dict.keys():
                            book.delete_cont_from_addressbook(name)
                    
                    if choice=='4':
                        print(book.display_addressbook())
                    
                    if choice=='5':
                        break
                    
                    if choice=='ex':
                        exit()
                
                else:
                    break
        
        if choice=='3':
            book_name = input('Enter book name:')
            book = addressbook_sys.get_book(book_name)
            print(book.display_addressbook())
            addressbook_sys.delete_book(book_name)
            
            
        if choice=='4':
            addressbook_sys.show_addressbook_system()
            
        if choice=='5':
            addressbook_sys.add_to_json()
            
        # if choice=='5':
            # main_dict={}
            # for item in addressbook_sys.multiple_addressbook_dict.values():
                
            #         for i in item.addressbook_dict.values():
            #             print(item.addressbook_dict)
            #             print(i.contact_dict)
            #             print("Next item\n")
            #             main_dict.update({i.contact_dict['firstname']+ " "+ i.contact_dict['lastname']:i.contact_dict})
                    
                    
            #         # # key = addressbook_sys.multiple_addressbook_dict.keys()
            #         # with open('contacts.json','r') as f:
            #         #     data= json.load(f)
            #         #     print(data)
            #         #     # main_dict.update({key:data})
                        
                        
                
            #     # for i in item.addressbook_dict.values():
            #     #     print(i)
            # # print(main_dict)
            # with open('contacts.json', 'w') as file:
            #     data = (main_dict)
            #     json.dump(data, file, indent=4)
        if choice=='ex':
            exit()            
                    
        
         