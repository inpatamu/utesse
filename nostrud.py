import hashlib

def calculate_file_hash(filename):
    # Create a hash object
    sha256_hash = hashlib.sha256()
    
    # Open file in binary mode and read chunks
    with open(filename, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    
    # Return the hexadecimal digest of the hash
    return sha256_hash.hexdigest()

# Example usage:
file_hash = calculate_file_hash("example.txt")
print(f"The SHA-256 hash of the file is: {file_hash}")
