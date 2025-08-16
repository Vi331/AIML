from flask import Flask, request, render_template
import pickle

app = Flask(__name__, template_folder='templates')

# Load trained model
model = pickle.load(open('C:/Users/varsh/PycharmProjects/FlaskProject1/model_performance.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    study_hours = float(request.form['feature1'])
    attendance = float(request.form['feature2'])
    previous_grade = float(request.form['feature3'])

    input_data = [[study_hours, attendance, previous_grade]]
    result = model.predict(input_data)

    return render_template('result.html', prediction=result)

print("✅ Student Project Running")

if __name__ == '__main__':
    app.run(debug=True)
