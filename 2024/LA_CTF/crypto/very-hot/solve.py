from Crypto.Util.number import long_to_bytes
import math

n = 10565111742779621369865244442986012561396692673454910362609046015925986143478477636135123823568238799221073736640238782018226118947815621060733362956285282617024125831451239252829020159808921127494956720795643829784184023834660903398677823590748068165468077222708643934113813031996923649853965683973247210221430589980477793099978524923475037870799
e = 65537
ct = 9953835612864168958493881125012168733523409382351354854632430461608351532481509658102591265243759698363517384998445400450605072899351246319609602750009384658165461577933077010367041079697256427873608015844538854795998933587082438951814536702595878846142644494615211280580559681850168231137824062612646010487818329823551577905707110039178482377985

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

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_gcd(b, a % b)
        return d, y, x - (a // b) * y

def mod_inverse(e, phi_n):
    gcd, x, y = extended_gcd(e, phi_n)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    else:
        return x % phi_n

p = binary_search(n)
q = p + 6
r = p + 12

phi_n = math.lcm(p-1, q-1, r-1)
d = mod_inverse(e, phi_n)

print(d)
m = pow(ct, d, n)

message = long_to_bytes(m).decode()
print(message)
