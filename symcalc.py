from sympy.abc import *

from flask import Flask, request
app = Flask(__name__)

@app.route('/code', methods=['GET', 'POST'])
def code():
    return str(eval(request.json['code']))

if __name__ == "__main__":
    app.run(debug=True, port=80)
