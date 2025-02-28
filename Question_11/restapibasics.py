from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/greet/<name>')
def greet(name):
    return jsonify({"message":f"Hello {name}!"})

if __name__ == '__main__':
    app.run(debug = True)