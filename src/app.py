"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Characters, Planets, Species, Favorites
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

# Get all Charactes and specific characters
@app.route("/people", methods=["GET"])
def get_all_people():

    all_people = Characters.query.all()
    if all_people is None:
        return jsonify("No records found."), 404
    else:
        all_people = list(map(lambda x: x.serialize(), all_people))
        return jsonify(all_people), 200


@app.route("/people/<int:characters_id>", methods=["GET"])
def get_person(characters_id):

    single_person = Characters.query.get(characters_id)

    if single_person is None:
        raise APIException(f'Person ID {characters_id} is not found!', status_code=404)
    
    single_person = single_person.serialize()
    return jsonify(single_person), 200


# @app.route("/planets", methods=["GET"])
# def get_all_planets():
#     pass

# @app.route("/planets/<int:planets_id>", methods=["GET"])
# def get_planet(planets_id):
#     pass

# @app.route("/species", methods=["GET"])
# def get_all_species():
#     pass

# @app.route("/species/<int:species_id>", methods=["GET"])
# def get_specie(species_id):
#     pass

@app.route("/favorites/people", methods=["POST"])
def add_favorite_person():

    data = request.get_json()
    new_favorite_person = Favorites(user_id = data["user_id"], characters_id = data["characters_id"])
    db.session.add(new_favorite_person)
    db.session.commit()

    return jsonify("Your favorite was added!"), 200    











# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
