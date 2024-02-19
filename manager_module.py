from contact import Contact
from contact_types import contact_type,list_contacts_type
def input_add_contact() -> contact_type :
    name = input("insert the contact name ->")
    email = input ("insert the contact email ->")
    phone = input ("insert the contact phone ->")
    return {"email":email,"name":name,"phone":phone}

def input_get_contact_name(action:str):
    contact_name=input(f"Type the name of the contact that should be {action} ->")
    return contact_name

def add_contact(contacts : list_contacts_type):
   contact_values = input_add_contact()
   contact_object = Contact(name=contact_values["name"],email=contact_values["email"],phone=contact_values["phone"])
   contacts.append(contact_object)
   return True
   
def get_contacts(contacts: list_contacts_type):
    if(len(contacts)==0):
        print("No contacts!!")
    for index,contact in enumerate(contacts,start=1):
        print(f"{index}. name:{contact.name} - email:{contact.email} - is_favorite:{contact.is_favorite} - phone:{contact.phone} \n")
    return True

def get_favorite_contacts(contacts: list_contacts_type):
    if(len(contacts)==0):
        print("No favorite contacts!!")
    for index,contact in enumerate(contacts,start=1):
        if(contact.is_favorite):
            print(f"{index}. {contact}")
    return True

def delete_contact(contacts: list_contacts_type):
    contact_name = input_get_contact_name(action="deleted")
    contact = find_contact_by_name(contacts=contacts,param_value=contact_name)
    contacts.remove(contact)
    print(f"The {contact_name} was successfully deleted!")
    
def find_contact_by_name(contacts: list_contacts_type,param_value):
    for contact in contacts:
        if(contact.name == param_value):
            return contact
     
def edit_contact(contacts: list_contacts_type):
    contact_name = input_get_contact_name(action="edited")
    contact = find_contact_by_name(contacts=contacts, param_value=contact_name)

    keys_copy = list(contact.__dict__.keys())

    for key in keys_copy:
        new_value = input(f"Insert the new value of contact {key}: ")
        if(new_value != "") :
            setattr(contact, key, new_value)
            if(key == "is_favorite") :
                new_value = bool(new_value)

    return True

def mark_contact_as_favorite(contacts: list_contacts_type):
    contact_name = input_get_contact_name("favorited")
    contact = find_contact_by_name(contacts=contacts,param_value=contact_name)
    is_favorite = True
    contact.is_favorite = is_favorite
    return True

def select_actions(contacts: list_contacts_type,action:int):
    valid_action =True
    match action:
        case 1 :
            add_contact(contacts=contacts)
        case 2 :
            get_contacts(contacts=contacts)
        case 3:
            edit_contact(contacts=contacts)
        case 4:
            mark_contact_as_favorite(contacts=contacts)
        case 5:
            get_favorite_contacts(contacts=contacts)
        case 6:
            delete_contact(contacts=contacts)
        case 7:
            print("Thanks for usage!")
            valid_action = False
    return valid_action
            