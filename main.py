
from flask import Flask, render_template, request
from CPT import *
model = CPT()
data = model.load_files("./data/train.csv")

# intialize Flask
app = Flask(__name__)


def train(CPTmodel):
    return CPTmodel.train()


def predictSequence(data, target, r, k=5):
    return model.predict(data, [target], k, r)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def homepage():
    return render_template('home.html')


@app.route('/train')
def train():
    model.train(data)
    return render_template('trainresult.html')


@app.route('/predict', methods=['GET', 'POST'])
def predictResult():
    if request.method == 'POST':
        print(request.form)
        seqToPredict = list(map(int, request.form.values()))
        print(seqToPredict)
        result = predictSequence(data, seqToPredict, 3)
        return render_template('predictersult.html', result=result)
    return render_template('predict.html')


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
