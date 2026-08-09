import flask

app = flask.Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Home Page!"

@app.route('/health')
def health():
    return "Application is running"

if __name__ == '__main__':
    app.run(debug=True, port=5000)