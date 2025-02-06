from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if username in users:
        return jsonify({"message": "User already exists!"}), 400

    users[username] = password
    return jsonify({"message": "User registered successfully!"})

@app.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if users.get(username) == password:
        return jsonify({"message": "Login successful!"})
    
    return jsonify({"message": "Invalid credentials!"}), 401

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
