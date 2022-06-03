
from ctypes import resize
import numpy as np
import random
import pickle
from flask import Flask, render_template, request
from CPT import *
model = CPT()
data = model.load_files("./data/train.csv")

# intialize Flask
app = Flask(__name__)


def train(CPTmodel):
    return CPTmodel.train()


def getSeq(inp, num):
    diff = np.diff(np.array(inp))
    d = sum(diff)/len(diff)
    d = round(d)
    print(np.diff(np.array(inp)))
    seq = [round(i) for i in np.arange(inp[-1]+d, inp[-1]+(d*num+1), d)]
    return seq


def predictSequence(data, target, r, k=5):
    emp = open("model.pkl", "rb")
    model_p = pickle.load(emp)
    # return model_p.predict(data, [target], k, r)

    sq = getSeq(target, r)
    print(sq)
    return sq


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def homepage():
    return render_template('home.html')


@app.route('/train')
def train():
    model.train(data)
    with open('model.pkl', 'wb') as fh:
        pickle.dump(model, fh)
    return render_template('trainresult.html')


@app.route('/predict', methods=['GET', 'POST'])
def predictResult():
    steps = 5
    numpred = 3
    if request.method == 'POST':

        print(request.form)
        sequence = list(map(int, request.form.get('sequence').split()))
        numpred = int(request.form.get('numpred'))
        print(sequence)
        result = getSeq(sequence, numpred)
        return render_template('predictresult.html', result=result, steps=steps)
    return render_template('predict.html', steps=steps)


@app.route('/test', methods=['GET', 'POST'])
def trainResult():
    if request.method == 'POST':
        print(request.form)
    return render_template('trainresult.html')


def predictSeq(target, num_predictions=1):
    predictions = model.predict(data, target, 5, n=num_predictions)
    return render_template('predictresult.html', predictions=predictions)


if __name__ == '__main__':

    # to run the flask app in the debug mode (app will start automatically)
    app.run(debug=True)
