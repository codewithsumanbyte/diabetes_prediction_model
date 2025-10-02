from flask import Flask, request, render_template
import pickle
import numpy as np

# Load the trained model
model_path = 'model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract values from form and convert to float
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    
    # Make prediction
    prediction = model.predict(final_features)[0]
    probability = model.predict_proba(final_features)[0][1] * 100

    # Prepare output text
    if prediction == 1:
        output = f"⚠️ Diabetic (Probability: {probability:.2f}%)"
    else:
        output = f"✅ Not Diabetic (Probability: {probability:.2f}%)"

    return render_template('index.html', prediction_text=output)

if __name__ == "__main__":
    app.run(debug=True)
