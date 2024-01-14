# Problem
Incorrect header

## How to figure out
1. Look at the hex dump and compare the different
   
   `hexyl chal.png | head`
2. compare the hex with [png header](https://en.wikipedia.org/wiki/PNG#Examples)
3. `IHDR`, `IDAT`, `IEND` can be found using

   `hexyl chal.png | rg [IHDR/IDAT/IEND]`
5. So the only things missing is PNG signature

# Solve
Fixing the signature with python

Image show a bad handwritting, but enough to guess some char
s and 8, g and 9 can be easily mix up

`flag{sp3ll_15_89_50_4E_47}`
