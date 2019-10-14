# main file
from flask import Flask, jsonify, abort, make_response
from db import db

def _init_blueprints(application):
	import handlers.error_handler as error_handler
	import routes.core as core
	
	application.register_blueprint(error_handler.error)
	application.register_blueprint(core.core)


def create_application():
	app = Flask(__name__)
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

	_init_blueprints(app)

	db.init_app(app)
	return app

if __name__=="__main__":
	app = create_application()	# app object init all blueprints in this function.

	
	@app.route("/health_check", methods=["GET"])
	def health_check():
		return abort(404)

	app.run(debug=True)