def rc4(key, data):
    S = list(range(256))
    j = 0
    out = []

    # Convertir la clave a bytes
    if isinstance(key, str):
        key = [ord(c) for c in key]

    # KSA: Key Scheduling Algorithm
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    # PRGA: Pseudo-Random Generation Algorithm
    i = j = 0
    for char in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        out.append(char ^ K)

    return bytes(out)

hex_input = "b1fa38466a555b89c3a49726647f08aef67a6130a8fee5871a35e2bc4ac8d053b6a93e7095"
key = "21762"

cipher_bytes = bytes.fromhex(hex_input)
decrypted = rc4(key, cipher_bytes)

print(decrypted.decode('utf-8', errors='replace'))
