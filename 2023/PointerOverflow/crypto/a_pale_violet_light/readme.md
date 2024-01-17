# Problem
Given the following numbers, solve the RSA encryption.
e = 5039
N = 34034827
C = 933969 15848125 24252056 5387227 5511551 10881790 3267174 14500698 28242580 933969 32093017 18035208 2594090 2594090 9122397 21290815 15930721 4502231 5173234 21290815 23241728 2594090 21290815 18035208 10891227 15930721 202434 202434 21290815 5511551 202434 4502231 5173234 25243036

# solution
```python
from Crypto.Util.number import long_to_bytes
import subprocess
import os

e = 5039
N = 34034827
C = [933969,15848125,24252056,5387227,5511551,10881790,3267174,14500698,28242580,933969,32093017,18035208,2594090,2594090,9122397,21290815,15930721,4502231,5173234,21290815,23241728,2594090,21290815,18035208,10891227,15930721,202434,202434,21290815,5511551,202434,4502231,5173234,25243036]
# C = long_to_bytes(C)
C = map(str,C)
C = ",".join(C)

temp_file = f"{os.getcwd()}/tmp.txt"
if os.path.exists(temp_file):
    os.remove(temp_file)

command = ["rsactftool", "--decrypt", C, "-e", f"{e}", "-n", f"{N}", "--output", temp_file]
subprocess.run(command)

with open("./tmp.txt", "rb") as file:
    content=file.read()
    print(content.decode().replace(" ", "_"))

os.remove(temp_file)
```
flag: `poctf{uwsp_533k_4nd_y3_5h411_f1nd}`
