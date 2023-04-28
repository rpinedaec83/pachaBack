from flask import Flask, request
from flask_orator import Orator, jsonify




#Configuration
DEBUG = True
ORATOR_DATABASES = {
    'default': 'twittor',
    'twittor': {
        'driver': 'postgres',
        'host': 'localhost',
        'user': 'postgres',
        'password': 'pacha23',
        'database': 'twittor'
    }
}

# Creating Flask application
app = Flask(__name__)
app.config.from_object(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

# Initializing Orator
db = Orator(app)



#Modelos
class User(db.Model):
    __fillable__ = ['name', 'email']


#Rutas
@app.route('/users', methods=['POST'])
def create_user():
    user = User.create(**request.get_json())
    return jsonify(user)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.find_or_fail(user_id)
    return jsonify(user)

@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.all()
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    user = User.find_or_fail(user_id)
    user.update(**request.get_json())

    return jsonify(user)



if __name__ == '__main__':
    app.run()