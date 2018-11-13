from flask import render_template,make_response, jsonify
from app.models import User

from app import app


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/index', methods=['GET', 'POST'], endpoint='index')
def index(name=None):
    return render_template('index.html', name=name)


@app.route('/users')
def get_users():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/users/<int:id>')
def get_user_by_id(id):
    return User.query_user_by_id(id)


if __name__ == '__main__':
    app.run()
