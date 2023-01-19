from flask import Flask, render_template

from users import users_blueprint
from database import init_db, db_session


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.register_blueprint(users_blueprint, url_prefix='/users')

    with app.app_context():
        init_db()

    return app


app = create_app()


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template('about.html')
