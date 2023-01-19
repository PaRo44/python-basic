from flask import render_template, request, redirect, url_for

from users import users_blueprint
from users.forms import UserForm
from database import db_session
from models import User


@users_blueprint.route('/')
def view():
    users_list = User.query.all()
    return render_template('users/view.html', users_list=users_list)


@users_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(
            name=form.name.data,
            surname=form.surname.data,
            login=form.login.data,
            email=form.email.data
        )
        db_session.add(user)
        db_session.commit()
        return redirect(url_for('users.view'))
    return render_template('users/add.html', form=form)
