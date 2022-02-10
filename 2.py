from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/trainig/<job>')
def index(job):
    return render_template('training.html', job=job)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

