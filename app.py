
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

# initiazlize db
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(300), nullable = False)
    def __repr__(self):
        return '<Task %r>' % self.id

# creation of db tables within app context
with app.app_context():
    db.create_all()

    
@app.route('/')
def home():
    #return "hello world"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)