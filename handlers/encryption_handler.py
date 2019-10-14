from models import Key
import random

KEY_MAX = 100

def encrypt(data):
	key_id = random.randint(1, KEY_MAX)

	key = Key.query.get(key_id)
	cipher_text = ""
	return cipher_text

def decrypt(cipher_text, key):
	plain_text = ""

	return plain_text