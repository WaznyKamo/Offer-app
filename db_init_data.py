from __init__ import db
from db_models import Category, Product

db.session.add(Category(name='Food'))
db.session.add(Category(name='Cars'))
db.session.add(Category(name='Clothes'))
db.session.add(Category(name='Household items'))
db.session.commit()

db.session.add(Product(name='Apple', price=1, category_id=1))
db.session.add(Product(name='Banana', price=1.5, category_id=1))
db.session.add(Product(name='Pie', price=10, category_id=1))
db.session.add(Product(name='Steak', price=69, category_id=1))
db.session.add(Product(name='Ford Focus', price=10000, category_id=2))
db.session.add(Product(name='Audi Q7', price=300000, category_id=2))
db.session.add(Product(name='BMW M3', price=400000, category_id=2))
db.session.add(Product(name='Toyota Yaris', price=2000, category_id=2))
db.session.add(Product(name='Jeans', price=50, category_id=3))
db.session.add(Product(name='Jacket', price=250, category_id=3))
db.session.add(Product(name='Jordans', price=220, category_id=3))
db.session.add(Product(name='Broom', price=10, category_id=4))
db.session.add(Product(name='Iron', price=50, category_id=4))
db.session.add(Product(name='Dishwasher', price=500, category_id=4))

db.session.commit()
