from flask import Flask, request, g
import sqlite3

app = Flask(__name__)
DATABASE = 'sample.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.route('/')
def home():
    return "Hello, World! Go to /add?name=your_name&hobby=your_hobby to add yourself."

@app.route('/add')
def add_user():
    name = request.args.get('name')
    hobby = request.args.get('hobby')
    if not name:
        return "Please provide a name in the URL"
    
    if not hobby:
        return "Please provide a hobby in the URL"
    
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (name, hobby) VALUES (?, ?)", (name, hobby))
    db.commit()
    return f"User {name} - Hobby - {hobby} added!"

@app.route('/users')
def list_users():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT id, name, hobby FROM users")
    rows = cursor.fetchall()
    return '<br>'.join([f"{id}: {name} - {hobby}" for id, name, hobby in rows])

@app.teardown_appcontext
def close_db(error):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
        
if __name__ == '__main__':
    app.run(debug=True)


