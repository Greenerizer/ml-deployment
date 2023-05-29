from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load pickle file
model = pickle.load(open("model.pkl", "rb"))

@app.route('/', methods = ["GET"])
def home():
   return render_template("index.html")

@app.route('/predict', methods = ["POST"])
def predict():
   float_features = [float(x) for x in request.form.values()]
   features = [np.array(float_features)]
   prediction = model.predict(features)
   return render_template("index.html", prediction_text = "The flower species is {}".format(prediction))

if __name__ == '__main__':
   app.run(debug=True, port=3000)