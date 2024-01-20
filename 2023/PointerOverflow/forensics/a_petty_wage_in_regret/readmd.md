# Problem
A pdf file

# Solution
1. execute this code to get the "User Comment in the image". `exiftool DF2.jpg | rg User`
> User Comment                    : 3A3A50312F323A3A20706F6374667B757773705F3768335F7730726C645F683464
2. Convert the hex to string with python
```python
>>> bytes.fromhex("3A3A50312F323A3A20706F6374667B757773705F3768335F7730726C645F683464")
b'::P1/2:: poctf{uwsp_7h3_w0rld_h4d'
```
3. With python and Chatgpt, a script `solve.py` is created to shapen the image even more to make the word clear
```
::P2/2:: 17_f1257
```
4. Combining those
`poctf{uwsp_7h3_w0rld_h4d_17_f1257}

