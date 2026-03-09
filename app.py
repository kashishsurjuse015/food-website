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

# --- ROUTES START ---


@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/menu')
def menu():
    food_items = [
        {"_id": "1", "name": "Special Chicken Biryani", "price": 250, "description": "Slow-cooked aromatic rice with tender chicken spices.", "image_url": "/static/01.jpg", "stripe_url": "#"},
        {"_id": "2", "name": "Veg Hyderabadi Biryani", "price": 180, "description": "Fresh vegetables mixed with basmati rice and saffron.", "image_url": "/static/06.jpg", "stripe_url": "#"},
        {"_id": "3", "name": "Paneer Tikka Biryani", "price": 220, "description": "Grilled paneer cubes layered with spicy biryani rice.", "image_url": "/static/02.jpg", "stripe_url": "#"},
        {"_id": "4", "name": "Mutton Dum Biryani", "price": 350, "description": "Rich flavors of mutton with long grain basmati rice.", "image_url": "/static/03.jpg", "stripe_url": "#"},
        {"_id": "5", "name": "Chicken Lollipop", "price": 200, "description": "Deep fried chicken appetizers with sauce.", "image_url": "/static/04.jpg", "stripe_url": "#"},
        {"_id": "9", "name": "Dal Tadka", "price": 140, "description": "Yellow lentils tempered with ghee.", "image_url": "/static/09.jpg", "stripe_url": "#"},
        {"_id": "10", "name": "Gulab Jamun", "price": 60, "description": "Sweet dessert balls in sugar syrup.", "image_url": "/static/10.jpg", "stripe_url": "#"},
        # --- Chinese Dishes Added ---
        {"_id": "11", "name": "Veg Manchurian", "price": 150, "description": "Spicy vegetable balls in Chinese gravy.", "image_url": "/static/11.jpg", "stripe_url": "#"},
        {"_id": "12", "name": "Veg Hakka Noodles", "price": 120, "description": "Stir-fried noodles with crunchy vegetables.", "image_url": "/static/12.jpg", "stripe_url": "#"},
        {"_id": "13", "name": "Paneer Chilli", "price": 180, "description": "Crispy paneer tossed in soya and chilli sauce.", "image_url": "/static/13.jpg", "stripe_url": "#"}
    ]
    return render_template('menu.html', food_items=food_items)

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_name = request.form.get('username')
        pass_word = request.form.get('password')
        user = User.query.filter_by(username=user_name).first()
        if user and user.password == pass_word:
            session['user'] = user_name
            flash('Login Successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid Credentials', 'danger')
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

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        flash(f"Thank you {name}, feedback received!", "success")
        return redirect(url_for('contact'))
    return render_template('contact.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
