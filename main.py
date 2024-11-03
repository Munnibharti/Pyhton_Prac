# main.py
from crud_operation import add_contact,get_contacts

# Sample code to interact with the CRUD functions
if __name__ == "__main__":
    # Add a new contact
    add_contact("John Doe", "1234567890", "john@example.com")
    
    # #Fetch and display all contacts
    contacts = get_contacts()
    for contact in contacts:
        print(contact)
    
    # # # Update a contact
    # update_contact(1, "John Smith", "123-456-7890", "johnsmith@example.com")
    
    # # # Delete a contact
    # delete_contact(1)
