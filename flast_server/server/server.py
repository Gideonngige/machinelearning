from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello, World!"

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations':util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    return "Hi"
if __name__ == '__main__':
    print("Starting server...")
    app.run()