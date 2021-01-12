from flask import Flask
from flask import render_template, request, redirect
import sqlite3
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['GET'])
def search():
    if request.method == 'GET':
        if not request.args:
            return(redirect('/', 302))
        elif request.args['query'] == '':
            return(redirect('/', 302))
        else:
            conn = sqlite3.connect('teachers.db')
            c = conn.cursor()
            search = request.args['query']
            c.execute("SELECT name, address FROM teachers WHERE name LIKE ? OR address LIKE ?", (f'%{search}%', f'%{search}%'))
            conn.commit()
            data = c.fetchall()
            conn.close()
            return render_template('index.html', teachers=data)
    else:
        return(redirect('/', 302))
