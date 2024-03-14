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
    

# Function for calculating daily calories that takes in dict of user data
def calc_daily_cal(user_data) -> int:
    bmr: int = 0 # basal metabolic rate variable
    result: int = 0
    # Calculates the BMR for Male and Female
    if user_data['gender'] == ("Male"):
        bmr = int((10 * user_data['weight']) + (6.25 * user_data['height']) - (5 * user_data['age']) + 5)
    else:
        bmr = int((10 * user_data['weight']) + (6.25 * user_data['height']) - (5 * user_data['age']) - 161)
    # Finds the daily calories needed for maintainance at a particular activity level
    result = int(bmr * user_data['activity_level'])

    if user_data['fitness_goal'] == ("Build Muscle"):
        result = int(result * 1.1)
        return result
    elif user_data['fitness_goal'] == ("Lose Weight"):
        result = int(result * .9)
        return result
    else:
        return result


# Placeholder function for calculating meal recommendations based on meal type
def calculate_meal_recommendations(user_data, meal_type):
    # Your meal recommendation logic goes here
    # Must first get the menu for the meal type from the database
    menu = {} # Placeholder for menu from database

    # Defines the certain restrictions for macros
    meal_cal: int = 0
    protein_goal = 0.24
    carbs_goal = 0.53
    fats_goal = 0.23

    # Calculates the amount of calories for the meal
    if meal_type == 'breakfast':
        meal_cal = calc_daily_cal(user_data) * .22
    elif meal_type == 'lunch':
        meal_cal = calc_daily_cal(user_data) * .31
    elif meal_type == 'dinner':
        meal_cal = calc_daily_cal(user_data) * .35
    
    selected_items = []
    total_calories = 0
    total_protein = 0
    total_carbs = 0
    total_fats = 0

    # Sort menu items by healthiness rating (higher rating means healthier)
    sorted_menu = sorted(menu.items(), key=lambda x: x[1]["healthiness"], reverse=True)

    # Iterate through sorted menu items and select items until total calories reach the limit
    for item, info in sorted_menu:
        if total_calories + info["calories"] <= meal_cal:
            # Check if adding this item exceeds macronutrient limits
            if ((total_protein + info["protein"]) * 4) / total_calories <= protein_goal \
                and ((total_carbs + info["carbs"]) * 4) / total_calories <= carbs_goal \
                and ((total_fats + info["fats"]) * 9) / total_calories <= fats_goal:
                selected_items.append(item)
                total_calories += info["calories"]
                total_protein += info["protein"]
                total_carbs += info["carbs"]
                total_fats += info["fats"]

    return selected_items, total_calories, total_protein, total_carbs, total_fats


# Endpoint for getting meal recommendations
@app.route('/meal_recommendations', methods=['POST'])
def get_meal_recommendations():
    data = request.json
    user_id = data['user_id']  # Placeholder for retrieving the specific user's data
    # Fetch user data from Supabase based on user_id or some form of authentication
    user_data = {}  # Placeholder for user's data
    recommendations = {
        'breakfast': calculate_meal_recommendations(user_data, 'breakfast'),
        'lunch': calculate_meal_recommendations(user_data, 'lunch'),
        'dinner': calculate_meal_recommendations(user_data, 'dinner'),
        'snacks': f"{(calc_daily_cal() * .12)} calories" # Come back and add the arguments
    }
    return jsonify(recommendations)


if __name__ == "__main__":
    app.run(debug = True)