# Solve
Use Chinese Remainder Thero

Solution:
```python
import libnum
from sympy.ntheory.modular import crt

moduli = [0 for _ in range(7)]
remainders = [0 for _ in range(7)]

with open("output.txt", "r") as file:
    for i in range(7):
        content = file.readline()
        pos = next(filter(str.isdigit, content), None)
        digit = content.find(pos)
        equal = content.find("=")
        moduli[i] = int(content[digit : equal - 1])
        remainders[i] = int(content[equal + 2 :])
print(moduli)
print(remainders)

e = 3

res = crt(moduli, remainders)
print(f"\nWe can solve M^e with CRT to get {res}")
val = libnum.nroot(res[0], e)
print(f"\nIf we assume e=3, we take the third root to get: {val}")
print("Next we convert this integer to bytes, and display as a string.")
print(f"\nDecipher: {val.to_bytes(100,'big').decode('utf-8')}")

```