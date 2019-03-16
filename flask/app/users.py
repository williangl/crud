from flask import Blueprint

from .model import User
from .serealizer import UserSchema

bp_user = Blueprint('user', __name__)

@bp_user.route('/show', methods=['GET'])
def show():
    bs = UserSchema(many=True)
    result = User.query.all()
    return bs.jsonify(result), 200


@bp_user.route('/delete', methods=['GET'])
def delete():
    ...


@bp_user.route('/update', methods=['POST'])
def update():
    ...


@bp_user.route('/insert', methods=['POST'])
def insert():
    ...
