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
from models import db, User, Character, Planet, Favorite
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
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

#user section
@app.route('/user', methods=['GET'])
def handle_hello():

    users= User.get_all_users()
    serialized_users = []
    for user in users:
        serialized_users.append(user.serialize())
    return jsonify(serialized_users), 200


@app.route('/user/<int:user_id>', methods=['GET'])
def handle_hello():

    users= User.get_users_by_id(id)
    return(jsonify(user.serialize()))

#people section
@app.route('/people', methods=['GET'])
def get_people():

    characters = Character.get_all_charactersl()
    serialized_characters = []
    for character in characters:
        serialized_characters.append(character.serialize())

    return(jsonify(serialized_planets))
    

@app.route('/people/<int:people_id>', methods=['GET'])
def get_person(people_id):
    # people_id = 

    character = Character.get_characters_by_id(people_id)
    
    return(jsonify(character.serialize())), 200

#planets section

@app.route('/planets', methods=['GET'])
def get_planets():

    planets = Planets.get_all_planets()
    serialized_planets = []
    for planet in planets:
        serialized_planets.append(planet.serialize())

    return(jsonify(serialized_planets))
    response_body = characters

    return jsonify(response_body), 200

@app.route('/planet/<int:planet_id>', methods=['GET'])
def get_person(planet_id):
    # people_id = 

   planet = Planet.get_planet_by_id(planet_id)
   return(jsonify(planet.serialize())), 200

# favorites section
@app.route('/favorites', methods=['GET'])
def get_all_favorites():
    
    favorites = Favorites.get_all_favorites()
    serialized_favorites = []
    for favorite in favorites:
        serialized_favorites.append(favorite.serialize())

    return(jsonify(serialized_favorites))


@app.route('/favorites/<int:id>', methods=['GET'])
def get_favorites_by_id(id):
    
    favorite = Favorites.get_favorites_by_id(id)
    
    return(jsonify(favorite.serialize()))

#fav post section
@app.route('/favorites/<int:user_id>', methods=['POST']) 
def add_favorite(user_id):
    request_body = request.get_json(force=True)

    user = User.get_users_by_id(user_id)
    uid = request_body["uid"]
    element_id = uid[2:]
    new_favorite = None

    if uid.startswith("c"):
        new_favorite = Favorite(user_id=user.id, character_id=element_id)
    else:
        new_favorite = Favorite(user_id=user.id, planet_id=element_id)

    db.session.add(new_favorite)
    db.session.commit()
    

    return jsonify(new_favorite.serialize())

#fav delete section

@app.route('/favorites/<int:user_id>', methods=['DELETE']) 
def add_favorite(user_id):
    request_body = request.get_json(force=True)

    user = User.get_users_by_id(user_id)
    uid = request_body["uid"]
    element_id = uid[2:]
    remove_favorite = None

    if uid.startswith("c"):
        remove_favorite = Favorite(user_id=user.id, character_id=element_id)
    else:
        remove_favorite = Favorite(user_id=user.id, planet_id=element_id)


    db.session.delete(remove_favorite)
    db.session.commit()
    

    return jsonify(remove_favorite.serialize())


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
