#!/usr/bin/env python

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# from Crypto.PublicKey import RSA
# private_key = RSA.generate(1024)
# public_key = private_key.publickey()
# print(private_key.exportKey(format='PEM'))
# print(public_key.exportKey(format='PEM'))

# with open ("private.pem", "w") as prv_file:
#     print("{}".format(private_key.exportKey()), file=prv_file)

# with open ("public.pem", "w") as pub_file:
#     print("{}".format(public_key.exportKey()), file=pub_file)

def generate_keys():
	modulus_length = 2048
	key = RSA.generate(modulus_length)
	#print (key.exportKey())
	pub_key = key.publickey()
	#print (pub_key.exportKey())
	open('keys')
	#return key, pub_key

def encrypt_public_key(a_message, public_key):
	encryptor = PKCS1_OAEP.new(public_key)
	encrypted_msg = encryptor.encrypt(a_message)
	#print(encrypted_msg)
	encoded_encrypted_msg = base64.b64encode(encrypted_msg)
	#print(encoded_encrypted_msg)
	return encoded_encrypted_msg

def decrypt_private_key(encoded_encrypted_msg, private_key):
	encryptor = PKCS1_OAEP.new(private_key)
	decoded_encrypted_msg = base64.b64decode(encoded_encrypted_msg)
	#print(decoded_encrypted_msg)
	decoded_decrypted_msg = encryptor.decrypt(decoded_encrypted_msg)
	#print(decoded_decrypted_msg)
	return decoded_decrypted_msg

def main():
	private, public = generate_keys()
	#print (private)
	message = b'Hello world'
	encoded = encrypt_public_key(message, public)
	a =  decrypt_private_key(encoded, private)
	print(a)


main()	