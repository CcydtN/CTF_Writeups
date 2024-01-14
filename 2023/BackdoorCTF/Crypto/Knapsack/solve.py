import random
import hashlib
from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Cipher import AES
import itertools
from tqdm import tqdm
import string

Ciphertext = bytes.fromhex(
    "af95a58f4fbab33cd98f2bfcdcd19a101c04232ac6e8f7e9b705b942be9707b66ac0e62ed38f14046d1cd86b133ebda9"
)
numbers = [
    600848253359,
    617370603129,
    506919465064,
    218995773533,
    831016169202,
    501743312177,
    15915022145,
    902217876313,
    16106924577,
    339484425400,
    372255158657,
    612977795139,
    755932592051,
    188931588244,
    266379866558,
    661628157071,
    428027838199,
    929094803770,
    917715204448,
    103431741147,
    549163664804,
    398306592361,
    442876575930,
    641158284784,
    492384131229,
    524027495955,
    232203211652,
    213223394430,
    322608432478,
    721091079509,
    518513918024,
    397397503488,
    62846154328,
    725196249396,
    443022485079,
    547194537747,
    348150826751,
    522851553238,
    421636467374,
    12712949979,
]
secret_sum = 7929089016814


def helper(secret):
    k = bytes_to_long(secret)
    s = 0
    for i in range(40):
        if k & (1 << i):
            s += numbers[i]
    return s


# characters = string.ascii_letters + string.digits + string.punctuation
characters = string.ascii_letters + string.digits
# characters = string.ascii_letters
for combination in tqdm(
    itertools.product(characters, repeat=5),
    total=len(characters) ** 5,
):
    word = "".join(combination).encode()
    current_sum = helper(word)
    if current_sum != secret_sum:
        continue

    key = hashlib.sha256(word).digest()[:16]
    cipher = AES.new(key, AES.MODE_ECB)
    tmp = cipher.decrypt(Ciphertext)
    if not all(0 <= byte <= 127 for byte in tmp):
        continue
    text = tmp.decode()
    if text.startswith("flag"):
        answer = (word, text)
        break

print()
print(answer)
