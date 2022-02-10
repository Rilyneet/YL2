from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['title'] = 'Домашняя страница'
    return render_template('index.html', **param)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')

