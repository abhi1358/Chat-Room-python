import hashlib

class SHA256:

	def generate_hash1(filename):
		with open(filename,"rb") as f:
    			bytes = f.read() # read entire file as bytes
    			readable_hash = hashlib.sha256(bytes).hexdigest();
    			#print(readable_hash)
    			return readable_hash

	def generate_hash2(filename):
		sha256_hash = hashlib.sha256()
		with open(filename,"rb") as f:
    	# Read and update hash string value in blocks of 4K
    		for byte_block in iter(lambda: f.read(4096),b""):
        		sha256_hash.update(byte_block)
    		#print(sha256_hash.hexdigest())
    		return sha256_hash.hexdigest()