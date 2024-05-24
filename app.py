from flask import Flask
from flask import request
from flask import jsonify
import pickle


app = Flask(__name__)


@app.route("/api/v1.0/predict", methods=['GET'])
def predict():
    x1 = request.args.get("x1", 0, type=float)
    x2 = request.args.get("x2", 0, type=float)
    with open('perceptron.pickle',"rb") as picklefile:
        nn = pickle.load(picklefile)
    result = nn.predict([[x1, x2]])
    features = {'x1': x1, 'x2': x2}
    predicted_class = {'cls': result[0]}
    return jsonify(features=features, predicted_class=predicted_class)


if __name__ == '__main__':
    app.run()