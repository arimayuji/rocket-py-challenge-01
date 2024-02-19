from contact import Contact
from typing import List,TypedDict

list_contacts_type =List[Contact]
contact_type = TypedDict("Contact",{"name":str,"phone":str,"email":str})