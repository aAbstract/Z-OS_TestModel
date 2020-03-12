from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import random
import string
import base64

# this function generate two files one is the public key and the other is the private key
# each client must have his own public key
# id is in form of <client-id>_<his-role-in-the-system>
def generate_keys(id):
	modulus_length = 2048
	private_key = RSA.generate(modulus_length)
	public_key = private_key.publickey()
	with open ("keys/%s_private_key.pem"%(id), "w") as prv_file:
		print("{}".format(private_key.exportKey()), file=prv_file)
	with open ("keys/%s_public_key.pem"%(id), "w") as pub_file:
		print("{}".format(public_key.exportKey()), file=pub_file)

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

def rand_str_gen(len):
	return ''.join([random.choice(string.uppercase+string.lowercase) for x in range(len)])

# this function checks if the connected client is not a hacker
# recieved_encoded_encrypted_msg: the data recieved from the client after sending the random string to him
# id is in form of <client-id>_<his-role-in-the-system>
def validate(recieved_encoded_encrypted_msg, random_straing, client_id):
	try:
		key = RSA.importKey(open("keys/%s_private_key.pem"%(id), "rb"))
		if(decrypt_private_key(recieved_encoded_encrypted_msg) == random_string):
			return True
		else:
			return False
	except:
		return False

def check_clients(client_id):
	with open ("clients", "r") as clients_file:
		clients =  clients_file.read().split(',')
		if client_id in clients:
			return True
		else:
			return False

		

def apply_sec(socket_client, client_id):
	if check_clients(client_id):
		rand_str = rand_str_gen(8)
		socket_client.sendall(b'%s'%(rand_str))
		response = socket_client.recv(2048)
		if validate(response,rand_str,client_id):
			return True
		else:
			return False
	else:
		return False
