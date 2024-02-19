from manager_module import select_actions
from contact import Contact

print("""
      
      Select your action : <ACTION> <PARAMETER>
            1. ADD CONTACT : { name,phone,email }
            2. VIEW CONTACTS
            3. EDIT CONTACT : contact name
            4. MARK AS FAVORITE : contact name
            5. VIEW FAVORITE CONTACTS
            6. DELETE CONTACT : contact name
            7. OUT 
      
      """)
contacts : list[Contact] = []

while True:
    action = int(input("type the action number! ->"))
    
    valid_action=select_actions(contacts=contacts,action=action)
    if(not valid_action):
          break