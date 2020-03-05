from flask import Flask
import os
from histogram import histogram
app = Flask(__name__)

@app.route('/')
def hello_world():
    return histogram('despacito.txt')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
