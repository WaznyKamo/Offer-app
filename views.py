from flask import render_template, request, flash, redirect
from Offer_app import app, db
from db_models import Category, Product
from forms import Login, UserForm
from db_models import User


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/categories/', defaults={'category_id': None})
@app.route('/categories/<int:category_id>')
def show_categories(category_id):
    if category_id is None:
        categories = Category.query.all()
        return render_template('categories.html', categories=categories)
    else:
        products_from_category = Product.query.filter_by(category_id=category_id)
        return render_template('products_from_category.html', products=products_from_category)


@app.route('/products')
def show_products():
    products = Product.query.all()
    return render_template('products_from_category.html', products=products)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = UserForm()

    if request.method == 'POST':
        if form.validate():
            validated_data = form.data.copy()
            validated_data.pop('csrf_token')

            if User.query.filter_by(email=validated_data['email']).first is not None:
                flash('Email already taken')
                return render_template('register.html', form=UserForm())

            new_client = User(**validated_data)
            db.session.add(new_client)
            db.session.commit()
            flash('User created')
            return redirect('/login')
    return render_template('register.html', form=UserForm())


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()

    if request.method == 'POST' and form.validate():
        validated_data = form.data.copy()
        validated_data.pop('csrf_token')



