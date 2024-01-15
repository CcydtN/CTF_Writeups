# My solution
index.php:127
``` php
if((int)$row[1] == $mysupersecurehash && $mysupersecurehash == 0e0776470569150041331763470558650263116470594705){
```

This line is going to pass when `$mysupersecurehash` equal to 0

So I found a value that has hash start with `0eXXXXXXXXX...` and can be identify as 0

The last step is kind of brute-force, I send all 500 admin with the same password. One of them will return the flag.

# Better solution
use SQL injection using with the GET request
https://github.com/Lyther/Backdoor-CTF-2023-Writeups/blob/main/web/too-many-admins/README.md

https://medium.com/@pradyun/backdoor-ctf-writeup-6c89a34fd319
