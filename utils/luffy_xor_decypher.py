def xor_cipher(text_hex, key):
    # Manejar text como hexadecimal y convertirlo a bytes
    text_bytes = bytes.fromhex(text_hex)
    key_bytes = key.encode() # Convertir la clave a bytes

    # Aplicar XOR
    cipher_text = bytes([text_bytes[i] ^ key_bytes[i % len(key_bytes)] for i in range(len(text_bytes))])
    
    return cipher_text

if __name__ == "__main__":
    text = "747d76716d035007010a0405510357070803065757005205510a0155065001070105050509"
    key = "21762"
    result = xor_cipher(text, key)
    print(result.decode(encoding='utf-8'))
