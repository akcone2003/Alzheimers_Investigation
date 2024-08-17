import unittest
from unittest.mock import patch, MagicMock, mock_open
import numpy as np
import pandas as pd
from flask import json

# Patch 'load_model' before importing 'main'
with patch('model_loader.load_model'):
    from app import app  # Importing the app after patch


class TestPredictFunction(unittest.TestCase):
    """
    The main testing class for testing the Flask application.
    It uses the built-in unittest module in Python. Some functions from `unittest.mock` are used to replace parts of
    the code that would do real actions (like opening a file or calling a model's predict function) with mock objects
    which simplifies testing and allows you to focus on the unit of code that you are trying to test.
    """
    def setUp(self):
        """
        This method sets up each test with a fresh test client.
        It is automatically called before each test method defined in this class.
        """
        self.app = app.test_client()
        self.app.testing = True

    def data_input(self):
        """
        This method provides a dictionary of sample data which is used for testing.
        """
        return {
            'Age': '34',
            'Gender': '0',
            'Ethnicity': '1',
            'EducationLevel': '5',
            'BMI': '24',
            'Smoking': '0',
            'AlcoholConsumption': '3',
            'PhysicalActivity': '7',
            'DietQuality': '8',
            'SleepQuality': '6',
            'FamilyHistoryAlzheimers': '1',
            'CardiovascularDisease': '0',
            'Diabetes': '0',
            'Depression': '0',
            'HeadInjury': '0',
            'Hypertension': '1',
            'SystolicBP': '110',
            'DiastolicBP': '80',
            'CholesterolTotal': '140',
            'CholesterolLDL': '65',
            'CholesterolHDL': '60',
            'CholesterolTriglycerides': '150',
            'MMSE': '23',
            'FunctionalAssessment': '15',
            'MemoryComplaints': '2',
            'BehavioralProblems': '3',
            'ADL': '5',
            'Confusion': '1',
            'Disorientation': '1',
            'PersonalityChanges': '1',
            'DifficultyCompletingTasks': '0',
            'Forgetfulness': '1',
        }

    @patch('app.load_model')
    @patch('app.process_features', return_value=pd.DataFrame())
    @patch('app.render_template', return_value="The probability of Alzheimer's is 0.75. This indicates a high risk.")
    @patch('app.model.predict_proba', return_value=np.array([[0.25, 0.75]]))
    @patch('app.open', create=True)
    def test_predict(self, mock_predict_proba, mock_render_template, mock_process_features, mock_load_model, mock_open):
        """
        Tests the '/predict' route of the application.
        Five actions are mocked here:
        - loading the model,
        - processing the features of the model,
        - rendering the template,
        - calling the model's predict_proba function, and
        - opening the weights json files.

        The test checks that the route returns the expected status code and data.
        """
        data = self.data_input()

        # Mock the open function used to open 'weights/health_weights.json'
        health_weights = json.dumps({
            "SystolicBP": 0.16713048467999211, "CholesterolTotal": 0.20538780018515296,
            "CholesterolLDL": 0.20371637265656023,
            "CholesterolHDL": 0.21295212981036069, "CholesterolTriglycerides": 0.21081321266793412,
            "BMI": 0.19723692111125013, "PhysicalActivity": 0.1880104973471069,
            "DietQuality": 0.19348311953836947, "SleepQuality": 0.20101583931020794,
            "Smoking": 0.023329569340162733, "AlcoholConsumption": 0.1969240533529028
        })

        cardiometabolic_weights = json.dumps({
            "SystolicBP": 0.16713048467999211, "CholesterolTotal": 0.20538780018515296,
            "CholesterolLDL": 0.20371637265656023,
            "CholesterolHDL": 0.21295212981036069, "CholesterolTriglycerides": 0.21081321266793412,
        })

        def mock_read(file):
            if file == 'weights/health_weights.json':
                return health_weights
            if file == 'weights/cardiometabolic_weights.json':
                return cardiometabolic_weights

        # Replace the 'read' method with our 'mock_read' function
        mock_open.return_value.__enter__.return_value.read.side_effect = mock_read

        # Make the request to the '/predict' endpoint using the test client
        response = self.app.post('/predict', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "The probability of Alzheimer's is 0.75. This indicates a high risk.")

    @patch('app.process_features', return_value=pd.DataFrame())
    def test_predict_exception(self,_):
        """
        Tests the exception handling mechanism in the '/predict' route by sending incorrect sample data
        and verifying that a status code 500 is returned.
        """
        data = {'incorrect_feature': '4'}

        response = self.app.post('/predict', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 500)


if __name__ == '__main__':
    unittest.main()
