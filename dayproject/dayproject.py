#-	SQL Table within your database that contains order_id, 
# customer_name, drink, size, extras, price,
import sqlite3 as sql

conn = sql.connect("coffeeorder-db")

cursor = conn.cursor()

def creatingTable():
    sql_file = open("dayproject.sql")
    sql_string = sql_file.read()
    cursor.executescript(sql_string)
#creatingTable()
def insertOrder():
    coffee_name = input("Please enter coffee name ")
    coffee_query = f"INSERT INTO orders (drink) VALUES ('{coffee_name}');"
    cursor.execute(coffee_query)
    return True

def readOrder(query):
    return cursor.execute(query).fetchall()

def readAllDrinks():
    query = "SELECT * FROM orders"
    return readOrder(query)

# Changing / manipulating data
def dataQuery(query):
    cursor.execute(query)
    return True

def deleteOrder():
    id = input("what is the ID of the order you want to delete?:")
    query = f"DELETE FROM orders where order_id = {id}"
    return dataQuery(query)

def updateOrder():
    id = input("what is the order you would like to update:")
    drink= input("what would you like the new drink to be")
    query = f"UPDATE orders SET drink = '{drink}' WHERE order_id = {id}"
    return dataQuery(query)


def runApp():

    print("""
    Welcome to QA Coffee shop! 
    Please select an option from below: 
    1. add an order
    2. read an orders
    3. update an order
    4. delete an order
    """
    )
    running = True

    # Does a thing while a condition is true
    while running:
        choice = int(input("Please select a choice using a number: "))
        if choice == 1:
            insertOrder()
        elif choice == 2:
            print(readAllDrinks())
        elif choice == 3:
            updateOrder()
        elif choice == 4:
            deleteOrder()
        else: 
            print("Incorrect choice.. try again..")

        end_choice = input("Do you want to query more data Y / N: ")
        if end_choice.upper() == "N":
            running = False

runApp()

conn.commit()