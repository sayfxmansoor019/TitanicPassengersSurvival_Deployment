from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/api/v1/service/myendpoint/score', methods=['POST'])
def predict():
    data = request.get_json()
    
    input1 = data['Inputs']['input1']
    input2 = data['Inputs']['input2']
    input3 = data['Inputs']['input3']
    
    
    prediction = model.predict([[input1, input2, input3]])
    
    return jsonify(prediction.tolist())  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)  
