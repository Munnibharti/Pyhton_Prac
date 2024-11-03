import pyodbc

# def get_connection():
#     connection = pyodbc.connect(
#         'DRIVER={SQL Server};'
#         'SERVER=localhost;'       # Replace with your server name
#         'DATABASE=ContactDB;'     # Replace with your database name
#         'Trusted_Connection=yes;' # Use SQL Server Authentication if needed
#     )
#     return connection
# Define the connection string
# connection_string = (
#     'DRIVER={SQL Server};'
#     'SERVER=DESKTOP-S0NDMQL\SQLEXPRESS02'          # Using localhost as the server
#     'DATABASE=ContactDB;'       # Replace with your actual database name
#     'Trusted_Connection=yes;'    # For Windows Authentication
# )

# # Establish the connection
# try:
#     conn = pyodbc.connect(connection_string)
#     print("Connection successful!")
# except Exception as e:
#     print(f"Error: {e}")

# print("Print print")


try:
    # Set up the connection string
    def get_connection():


        conn = pyodbc.connect(
            "Driver={ODBC Driver 17 for SQL Server};"
            "Server=DESKTOP-S0NDMQL\SQLEXPRESS02;"
            "Database=ContactDB;"
            "Trusted_Connection=yes;"
        # "UID=YourUsername;"
        # "PWD=YourPassword;"
        )
        return conn
    #print("Connection successful!")
   

    # Test query
    #cursor = conn.cursor()

#     cursor.execute("""
#     CREATE TABLE USERs (
#         USER_ID INT PRIMARY KEY IDENTITY(1,1),
#         Name VARCHAR(50),
#         Email VARCHAR(50),
#         Mobile_No VARCHAR(10)
#     );
# """)

#     conn.commit()
    #cursor.execute("SELECT * FROM USER")

    # cursor.execute("SELECT 1")
    # result = cursor.fetchone()
    # print("Test query result:", result[0])

    # Close the connection
    conn.close()

except Exception as e:
    print("Error:", e)
