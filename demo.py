from flask import Flask, request, render_template
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/demo/', methods=['POST'])
def respond():
    curr_num = request.args.get("curr_num", "0")

    new_num = int(curr_num) + 1

    response = f"<button hx-post=\"https://htmxdemo.herokuapp.com/demo/?curr_num={new_num}\" hx-swap=\"outerHTML\">Click Me - {new_num}</button>"

    return response

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(threaded=True, port=5000)