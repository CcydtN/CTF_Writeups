# very-hot
> I didn't think that using two primes for my RSA was sexy enough, so I used three.

## Problem
- a modified RSA encryption
- Hint:
  - `q = p + 6`
  - `r = p + 12`
  
## Solve

### Finding p
Because `n = p * q * r`, `q = p + 6` and `r = p + 12`
The range of `n` is [0, ( 2^(384)-1 ) ^ 3].

`p` can be found with binary_search, thus `q`, `r` is also know.
```python
def binary_search(target):
    left, right = 0, (2**(384) - 1)**3
    key = lambda x: x*(x+6)*(x+12)
    while left <= right:
        mid = (left + right) // 2
        # Check if target is present at mid
        tmp = key(mid)
        if tmp == target:
            return mid
        elif tmp < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

p = binary_search(n)
q = p + 6
r = p + 12
```

### Solve RSA
The remaining step is similar to normal RSA.
```python
from Crypto.Util.number import long_to_bytes

phi_n = math.lcm(p-1, q-1, r-1) # do with 3 variable instead of 2
d = mod_inverse(e, phi_n)
m = pow(ct, d, n)
message = long_to_bytes(m).decode()
print(message)
```