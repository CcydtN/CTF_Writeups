# Problem
A pdf file

# Solution
1. extracting flag by execute `strings DF1.pdf`
> poctf(uwsp_77333163306D335F37305F3768335F39346D33}
2. Use python to convert strings from hex
```python
>>> bytes.fromhex("77333163306D335F37305F3768335F39346D33")
b'w31c0m3_70_7h3_94m3'
```
3. Fix the left bracket
> poctf{uwsp_w31c0m3_70_7h3_94m3}
