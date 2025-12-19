from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
     return render_template('index.html', title='home Page')

@app.route('/about')
def about():
    title='About Page'
    name='Akarat'
    email='akarat555@gmail.com'
    phone='0963705756'
    return render_template('about.html', title=title,  name=name, email=email, phone=phone)

@app.route('/favoerite/food')
def favorite_food():
    title='Favorite Food'
    foods = ['ข้าวมันไก่', 'ข้าวผัด', 'ข้าวต้ม', 'ผัดมาม่า']
    return render_template('food.html', foods=foods, title=title)

@app.route('/favorite/sport')
def favorite_sport():
    title='Favorite Sport'
    sports = ['แบทมินตัน', 'บาสเกตบอล', 'วิ่ง', 'ปั่นจักรยาน']
    return render_template('sport.html', sports=sports, title=title)

@app.route('/greet/<username>')
def wlcome(username):
    title='Welcome Page'
    return render_template('welcome.html',title=title, username=username)

@app.route('/square/Favorite_movie')
def favorite_movie():
    title='Favorite Movie'
    movies = ['Now You See Me', 'Machete Kill', 'Breaking Bad', 'Lacasa de papel', 'Predator']
    return render_template('movie.html', movies=movies, title=title)