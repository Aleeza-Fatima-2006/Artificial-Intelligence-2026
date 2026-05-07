import numpy as np
import pickle
import joblib
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Load the model and encoders
with open('random_forest_model.pkl', 'rb') as f:
    model = pickle.load(f)

encoders = joblib.load("encoders.pkl")

# List all available categories (for dropdowns)
JOB_TITLES = list(encoders['job_title'].classes_)
COUNTRIES = list(encoders['country'].classes_)
EXP_LEVELS = list(encoders['experience_level'].classes_)
EDU_LEVELS = list(encoders['education_level'].classes_)
PRIMARY_SKILLS = list(encoders['primary_skill'].classes_)

@app.route('/')
def index():
    return render_template('index.html',
                           job_titles=JOB_TITLES,
                           countries=COUNTRIES,
                           exp_levels=EXP_LEVELS,
                           edu_levels=EDU_LEVELS,
                           primary_skills=PRIMARY_SKILLS)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        job_title = request.form['job_title']
        country = request.form['country']
        exp_level = request.form['experience_level']
        edu_level = request.form['education_level']
        year = int(request.form['year'])
        primary_skill = request.form['primary_skill']

        # Encode categorical features using the loaded encoders
        job_enc = encoders['job_title'].transform([job_title])[0]
        country_enc = encoders['country'].transform([country])[0]
        exp_enc = encoders['experience_level'].transform([exp_level])[0]
        edu_enc = encoders['education_level'].transform([edu_level])[0]
        skill_enc = encoders['primary_skill'].transform([primary_skill])[0]

        # Prepare feature array (order must match training)
        features = np.array([[job_enc, country_enc, exp_enc, edu_enc, year, skill_enc]])

        # Predict salary
        predicted_salary = model.predict(features)[0]

        return jsonify({'success': True, 'salary': round(predicted_salary, 2)})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)