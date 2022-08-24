from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorite = db.relationship('Favorite', lazy=True )

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
    @classmethod
    def get_all_users(cls):
        users = cls.query.all()
        return users

    @classmethod
    def get_users_by_id(cls, id):
        users_by_id = cls.query.filter_by(id = id).one_or_none()
        return users_by_id

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    height = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    hair_color = db.Column(db.String(250))
    skin_color = db.Column(db.String(250))
    eye_color = db.Column(db.String(250))
    year_of_birth = db.Column(db.String(250))
    gender = db.Column(db.String(250))
    uid = db.Column(db.String(50))
    children = db.relationship('Favorite', lazy=True)

    def __repr__(self):
        return '<Character %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "year_of_birth": self.year_of_birt,
            "gender": self.gender,
            "uid": self.uid
        }

    @classmethod
    def get_all_characters(cls):
        characters = cls.query.all()
        return characters

    @classmethod
    def get_characters_by_id(cls, id):
        characters_by_id = cls.query.filter_by(id = id).one_or_none()
        return characters_by_id

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    diameter = db.Column(db.Integer)
    rotation_period = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    gravity = db.Column(db.String(250))
    population = db.Column(db.Integer)
    climate = db.Column(db.String(250))
    terrain = db.Column(db.String(250))
    surface_water = db.Column(db.Integer)
    uid = db.Column(db.String(50))
    children = db.relationship('Favorite', lazy=True)

    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "uid": self.uid
        }
    def serialize_basics(self):
        return {
            "id": self.id,
            "name": self.name,
            "uid": self.uid
        }
    
    @classmethod
    def get_all_planets(cls):
        planets = cls.query.all()
        return planets

    @classmethod
    def get_planet_by_id(cls, id):
        planets_by_id = cls.query.filter_by(id = id).one_or_none()
        return planets_by_id

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    character_id = db.Column(db.Integer, db.ForeignKey(Character.id))
    planet_id = db.Column(db.Integer, db.ForeignKey(Planet.id))

    def __repr__(self):
        return f'<Favorite {self.user_id}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id
        }

    @classmethod
    def get_all_favorites(cls):
        favorites = cls.query.all()
        return favorites

    @classmethod
    def get_favorite_by_id(cls, id):
        favorites_by_id = cls.query.filter_by(id = id).one_or_none()
        return favorites_by_id
    
    
    

    