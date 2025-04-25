def xor_cipher(text, key):
    # Convertir tanto el texto como la clave a bytes
    if type(text) == str:
        text_bytes = text.encode()
    else:
        text_bytes = text
    key_bytes = key.encode()  # Convertir la clave a bytes

    # Cifrar con XOR
    cipher_text = bytes([text_bytes[i] ^ key_bytes[i % len(key_bytes)] for i in range(len(text_bytes))])
    
    return cipher_text

if __name__ == "__main__":
    text = "747d76716d035007010a0405510357070803065757005205510a0155065001070105050509"
    key = "21762"
    print(xor_cipher(text, key))