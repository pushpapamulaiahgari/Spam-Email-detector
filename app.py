from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load('spam_model.pkl') # Model load chesam

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    if request.method == 'POST':
        message = request.form['message']
        prediction = model.predict([message])[0]
        result = "🚨 SPAM DETECTED" if prediction == 'spam' else "✅ HAM - SAFE MESSAGE"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)