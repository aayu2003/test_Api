from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify('Welcome to the API'),200

@app.route('/api/data', methods=['GET'])
def get_data():
    # Check for the API key in the request headers
    api_key = request.headers.get('X-API-Key')

    # Replace 'YOUR_API_KEY' with your actual API key
    if api_key == 'YOUR_API_KEY':
        data = {'message': 'This is the protected data.'}
        return jsonify(data), 200
    else:
        return jsonify({'error': 'Invalid API key'}), 401

if __name__ == '__main__':
    app.run()
