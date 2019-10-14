from db import db

class Keys(db.Model):
	__tablename__ = "keys"
	id = db.Column(db.Integer, primary_key=True)
	ext_id = db.Column(db.String(10), unique=True, nullable=False)
	created = db.Column(db.DateTime, server_default=db.func.now())
	updated = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
	active = db.Column(db.Boolean)
	tag = db.Column(db.String(16))
	value = db.Column(db.Text)

class Permissions(db.Model):
	__tablename__ = "permissions"
	id = db.Column(db.Integer, primary_key=True)
	ext_id = db.Column(db.String(10), unique=True, nullable=False)
	created = db.Column(db.DateTime, server_default=db.func.now())
	updated = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
	tag = db.Column(db.String(16)) # Random string

class Groups(db.Model):
	__tablename__ = "groups"
	id = db.Column(db.Integer, primary_key=True)
	ext_id = db.Column(db.String(10), unique=True, nullable=False)
	name = db.Column(db.String(16))
	# groups = db.Column()# subgroups
	# entities = db.Column()# child entities.
	created = db.Column(db.DateTime, server_default=db.func.now())
	updated = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

# An entity is whoever can generate keys or can have access to the keys.
class Entity(db.Model):
	__tablename__ = "entity"
	id = db.Column(db.Integer, primary_key=True)
	ext_id = db.Column(db.String(10), unique=True, nullable=False)
	# groups = db.Column()
	tag = db.Column(db.String(10))
	public_key = db.Column(db.Text)
	private_key = db.Column(db.Text)
	created = db.Column(db.DateTime, server_default=db.func.now())
	updated = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
