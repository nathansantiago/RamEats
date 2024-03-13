from flask import Flask, jsonify, request
from supabase import create_client

app = Flask(__name__)

# Initialize Supabase client
supabase_url = "SUPABASE_URL"
supabase_key = "SUPABASE_API_KEY"
supabase = create_client(supabase_url, supabase_key)


# Endpoint for user registration
@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    gender = data['gender']
    height = data['height']
    height = (height * 2.54) # Converts from in to cm for calculations
    weight = data['weight']
    weight = (weight * 0.453592) # Converts from lb to kgs for calculations
    age = data['age']
    activity_level = data['activity_level']
    fitness_goal = data['fitness_goal']

    # Insert user data into 'users' table in Supabase
    response = supabase.table('users').insert({
        'gender': gender,
        'height': height,
        'weight': weight,
        'age': age,
        'activity_level': activity_level,
        'fitness_goal': fitness_goal
    }).execute()

    if response['status'] == 201:
        return jsonify({'message': 'User registered successfully!'}), 201
    else:
        return jsonify({'error': 'Failed to register user!'}), 500
    

# Function for calculating daily calories
def calc_daily_cal(gender, height, weight, age, activity_level, fitness_goal) -> int:
    bmr: int = 0 # basal metabolic rate
    result: int = 0
    if gender == ("Male"):
        bmr = int((10 * weight) + (6.25 * height) - (5 * age) + 5)
    else:
        bmr = int((10 * weight) + (6.25 * height) - (5 * age) - 161)
    
    result = int(bmr * activity_level)

    if fitness_goal == ("Build Muscle"):
        result = int(result * 1.09)
        return result
    elif fitness_goal == ("Lose Weight"):
        result = int(result * .91)
        return result
    else:
        return result


# Function for calculating meal recommendations
def calculate_meal_recommendations(user_data):
    # Meal recommendation algorithm goes here
    # This is just a placeholder
    return ["Salad", "Grilled Chicken", "Fruits"]


# Endpoint for getting meal recommendations
@app.route('/meal_recommendations', methods = ['POST'])
def get_meal_recommendations():
    data = request.json
    # Fetch user data from Supabase based on some form of authentication
    # Calculate meal recommendations based on user data and dining hall menu
    # Return meal recommendations as JSON response
    recommendations = calculate_meal_recommendations(data)
    return jsonify({'recommendations': recommendations})


if __name__ == "__main__":
    app.run(debug = True)