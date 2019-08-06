from flask import render_template, url_for, flash, redirect
from flaskblog import app, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.view_containers_flask import perform_orion_function
#from flaskblog.models import User, Post, OrionUser
#import csv

posts = [
        {
                'author': 'Example 1',
         'title': 'Example Title 1',
         'content': 'Lorem ipsum dolor sit amet, ignota placerat liberavisse eam ei, elit saperet concludaturque sit ne. Discere postulant sadipscing qui ad, ei sea nostrum deseruisse. Sit id utinam insolens erroribus. Facilisi torquatos duo id. In volumus honestatis sit. Assum adipisci reprehendunt his an. Ubique persequeris pro cu, pro eirmod minimum ad.',
         'date_posted': 'April 20, 2018'
         },
        {'author': 'Example 2',
         'title': 'Example Title 2',
         'content': 'Mel etiam iuvaret ex, ex suas lobortis vulputate vis. Mei elit utinam platonem in, eu commodo vidisse vel. Vis unum salutatus in. Paulo tritani corrumpit ex qui, ex recusabo invenire liberavisse nam. In unum duis electram pro, his an discere iudicabit. At impetus alterum inermis vel, ex eam diam modus primis.',
         'date_posted': 'April 21, 2018'
         }
        ]


@app.route("/")
@app.route("/home")
# / = root page or home page
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
# / = root page or home page
def about():
    return render_template('about.html', title='About')

@app.route("/orion")
def orion():
    return render_template('orion.html', title='Orion')

@app.route("/login_1", methods=['GET', 'POST'])
def login_1():
    form  = LoginForm()
    if form.validate_on_submit():
#        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        return perform_orion_function('view', form.username.data, form.password.data, form.request_id.data)

#        return redirect(url_for('home'))
    return render_template('login_1.html', title='Orion', form=form)

@app.route("/login_2", methods=['GET', 'POST'])
def login_2():
    form  = LoginForm()
    if form.validate_on_submit():
#        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
#        perform_orion_function('view', form.username.data, form.password.data, form.request_id.data)
        flash('Orion information saved', 'success')
        return redirect(url_for('home'))
    return render_template('login_2.html', title='Orion', form=form)

@app.route("/login_3", methods=['GET', 'POST'])
def login_3():
    form  = LoginForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        flash('Orion information saved', 'success')
        return redirect(url_for('home'))
    return render_template('login_3.html', title='Orion', form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
#        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
#        user = OrionUser(username=form.username, password=hashed_password)
#        db.session.add(user)
#        db.session.commit()
        flash(f'Your account is now created, you are now able to log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)



