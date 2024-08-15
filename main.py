import joblib
import numpy as np
from flask import Flask, request, render_template
import pickle
import pandas as pd
import json
from model_loader import load_model

# Create app object using Flask class
app = Flask(__name__)

# Load the model
model = load_model()


# Print model configuration
print("Model Configuration:")
print(model.get_params())


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

    # Define data columns
    df_columns = [
        'Age', 'Gender', 'Ethnicity', 'EducationLevel', 'BMI', 'Smoking',
        'AlcoholConsumption', 'PhysicalActivity', 'DietQuality', 'SleepQuality',
        'FamilyHistoryAlzheimers', 'CardiovascularDisease', 'Diabetes', 'Depression',
        'HeadInjury', 'Hypertension', 'SystolicBP', 'DiastolicBP', 'CholesterolTotal',
        'CholesterolLDL', 'CholesterolHDL', 'CholesterolTriglycerides', 'MMSE',
        'FunctionalAssessment', 'MemoryComplaints', 'BehavioralProblems', 'ADL',
        'Confusion', 'Disorientation', 'PersonalityChanges',
        'DifficultyCompletingTasks', 'Forgetfulness',
    ]

    # Create DataFrame
    features_df = pd.DataFrame([raw_features], columns=df_columns)

    print(f"Dataframe BEFORE additional features are computed {features_df.to_dict()}\n")  # DEBUG

    # Compute additional features
    features_df['HealthScore'] = sum(features_df[col] * weight for col, weight in health_weights.items()
                                     if col in features_df.columns)
    features_df['CardiometabolicIndex'] = sum(
        features_df[col] * weight for col, weight in cardiometabolic_weights.items()
        if col in features_df.columns)

    features_df['TotalHealthScore'] = features_df['HealthScore'] + features_df['CardiometabolicIndex']

    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    print(f"Dataframe AFTER additional features are computed {features_df.to_dict()}\n")  # DEBUG

    return features_df


@app.route('/predict', methods=['POST'])
def predict():
    """
    This method is used to predict the probability of Alzheimer's disease based on a set of input features.

    :return: A rendered HTML template with the prediction result and risk level.

    """
    try:

        # define a dictionary mapping feature names to their data types
        feature_types = {
            'Age': int,
            'Gender': int,
            'Ethnicity': int,
            'EducationLevel': int,
            'BMI': float,
            'Smoking': int,
            'AlcoholConsumption': float,
            'PhysicalActivity': float,
            'DietQuality': float,
            'SleepQuality': float,
            'FamilyHistoryAlzheimers': int,
            'CardiovascularDisease': int,
            'Diabetes': int,
            'Depression': int,
            'HeadInjury': int,
            'Hypertension': int,
            'SystolicBP': int,
            'DiastolicBP': int,
            'CholesterolTotal': float,
            'CholesterolLDL': float,
            'CholesterolHDL': float,
            'CholesterolTriglycerides': float,
            'MMSE': float,
            'FunctionalAssessment': float,
            'MemoryComplaints': int,
            'BehavioralProblems': int,
            'ADL': float,
            'Confusion': int,
            'Disorientation': int,
            'PersonalityChanges': int,
            'DifficultyCompletingTasks': int,
            'Forgetfulness': int,
        }

        # get raw features from form values
        raw_features = request.form.values()

        # cast raw_features to respective data types
        casted_features = [feature_types[feature_name](feature_value) for feature_name, feature_value in
                           zip(feature_types, raw_features)]

        print(f'Raw features: {casted_features}')
        # DEBUG
        processed_features_df = process_features(casted_features)

        print(f'Processed features: {processed_features_df.to_dict()}\n')  # DEBUG
        print(f'Processed features shape: {processed_features_df.shape}\n')  # DEBUG

        print(f'Features expected by the model: {model.feature_names_in_}')  # DEBUG
        print(f'Features provided for prediction: {processed_features_df.columns}')  # DEBUG

        # Making predictions using trained model
        prediction = model.predict_proba(processed_features_df)

        print(f"Prediction for negative: {np.round(prediction[0], 2)} "
              f"and Prediction for Positive: {np.round(prediction[0][1], 2)}")
        output = round(prediction[0][1], 2)

        # Assessing risk
        if output >= 0.7:
            risk_level = "high"
        elif output >= 0.4:
            risk_level = "moderate"
        else:
            risk_level = "low"

        return render_template('index.html',
                               prediction_text=f"The probability of Alzheimer's is {output}. This indicates a {risk_level} risk.")
    except Exception as e:
        app.logger.error(f'Error occurred: {e}')
        raise e


if __name__ == '__main__':
    app.run()
