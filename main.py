import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

status_file = "counter.pkl"

try:
    with open(status_file, "rb") as f:
        count = pickle.load(f)
except FileNotFoundError:
    count = 0

@app.route('/')
def home():
    return render_template('index.html', count=count)

@app.route('/increment')
def increment():
    global count
    count += 1
    save_counter()
    return render_template('index.html', count=count)

@app.route('/decrement')
def decrement():
    global count
    count -= 1
    save_counter()
    return render_template('index.html', count=count)

@app.route('/reset')
def reset():
    global count
    count = 0
    save_counter()
    return render_template('index.html', count=count)

def save_counter():
    with open(status_file, "wb") as f:
        pickle.dump(count, f)

if __name__ == '__main__':
    app.run(debug=True)