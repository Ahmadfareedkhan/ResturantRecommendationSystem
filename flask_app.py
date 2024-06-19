from flask import Flask, render_template, request
import pandas as pd
import os

TEMPLATE_DIR = os.path.abspath(r"C:\Users\ahmad\.vscode\ResturantRecommendationSystem\templates")
STATIC_DIR = os.path.abspath(r"C:\Users\ahmad\.vscode\ResturantRecommendationSystem\static")

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

# Load the restaurant data from Excel
restaurant_data = pd.read_excel(r'C:\Users\ahmad\.vscode\ResturantRecommendationSystem\Resturant_data_1000.xlsx')  # Update the path to your Excel file

@app.route('/', methods=['GET', 'POST'])
def index():
    cities = restaurant_data['City'].unique()
    cuisines = restaurant_data['Cuisine'].unique()
    locations = restaurant_data['Location'].unique()
    filtered_restaurants = None
    recommendations = None

    if request.method == 'POST':
        city = request.form.get('city')
        cuisine_type = request.form.get('cuisine_type')
        location = request.form.get('location')
        min_rating = request.form.get('min_rating')

        filtered_restaurants = restaurant_data[(restaurant_data['City'] == city) &
                                               (restaurant_data['Cuisine'] == cuisine_type) &
                                               (restaurant_data['Location'] == location)]

        if min_rating:
            min_rating = float(min_rating)
            if 'Rating' in filtered_restaurants.columns:
                filtered_restaurants = filtered_restaurants[filtered_restaurants['Rating'].astype(float) >= min_rating]

        if not filtered_restaurants.empty:
            recommended_restaurant = filtered_restaurants.iloc[0]['Restaurant Name']
            recommendations = get_recommendations(recommended_restaurant)

    return render_template('index.html', 
                           cities=cities, 
                           cuisines=cuisines, 
                           locations=locations, 
                           filtered_restaurants=filtered_restaurants, 
                           recommendations=recommendations)

def get_recommendations(restaurant_name):
    restaurant_index = restaurant_data[restaurant_data['Restaurant Name'] == restaurant_name].index[0]
    recommendations = restaurant_data.loc[restaurant_index + 1:restaurant_index + 6, ['Restaurant Name', 'Cuisine', 'Location', 'Rating']]
    return recommendations

if __name__ == '__main__':
    app.run(debug=True)
