from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register_user():
    # Logic for registering a user
    return jsonify({"message": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login_user():
    # Logic for user login
    return jsonify({"message": "User logged in successfully"}), 200

@app.route('/profile', methods=['GET'])
def user_profile():
    # Logic to get user profile
    return jsonify({"user": "John Doe", "email": "john.doe@example.com"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
