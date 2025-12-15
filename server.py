from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
     return render_template('index.html', title='home Page')
@app.route('/about')
def about():
    title='About Page'
    name='Aekkachat'
    email='eafafa'              
    phone='0812345678'


    return render_template('about.html', title=title,  name=name, email=email, phone=phone)

@app.route('/favoerite/food')
def favorite_food():
    title='Favorite Food'
    foods = ['Pizza', 'Sushi', 'Ice Cream', 'Tacos']
    return render_template('food.html', foods=foods,itle=title)

@app.route('/favorite/sport')
def favorite_sport():
    title='Favorite Sport'
    sports = ['บอล', 'บาสเกตบอล', 'วอลเลย์บอล', 'ว่ายน้ำ']
    return render_template('sport.html', sports=sports, title=title)

@app.route('/greet/<username>')
def wlcome(username):
    title='Welcome Page'
    return render_template('welcome.html',title=title, username=username)