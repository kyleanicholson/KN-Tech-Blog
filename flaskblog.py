from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '2988ca4092a1903fb8f9c1a40a2ab02e'

posts = [
    {
        'author': 'Kyle Nicholson',
        'title': 'Blog Post 0',
        'content': 'First post content',
        'date_posted': 'September 6, 2022'
    },
    {
        'author': 'Kyle Nicholson',
        'title': 'Blog Post 1',
        'content': 'Second post content',
        'date_posted': 'September 10, 2022',
    },
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title = 'Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)