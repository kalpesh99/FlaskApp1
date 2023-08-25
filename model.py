# create peewee sql models for customers, orders, products


from peewee import Model, SqliteDatabase, ForeignKeyField, CharField, FloatField, IntegerField

# Define a SQLite database
db = SqliteDatabase('ecommerce.db')

# Define the Customer model
class Customer(Model):
    name = CharField()
    email = CharField()

    class Meta:
        database = db

# Define the Product model
class Product(Model):
    name = CharField()
    price = FloatField()

    class Meta:
        database = db

# Define the Order model
class Order(Model):
    customer = ForeignKeyField(Customer, backref='orders')
    product = ForeignKeyField(Product)
    quantity = IntegerField()

    class Meta:
        database = db

# # Connect to the database and create tables
# db.connect()
# db.create_tables([Customer, Product, Order])

# # Create new customer and product objects
# customer = Customer.create(name='John Doe', email='john@example.com')
# product1 = Product.create(name='Widget', price=19.99)
# product2 = Product.create(name='Gadget', price=39.99)

# # Create new order objects and insert into the database
# order1 = Order.create(customer=customer, product=product1, quantity=2)
# order2 = Order.create(customer=customer, product=product2, quantity=1)

# # Query and retrieve customers
# customers = Customer.select()
# for customer in customers:
#     print(f"Customer ID: {customer.id}, Name: {customer.name}, Email: {customer.email}")

# # Query and retrieve orders along with associated customer and product information
# orders = Order.select().join(Customer).join(Product).where(Customer.name == 'John Doe')
# for order in orders:
#     print(f"Order ID: {order.id}, Customer: {order.customer.name}, Product: {order.product.name}, Price: {order.product.price}, Quantity: {order.quantity}")

# Close the database connection
#db.close()
