from flask import Flask, jsonify, request
from utilities import predict_pipeline
from flask import Flask, render_template, request

app = Flask(__name__)


@app.post('/predict')
# sent text to this endpoint to get prediction
def predict():
    data = request.json
    try:
        sample = data['text']
    except KeyError:
        return jsonify({'error': 'No text sent'})

    sample = [sample]
    predictions = predict_pipeline(sample)
    try:
        result = jsonify(predictions[0])
    except TypeError as e:
        result = jsonify({'error': str(e)})
    print(result)
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)



# to test the end point send to      http://127.0.0.1:5000/predict    the following body
# Content-Type:application/json
# { "text": " i hate it  "}