from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes  # pycryptodome




def chacha20_encrypt(plaintext, user_id):
    key, nonce = generate_key_nonce(user_id=user_id)
    cipher = ChaCha20.new(key=key, nonce=nonce)
    ciphertext = cipher.encrypt(plaintext.encode())
    return ciphertext

def nami_cipher(plaintext, user_id):
    ciphertext = chacha20_encrypt(plaintext, user_id)
    return ciphertext

def generate_key_nonce(user_id):
    key = (user_id.encode() * 32)[:32]  # Derivar clave de 256 bits del ID
    nonce = (user_id.encode() * 8)[:8]  # Derivar nonce de 64 bits del ID
    return key, nonce

def chacha20_decrypt(ciphertext, user_id):
    key, nonce = generate_key_nonce(user_id=user_id)
    cipher = ChaCha20.new(key=key, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.decode()


if __name__ == "__main__":
    user_id = "21762"
    cipherFlag = "27a0a7a58ed44ddbfbd5e72b8761398a38f59ed91d503ab839b2902a04bf6c902e2a7a21f7"
    flag = chacha20_decrypt(bytes.fromhex(cipherFlag), user_id)
    print(flag)