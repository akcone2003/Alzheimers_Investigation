import numpy as np
from flask import Flask, request, render_template
import pickle

# Create app object using Flask class
app = Flask(__name__)

# Load trained model
model = pickle.load(open("models/model.pk1", "rb"))


# Define route to be home
# The decorator below links the relative route of the URL to the function it is decorating
# Home function is the '/' our root directory
# Running the app sends us to index.html

# use the route() decorator to tell Flask what URL should trigger our function
@app.route('/')
def home():
    return render_template("index.html")


# GET: A GET message is sent, and the server returns data
# POST: Used to send HTML Form data to the server
@app.route('/predict', methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]  # convert string input into float
    features = [np.array(int_features)]  # convert to array

    prediction = model.predict(features)  # predict on input

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='The predicted value is {}'.format(output))


if __name__ == '__main__':
    app.run()
