from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
# # class User(db.Model):
# #     id = db.
# Column(db.Integer, primary_key=True)
# #     username = db.
# Column(db.String, unique=True, nullable=False)
# #     password = db.
# Column(db.String, unique=False, nullable=False)
# #     first_name = db.
# Column(db.String, unique=False, nullable=False)
# #     last_name = db.
# Column(db.String, unique=False, nullable=False)
# #     email = db.
# Column(db.String, unique=True, nullable=False)
# #     phone_number =db.
# Column(db.String, unique=False, nullable=True)
# #     gender = db.
# Column(db.String, unique=False, nullable=False)

# #     favorites = relationship('favorites', back_populates='user')



class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False, nullable=False)
    specie = db.Column(db.String, unique=False, nullable=False)
    height = db.Column(db.String, unique=False, nullable=False)
    mass = db.Column(db.String, unique=False, nullable=False)

    def __repr__(self):
        return '<Characters %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "specie": self.specie,
            "height": self.height,
            "mass": self.mass,
            # do not serialize the password, its a security breach
        }

    # # user_id = db.
    # Column(db.Integer, ForeignKey('user.id'))
    # # user = relationship(User)

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False, nullable=False)
    climate = db.Column(db.String, unique=False, nullable=False)
    population = db.Column(db.String, unique=False, nullable=False)
    size = db.Column(db.String, unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "population": self.population,
            "size": self.size,
            # do not serialize the password, its a security breach
        }

    # # user_id = db.
    # Column(db.Integer, ForeignKey('user.id'))
    # # user = relationship(User)

class Species(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False, nullable=False)
    life_span = db.Column(db.String, unique=False, nullable=False)
    planet = db.Column(db.String, unique=False, nullable=False)
    skin_color = db.Column(db.String, unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "life_span": self.life_span,
            "planet": self.planet,
            "skin_color": self.skin_color,
            # do not serialize the password, its a security breach
        }

    # # user_id = db.
    # Column(db.Integer, ForeignKey('user.id'))


class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User)
    characters_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    characters = db.relationship(Characters)
    species_id = db.Column(db.Integer, db.ForeignKey('species.id'))
    species = db.relationship(Species)
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    planets = db.relationship(Planets)
    
    
    
    

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "characters_id": self.characters_id,
            "planets_id": self.planets_id,
            "species_id": self.species_id,
            # do not serialize the password, its a security breach
        }