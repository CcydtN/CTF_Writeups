import string

knowns = {
    # cipher: original
    "bkvim": "lactf",
    "Lzfqztk": "bendera",
    "wzbkdki": "selamat",
    "ckse": "pagi",
    "x": "h",
    "a": "y",
    "u": "k",
    "j": "u",
}

def monoalphabetic_substitution(ciphertext, substitution_key):
    plaintext = []
    for char in ciphertext:
        if not char.isalpha():
            plaintext.append(char)
            continue

        if char not in substitution_key:
            plaintext.append('*')
            continue

        plaintext.append(substitution_key[char])
    return ''.join(plaintext)

substitution_key = {}
for key,value in knowns.items():
    key = key.lower()
    value = value.lower()
    assert len(key) == len(value)
    for i in range(len(key)):
        a,b = key[i], value[i]
        # check if it already exist
        if a in substitution_key:
            assert substitution_key[a] == b
            continue
        substitution_key.update({a:b, a.upper():b.upper()})

missing_key = set([ c for c in string.ascii_lowercase if c not in substitution_key.keys()])
missing_value = set([ c for c in string.ascii_lowercase if c not in substitution_key.values()])
assert len(missing_key) == len(missing_value)

with open('message.txt', 'r') as file:
    ciphertext = file.read()
decrypted_text = monoalphabetic_substitution(ciphertext, substitution_key)

print("---")
print(ciphertext)
print("---")
print(decrypted_text)
print("---")