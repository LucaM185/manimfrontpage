from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('page.html')

if __name__ == '__main__':
    app.run(port=5132, debug=True, host='0.0.0.0')
