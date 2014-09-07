# all the imports
import sqlite3
from getfriends import getBuds
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
app = Flask(__name__)
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])
@app.route('/home')
def index():
	return render_template('index.html')

@app.route('/create')
def create():
	return render_template('createnewchat.html')

@app.route('/friends_render.html')
def friends():
	return render_template('friends_render.html')

@app.route('/process')
def process():
	pass


@app.route('/all')
def allfriends():
	buds=getBuds('aditya')
	return render_template('note_page.html',buds=buds)
@app.route('/main')
def main():
	buds=getBuds('aditya')
	return render_template('friends.html',buds=buds)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


app.config.from_object('config')
app.run(debug=True)

