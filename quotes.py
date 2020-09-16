from flask import Flask, render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# connecting to localhost database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:admin@localhost/quotes'

# connecting to heroku database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ucecgudjxttnqt:f65fd51262640552e63066897aed97e52fd1de53b2ac7d624e1be3b867d2671b@ec2-54-157-234-29.compute-1.amazonaws.com:5432/d86oj4fqo2j4kb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)

class Favquotes(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))

@app.route('/')
def index():
    result = Favquotes.query.all()
    return render_template('index.html',result=result)


@app.route('/quotes')
def quotes():
    return render_template('quotes.html')


@app.route('/process',methods = ['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quoteData = Favquotes(author=author, quote=quote)
    db.session.add(quoteData)
    db.session.commit()

    return redirect(url_for('index'))
