from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from datetime import datetime

app = Flask(__name__)

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rameats.db'
db = SQLAlchemy(app)

"""
Defines an SQLAlchemy model class which will help our python backend interact with db. This class definition creates a table named 'User' with columns for storing the user data and the colums will correspond to attributes of user objects in the app.
"""
class User(db.Model):
    # Declares id column in the database (db)
    # id declaration contains the primary key of the User table; uniquely identifies each row
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(10), nullable=False)
    height = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    activity_level = db.Column(db.String(20), nullable=False)
    fitness_goal = db.Column(db.String(20), nullable=False)

# Create database tables
db.create_all()

# Endpoint for user registration
@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    gender = data['gender']
    height = data['height']
    height = (height * 0.4253592) # Converts the units from customary to metric for calculations
    weight = data['weight']
    weight = (weight * 2.54) # Converts from inches to cm. for calculations
    age = data['age']
    activity_level = data['activity_level']
    fitness_goal = data['fitness_goal']

    try:
        new_user = User(gender=gender, height=height, weight=weight, age=age,
                        activity_level=activity_level, fitness_goal=fitness_goal)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'User already exists!'}), 400

# Endpoint for getting meal recommendations
@app.route('/meal_recommendations', methods=['POST'])
def get_meal_recommendations():
    data = request.get_json()
    # Fetch user data from the database based on user_id or some form of authentication
    # Calculate meal recommendations based on user data and Lenoir/Chase dining hall menus
    # Return meal recommendations as JSON response
    recommendations = calculate_meal_recommendations(data)
    return jsonify({'recommendations': recommendations})

# Function for calorie calculation and meal recommendation
def calculate_calories_func(height, weight, age, activity_level):
    # Your calorie calculation logic goes here
    
    return 2000

# Function for calculating meal recommendations
def calculate_meal_recommendations(daily_calories):
    # Meal recommendation algorithm goes here
    # This is just a placeholder
    return ["Salad", "Grilled Chicken", "Fruits"]

if __name__ == '__main__':
    app.run(debug=True)