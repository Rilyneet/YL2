from flask import Flask

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    param = {}
    param['title'] = 'Домашняя страница'
    return render_template('base.html', title=title)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
