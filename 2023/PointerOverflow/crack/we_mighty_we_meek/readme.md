# Problem
A password protected excel file

# My solution
1. rename the file `cp crack1.excel crack.xlsx`
2. crack password with `hashcat` and a filtered rockyou word list
```
python office2hashcat.py crack1.excel > hash.txt
rg "^[a-zA-z]+\$" /usr/share/dict/rockyou.txt | hashcat -m 9600 -a 0 hash.txt
```
password is `hsppyhsppyjoyjoy`
3. Open it and the flag is there.`poctf{uwsp_j3_p3n53_d0nc_j35_5u15}`
