from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__, template_folder='templates')
app.secret_key = 'your_secret_key'

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///food_website.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# 1. HOME ROUTE
@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

# 2. MENU ROUTE (Yahan aapka menu load hoga)
@app.route('/menu')
def menu():
    # Ye sample data hai jo menu.html ke {% for %} loop mein jayega
    food_items = [
        {
            "_id": "1", 
            "name": "Special Chicken Biryani", 
            "price": 250, 
            "description": "Slow-cooked aromatic rice with tender chicken spices.", 
            "image_url": "/static/01.jpg",
            "stripe_url": "#"
        },
        {
            "_id": "2", 
            "name": "Veg Hyderabadi Biryani", 
            "price": 180, 
            "description": "Fresh vegetables mixed with basmati rice and saffron.", 
            "image_url": "/static/06.jpg",
            "stripe_url": "#"
        },
        {
            "_id": "3", 
            "name": "Paneer Tikka Biryani", 
            "price": 220, 
            "description": "Grilled paneer cubes layered with spicy biryani rice.", 
            "image_url": "/static/02.jpg",
            "stripe_url": "#"
        }
    ]
    return render_template('menu.html', food_items=food_items)

# 3. OTHER ROUTES
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/cart')
def cart():
    return render_template('cart.html') # Agar cart page hai toh

if __name__ == '__main__':
    with app.app_context():
        db.create_all() # Database table banane ke liye
    app.run(debug=True)
  
