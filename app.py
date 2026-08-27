from flask import Flask, jsonify, request, session

app = Flask(__name__)

# In-memory stores that persist for the lifetime of this process
votes = {}
users = {}

@app.route('/')
def home(): 
    return "Welcome to the Home Page!"

@app.route('/health')
def health():
    return "Application is running"

@app.route('/vote/<name>')
def vote(name):
    if name not in votes:
        votes[name] = 1
    else:
        votes[name] += 1
    return f"Vote received for {name}! Total votes: {votes[name]}"

@app.route('/session_vote/<name>')
def session_vote(name):
    if 'votes' not in session:
        session['votes'] = {}
    session['votes'][name] = session['votes'].get(name, 0) + 1
    return f"Session vote received for {name}! Your session votes: {session['votes'][name]}"

@app.route('/results')
def results():
    return votes

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify(error='A JSON body is required'), 400

    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify(error='Username and password are required'), 400

    users[username] = password
    return jsonify(message=f'User {username} added successfully'), 201


@app.route('/get/<username>', methods=['GET'])
def get_password(username):
    if username not in users:
        return jsonify(error=f'User {username} not found'), 404

    return jsonify(username=username, password=users[username]), 200



if __name__ == '__main__':
    app.run(debug=True, port=5000)