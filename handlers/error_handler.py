from flask import make_response, Blueprint, jsonify

error = Blueprint('error', __name__)

@error.app_errorhandler(404)
def not_found(error):
	return make_response(jsonify({'status':404, "error":"not_found"}), 404)


@error.app_errorhandler(403)
def forbidden(error):
	return make_response(jsonify({'status':403, "error": "forbidden"}))

@error.app_errorhandler(400)
def forbidden(error):
	return make_response(jsonify({'status':400, "error": "bad request"}))