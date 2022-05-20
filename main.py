from flask import Flask, render_template
from CPT import *
model = CPT()
data = model.load_files("./data/train.csv")


# intialize Flask
app = Flask(__name__)


def train(CPTmodel):
    return CPTmodel.train()


def predictSequence(data, target, k, r):
    return model.predict(data, [target], k, r)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def homepage():
    return render_template('home.html')


if __name__ == '__main__':

    # to run the flask app in the debug mode (app will start automatically)
    app.run(debug=True)
