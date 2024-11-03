# crud_operations.py
from db_config import get_connection

def add_contact(name, phone, email):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO USERs (Name, Email, Mobile_No) VALUES (?, ?, ?)"
    cursor.execute(query, (name, email, phone))
    conn.commit()
    conn.close()
    print("Contact added successfully.")

def get_contacts():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM USERs"
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# def update_contact(contact_id, name, phone, email):
    # conn = get_connection()
    # cursor = conn.cursor()
    # query = "UPDATE Contacts SET Name = ?, Phone = ?, Email = ? WHERE ID = ?"
    # cursor.execute(query, (name, phone, email, contact_id))
    # conn.commit()
    # conn.close()
    # print("Contact updated successfully.")

# def delete_contact(contact_id):
    # conn = get_connection()
    # cursor = conn.cursor()
    # query = "DELETE FROM Contacts WHERE ID = ?"
    # cursor.execute(query, (contact_id,))
    # conn.commit()
    # conn.close()
    # print("Contact deleted successfully.")
