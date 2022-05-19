from flask import Flask, render_template
from CPT import *
model = CPT()
data = model.load_files("./data/train.csv")
model = None

# intialize Flask
app = Flask(__name__)


def train(CPTmodel):
    return CPTmodel.train()


def predict(data, target, 5, 3):


@app.route('/')
@app.route('/home')
def homepage():
    return render_template('home.html')


if __name__ == '__main__':

    # to run the flask app in the debug mode (app will start automatically)
    app.run(debug=True)