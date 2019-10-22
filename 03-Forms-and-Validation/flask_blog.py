from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '20929f20a01e15721f754f4e624bd7e4'

posts = [
    {
        'author' : 'John Doe',
        'title' : 'Programming in Python',
        'summary' : 'Welcome to the world of Python',
        'date' : '21st October 2019'
    },
    {
        'author' : 'Anonymous',
        'title' : 'Programming in C',
        'summary' : 'Welcome to the world of C',
        'date' : '22nd October 2019'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',title='About')

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html',title='Register',form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',title='Login',form=form)

if __name__ == '__main__':
    app.run(debug=True) 