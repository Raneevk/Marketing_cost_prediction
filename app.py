from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('linear_regression_model.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction = -int(model.predict(final)[0])
    if prediction>500:
        return render_template('index.html',pred='Your marketing cost is more than 500 rupees make sure the lead quality is good for this region.\n optimum cost for this region is rupees: {}'.format(prediction),bhai="Good luck!")
    else:
        return render_template('index.html',pred='Your marketing cost is less than 500.\n optimum cost is rupees {}'.format(prediction),bhai="Good luck!")

if __name__ == '__main__':
    app.run(debug=True)