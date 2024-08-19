# Alzheimer's Disease Risk Prediction App

## Problem Statement

Alzheimer's disease is a progressive neurological disorder leading to memory loss, cognitive decline, and loss of independence. As the global population ages, the incidence of Alzheimer's disease is expected to rise, increasing the burden on individuals, families, and healthcare systems. Early detection is crucial for effective intervention and management. Traditional methods often focus on limited factors, but a holistic approach considering a wide range of health and lifestyle factors can provide a more accurate risk assessment.

## Objective

This project aims to develop a predictive model to estimate the probability of developing Alzheimer's disease using a holistic health approach. The model incorporates a comprehensive set of features, including:

- Demographic information
- Cognitive assessments
- Physical health indicators
- Lifestyle factors
- Other relevant metrics

By leveraging a wide range of data, the model provides a personalized risk assessment to improve early detection and intervention.

## Approach

1. **Collect and Preprocess Data**: Utilize a dataset with diverse features related to cognitive function, physical health, and lifestyle habits. Ensure data consistency and completeness through preprocessing.

2. **Feature Engineering**: Create additional features representing holistic health metrics, such as composite scores for cardiometabolic health and overall health quality.

3. **Model Development**: Train a machine learning model (LightGBM) to predict Alzheimer's disease risk. Use cross-validation techniques for robust performance evaluation.

4. **Interpretability and Evaluation**: Assess model performance with metrics like AUC-ROC. Analyze feature importance to understand the impact of various health factors.

5. **Deployment and Application**: Develop a Flask-based web app to allow users to input their health data and receive an Alzheimer's risk estimate. The app provides a probabilistic output to guide proactive health management.

## Significance

This model enhances Alzheimer's disease risk assessment by integrating a broad spectrum of health factors. It improves prediction accuracy and promotes a comprehensive view of health management. Note that this model is intended for educational purposes and should not replace professional medical advice, diagnosis, or treatment.

## Data

The dataset used for this project is sourced from:
- El Kharoua, R. (2024). Alzheimer's Disease Dataset. Kaggle. [Dataset Link](https://www.kaggle.com/dsv/8668279)

## Summary

The project developed a predictive model using the **LightGBM Classifier (LGBMClassifier)** to estimate Alzheimer's disease risk. The model was trained on a diverse set of features and demonstrated strong performance:

- **Test Accuracy**: 95.814%
- **Precision**: 0.95 (Not Diagnosed), 0.97 (Diagnosed)
- **Recall**: 0.98 (Not Diagnosed), 0.92 (Diagnosed)
- **F1-Score**: 0.97 (Not Diagnosed), 0.94 (Diagnosed)
- **AUC-ROC Score**: 0.9516

## Deployment on Heroku

The model is deployed as a web application using **Heroku** and **Flask**. Key steps in the deployment include:

1. **Model Integration**: Integrated LGBMClassifier with a Flask application to process user input and provide risk estimates.

2. **Flask Application Development**: Designed a user-friendly frontend and backend to handle health data and model predictions.

3. **Heroku Deployment**: Deployed the Flask app on Heroku for scalability and reliability. Utilized Heroku's security features and monitoring tools for a secure and responsive application.

[Link to app](https://alzheimers-prediction-app-bd66bc1fb040.herokuapp.com/)
## Key Features

- **User Input**: Provides an intuitive HTML frontend for data input.
- **Risk Assessment**: Returns a probabilistic risk score based on user data.
- **Security**: Utilizes SSL and identity management for secure access.
- **Monitoring**: Tracks performance and usage statistics to ensure reliability.

By deploying on Heroku, the application ensures accessibility, scalability, and security for users seeking to understand their Alzheimer's disease risk and manage their health proactively.

-------

# Data Dictionary
## Patient Information
- **PatientID**: A unique identifier assigned to each patient (4751 to 6900).
    
## Demographic Details
- **Age**: The age of the patients ranges from 60 to 90 years.
- **Gender**: Gender of the patients, where 0 represents Male and 1 represents Female.
- **Ethnicity**: The ethnicity of the patients, coded as follows:
    - 0: Caucasian
    - 1: African American
    - 2: Asian
    - 3: Other
- **EducationLevel**: The education level of the patients, coded as follows:
    - 0: None
    - 1: High School
    - 2: Bachelor's
    - 3: Higher
    
## Lifestyle Factors
- **BMI**: Body Mass Index of the patients, ranging from 15 to 40.
- **Smoking**: Smoking status, where 0 indicates No and 1 indicates Yes.
- **AlcoholConsumption**: Weekly alcohol consumption in units, ranging from 0 to 20.
- **PhysicalActivity**: Weekly physical activity in hours, ranging from 0 to 10.
- **DietQuality**: Diet quality score, ranging from 0 to 10.
- **SleepQuality**: Sleep quality score, ranging from 4 to 10.

## Medical History
- **FamilyHistoryAlzheimers**: Family history of Alzheimer's Disease, where 0 indicates No and 1 indicates Yes.
- **CardiovascularDisease**: Presence of cardiovascular disease, where 0 indicates No and 1 indicates Yes.
- **Diabetes**: Presence of diabetes, where 0 indicates No and 1 indicates Yes.
- **Depression**: Presence of depression, where 0 indicates No and 1 indicates Yes.
- **HeadInjury**: History of head injury, where 0 indicates No and 1 indicates Yes.
- **Hypertension**: Presence of hypertension, where 0 indicates No and 1 indicates Yes.

## Clinical Measurements
- **SystolicBP**: Systolic blood pressure, ranging from 90 to 180 mmHg.
- **DiastolicBP**: Diastolic blood pressure, ranging from 60 to 120 mmHg.
- **CholesterolTotal**: Total cholesterol levels, ranging from 150 to 300 mg/dL.
- **CholesterolLDL**: Low-density lipoprotein cholesterol levels, ranging from 50 to 200 mg/dL.
- **CholesterolHDL**: High-density lipoprotein cholesterol levels, ranging from 20 to 100 mg/dL.
- **CholesterolTriglycerides**: Triglycerides levels, ranging from 50 to 400 mg/dL.

## Cognitive and Functional Assessments
- **MMSE**: Mini-Mental State Examination score, ranging from 0 to 30. Lower scores indicate cognitive impairment.
- **FunctionalAssessment**: Functional assessment score, ranging from 0 to 10. Lower scores indicate greater impairment.
- **MemoryComplaints**: Presence of memory complaints, where 0 indicates No and 1 indicates Yes.
- **BehavioralProblems**: Presence of behavioral problems, where 0 indicates No and 1 indicates Yes.
- **ADL**: Activities of Daily Living score, ranging from 0 to 10. Lower scores indicate greater impairment.

## Symptoms
- **Confusion**: Presence of confusion, where 0 indicates No and 1 indicates Yes.
- **Disorientation**: Presence of disorientation, where 0 indicates No and 1 indicates Yes.
- **PersonalityChanges**: Presence of personality changes, where 0 indicates No and 1 indicates Yes.
- **DifficultyCompletingTasks**: Presence of difficulty completing tasks, where 0 indicates No and 1 indicates Yes.
- **Forgetfulness**: Presence of forgetfulness, where 0 indicates No and 1 indicates Yes.

## Diagnosis Information
- **Diagnosis**: Diagnosis status for Alzheimer's Disease, where 0 indicates No and 1 indicates Yes.

## Confidential Information
- **DoctorInCharge**: This column contains confidential information about the doctor in charge, with "XXXConfid" as the value for all patients.
