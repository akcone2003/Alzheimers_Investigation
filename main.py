from flask import Flask, request, render_template
import pandas as pd
import json
from model_loader import load_model

# Create app object using Flask class
app = Flask(__name__)

# Load the model
model = load_model()


# Define route to be home
# The decorator below links the relative route of the URL to the function it is decorating
# Home function is the '/' our root directory
# Running the app sends us to index.html

# use the route() decorator to tell Flask what URL should trigger our function
@app.route('/')
def home():
    """

    Home Method

    This method is used to render the index.html template and return it.

    :return: The rendered index.html template

    """
    return render_template("index.html")


# need to process the features the same way in the live data form
def process_features(raw_features):
    """
    Process the raw features and compute additional features.

    :param raw_features: dictionary containing the raw features
    :return: DataFrame containing the processed features

    """
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

    # Compute additional features
    # Computing HealthScore
    features_df['HealthScore'] = sum(features_df[col] * weight for col, weight in health_weights.items()
                                     if col in features_df.columns)
    # Computing CardiometabolicIndex
    features_df['CardiometabolicIndex'] = sum(
        features_df[col] * weight for col, weight in cardiometabolic_weights.items()
        if col in features_df.columns)

    # Computing the TotalHealthScore
    features_df['TotalHealthScore'] = features_df['HealthScore'] + features_df['CardiometabolicIndex']

    return features_df


@app.route('/predict', methods=['POST'])
def predict():
    """
    :return: The predicted risk level of developing Alzheimer's disease.
    The predicted risk level is returned as a string, which can be one of the following:
    - "high" : Indicates a high risk of developing Alzheimer's disease.
    - "moderate" : Indicates a moderate risk of developing Alzheimer's disease.
    - "low" : Indicates a low risk of developing Alzheimer's disease.

    The prediction is made based on the given features provided in the form data.

    The features are casted to their respective data types as defined in the `feature_types`
    dictionary. This dictionary maps the feature names to their data types.

    The features are then processed using the `process_features` method, which returns a
    processed features dataframe.

    The trained model is used to make predictions on the processed features dataframe.
    The prediction is returned as an array of probabilities. The second element of this array
    represents the probability of developing Alzheimer's disease.

    The predicted probability is rounded to 4 decimal places and stored in the `output` variable.

    The risk level is assessed based on the `output` probability. If the `output` probability is
    greater than or equal to 0.7, the risk level is set to "high". If the `output` probability is
    greater than or equal to 0.4, the risk level is set to "moderate". Otherwise, the risk level
    is set to "low".

    The prediction and risk level are rendered in the 'index.html' template using the Flask
    `render_template` function. The prediction is displayed as the chances of developing
    Alzheimer's disease in percentage form (output * 100) and the risk level is displayed
    accordingly.

    In case of any exception, an error message is logged and the exception is raised.
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

        processed_features_df = process_features(casted_features)

        # Making predictions using trained model
        prediction = model.predict_proba(processed_features_df)

        output = round(prediction[0][1], 4)

        # Assessing risk
        if output >= 0.7:
            risk_level = "high"
        elif output >= 0.4:
            risk_level = "moderate"
        else:
            risk_level = "low"

        return render_template('index.html',
                               prediction_text=f"Your chances of developing Alzheimer's is {output * 100}%. This indicates a {risk_level} risk.")
    except Exception as e:
        app.logger.error(f'Error occurred: {e}')
        raise e


if __name__ == '__main__':
    app.run()
