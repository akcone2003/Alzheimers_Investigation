import joblib
import numpy as np
from flask import Flask, request, render_template
import pickle
import pandas as pd
import json

# Create app object using Flask class
app = Flask(__name__)

# Load trained model
with open("models/model.pkl", "rb") as file:
    model = pickle.load(file)


# Define route to be home
# The decorator below links the relative route of the URL to the function it is decorating
# Home function is the '/' our root directory
# Running the app sends us to index.html

# use the route() decorator to tell Flask what URL should trigger our function
@app.route('/')
def home():
    return render_template("index.html")


# need to process the features the same way in the live data form
def process_features(raw_features):
    # Load the feature weights
    with open('weights/health_weights.json', 'r') as file:
        health_weights = json.load(file)

    with open('weights/cardiometabolic_weights.json', 'r') as file:
        cardiometabolic_weights = json.load(file)

    # Define columns name based on their order in form
    feature_names = [
        'Age', 'BMI', 'AlcoholConsumption', 'PhysicalActivity', 'DietQuality', 'SleepQuality',
        'SystolicBP', 'DiastolicBP', 'CholesterolTotal', 'CholesterolLDL', 'CholesterolHDL',
        'CholesterolTriglycerides', 'MMSE', 'FunctionalAssessment', 'ADL', 'EducationLevel',
        'Gender', 'Ethnicity', 'Smoking', 'FamilyHistoryAlzheimers', 'CardiovascularDisease',
        'Diabetes', 'Depression', 'HeadInjury', 'Hypertension', 'MemoryComplaints',
        'BehavioralProblems', 'Confusion', 'Disorientation',
        'PersonalityChanges', 'DifficultyCompletingTasks', 'Forgetfulness'
    ]

    features_df = pd.DataFrame([raw_features], columns=feature_names)

    # Compute additional features
    features_df['HealthScore'] = sum(features_df[col] * weight for col, weight in health_weights.items())
    features_df['CardiometabolicIndex'] = sum(
        features_df[col] * weight for col, weight in cardiometabolic_weights.items())
    features_df['TotalHealthScore'] = features_df['HealthScore'] + features_df['CardiometabolicIndex']

    preprocessor = joblib.load('preprocessor.pkl')

    numeric_features = ['Age', 'BMI', 'AlcoholConsumption', 'PhysicalActivity', 'DietQuality',
                        'SleepQuality', 'SystolicBP', 'DiastolicBP', 'CholesterolTotal',
                        'CholesterolLDL', 'CholesterolHDL', 'CholesterolTriglycerides',
                        'MMSE', 'FunctionalAssessment', 'ADL', 'HealthScore',
                        'CardiometabolicIndex', 'TotalHealthScore']
    print(f"Features dataframe before scaling{features_df}") # DEBUG
    features_df = preprocessor.transform(features_df)
    print(f"Features dataframe after scaling {features_df}") # DEBUG
    return features_df


@app.route('/predict', methods=['POST'])
def predict():
    try:
        raw_features = [float(x) for x in request.form.values()]
        print(f'Raw features: {raw_features}')
        # DEBUG
        processed_features_df = process_features(raw_features)

        print(f'Processed features: {processed_features_df}')  # DEBUG
        print(f'Processed features shape: {processed_features_df.shape}')  # DEBUG
        print(f'Processed features columns: {processed_features_df.tolist()}')  # DEBUG
        prediction = model.predict_proba(processed_features_df)

        print(
            f'Prediction for negative: {np.round(prediction[0], 2)} and Prediction for Positive: {np.round(prediction[0][1], 2)}')
        output = round(prediction[0][1], 2)

        return render_template('index.html', prediction_text="The probability of Alzheimer's is {}".format(output))
    except Exception as e:
        app.logger.error(f'Error occurred: {e}')
        raise e


if __name__ == '__main__':
    app.run()
