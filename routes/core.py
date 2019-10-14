# encryption and decryption
from flask import Blueprint, make_response, jsonify, request, abort
import base64
from handlers.encryption_handler import encrypt, decrypt

core = Blueprint("core", __name__)

@core.route("/encrypt", methods=["POST"])
def encrypt_route():
	json_data = request.json
	if not json_data:
		return make_response(jsonify({"error": "invalid json"}), 403)

	# expect base64 encoded data
	

	data = 0
	return make_response(jsonify({"data": data}), 200)


@core.route("/decrypt", methods=["GET", "POST"])
def decrypt_route():
	json_data = request.json
	if not json_data:
		return make_response(jsonify({"error": "invalid json"}), 403)

	temp_data = base64.b64decode(json_data["data"]).decode()
	key = temp_data[-10:]
	cipher_text = temp_data[:-10]

	plain_text = decrypt(cipher_text, key)
	data = {"data": plain_text}

	return make_response(jsonify({"data":data}), 200)

def sign():
	pass

def verify():
	pass