def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key_length = len(key)
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % key_length].upper()) - ord('A')
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            key_index += 1
        else:
            encrypted_char = char

        ciphertext += encrypted_char

    return ciphertext

def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key_length = len(key)
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % key_length].upper()) - ord('A')
            if char.islower():
                decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            else:
                decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            plaintext += decrypted_char
            key_index += 1
        else:
            plaintext += char

    return plaintext

def find_key(intro, ct):
    def find_key_char(m, c):
        if not m.isalpha():
            return None
        base = ord('a') if m.islower() else ord('A')
        a = ord(m) - base
        b = ord(c) - base
        shift = (b - a) % 26
        return chr(ord('A') + shift)

    assert len(intro) == len(ct)
    keys = [ find_key_char(intro[i], ct[i]) for i in range(len(intro)) ]
    keys = list(filter(lambda x: x is not None, keys))
    return "".join(keys)
    

with open("intro.txt", 'r') as file:
    intro = file.read()

with open("ct.txt", 'r') as file:
    ct = file.read()

key = find_key(intro, ct[:len(intro)])

key += "A" * (161 - len(key))

assert len(key) == 161
assert ct[:len(intro)] == vigenere_encrypt(intro,key)
assert intro == vigenere_decrypt(ct[:len(intro)], key)
print(vigenere_decrypt(ct, key))
