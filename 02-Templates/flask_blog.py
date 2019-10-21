from flask import Flask, render_template, url_for

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True) 