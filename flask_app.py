from flask import Flask, render_template, jsonify
import os

TEMPLATE_DIR = os.path.abspath(
    r"C:\Users\ahmad\.vscode\ResturantRecommendationSystem\templates"
)
STATIC_DIR = os.path.abspath(
    r"C:\Users\ahmad\.vscode\ResturantRecommendationSystem\static"
)

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

# Dummy data - you should replace this with your actual restaurant recommendation logic
restaurants = [
    {"name": "Chez Panisse", "location": "Berkeley, CA", "cuisine": "French"},
    {"name": "Shizen Vegan Sushi", "location": "San Francisco, CA", "cuisine": "Japanese"}
]

@app.route('/')
def index():
    return render_template('index.html', restaurants=restaurants)

@app.route('/api/restaurants')
def api_restaurants():
    return jsonify(restaurants)


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/contact')
def contact():
    return render_template('contactus.html')


if __name__ == '__main__':
    app.run(debug=True)
