import os
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidTag

def derive_key(master_password: str, salt: bytes) -> bytes:
    """Derive a 32-byte key from master password using Scrypt"""
    kdf = Scrypt(
        salt=salt,
        length=32,
        n=2**2,  # CPU/memory cost parameter
        r=8,      # Block size parameter
        p=1       # Parallelization parameter
    )
    return kdf.derive(master_password.encode())

def encrypt_password(master_password: str, password: str) -> str:
    """Encrypt a password using master password"""
    salt = os.urandom(16)
    key = derive_key(master_password, salt)
    
    # Generate a random 96-bit nonce
    nonce = os.urandom(12)
    
    # Encrypt using AES-GCM
    cipher = Cipher(
        algorithms.AES(key),
        modes.GCM(nonce),
    )
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(password.encode()) + encryptor.finalize()
    
    # Combine salt + nonce + ciphertext + tag
    encrypted_data = salt + nonce + ciphertext + encryptor.tag
    return base64.b64encode(encrypted_data).decode('utf-8')

def decrypt_password(master_password: str, encrypted_data: str) -> str:
    """Decrypt a password using master password"""
    try:
        data = base64.b64decode(encrypted_data)
        salt = data[:16]
        nonce = data[16:28]
        ciphertext = data[28:-16]
        tag = data[-16:]
        
        key = derive_key(master_password, salt)
        
        # Decrypt using AES-GCM
        cipher = Cipher(
            algorithms.AES(key),
            modes.GCM(nonce, tag),
        )
        decryptor = cipher.decryptor()
        password = decryptor.update(ciphertext) + decryptor.finalize()
        
        return password.decode('utf-8')
    except (InvalidTag, ValueError) as e:
        return 'error during decryption'

# Example usage
if __name__ == "__main__":
    # Encrypt a password
    master_pw = "MySuperSecretMasterPassword123!"
    user_password = "s3cr3tUs3rP@ssw0rd"
    
    encrypted = encrypt_password(master_pw, user_password)
    print(f"Encrypted: {encrypted}")
    
    # Decrypt it back
    try:
        decrypted = decrypt_password(master_pw, encrypted)
        print(f"Decrypted: {decrypted}")
    except ValueError as e:
        print(f"Error: {e}")