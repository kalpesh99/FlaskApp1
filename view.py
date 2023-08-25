# Create flask app with three routes
# 1. /hello
# 2. /hello/<name>
# 3. /hello/<name>/<int:age>
# 4. /hello/<name>/<int:age>/<float:weight>

import sqlite3
import os
import sys
from model import Customer, Product, Order, db


from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/hello")
def hello1():
    return "Hello World!"

@app.route("/hello/<name>")
def hello2(name):
    return "Hello %s!" % name

@app.route("/hello/<name>/<int:age>") 
def hello3(name, age):
    return "Hello %s! You are %d years old." % (name, age)

@app.route("/hello/<name>/<int:age>/<float:weight>")
def hello4(name, age, weight):
    return "Hello %s! You are %d years old and weigh %f." % (name, age, weight)


# define a route to display all customers
@app.route("/customers")
def customers():
    # connect to the database
    conn = sqlite3.connect('ecommerce.db')
    # create a cursor
    cur = conn.cursor()
    # execute a query
    cur.execute("SELECT * FROM Customer")
    # fetch all results
    results = cur.fetchall()
    # close the connection
    conn.close()
    # return the results
    return str(results)



@app.route("/customers2")
def customers2():
    # connect to the database
    conn = sqlite3.connect('ecommerce.db')
    # create a cursor
    cur = conn.cursor()
    # execute a query
    cur.execute("SELECT * FROM Customer")
    # fetch all results
    results = cur.fetchall()
    # close the connection
    conn.close()
    # return the results

        # Query and retrieve customers
    customers = Customer.select()
    for customer in customers:
        print(f"Customer ID: {customer.id}, Name: {customer.name}, Email: {customer.email}")



    return render_template('customers.html', customers=customers)


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
    # Connect to the database and create tables
    db.connect()
    #db.create_tables([Customer, Product, Order])

    # Create new customer and product objects
    #customer = Customer.create(name='John Doe', email='john@example.com')
    #product1 = Product.create(name='Widget', price=19.99)
    #product2 = Product.create(name='Gadget', price=39.99)

    # Create new order objects and insert into the database
    #order1 = Order.create(customer=customer, product=product1, quantity=2)
    #order2 = Order.create(customer=customer, product=product2, quantity=1)

        

# End of file

