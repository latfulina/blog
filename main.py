from flask import Flask, render_template, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/user/<string:name>/<int:id>')
def user(name,id):
    return "User page:" +name + "-" + str(id)

# Запуск сервера,с проверкой. Если этот файл запускается,как основной файл
if __name__ == "__main__":
    app.run(debug=True)