# Problem
I found this old VeraCrypt container in my cloud drive. Can't for the life of me remember the password, but I'm sure you can figure out a way. All I remember is that I had a song stuck in my head when I was last working with the volume. How did it go?... "...playing in the street gonna be a big man someday"

HINT: The password is alphanumeric (A-Z, a-z, 0-9), contains no special characters, and the first three characters are gUn.

# Hint
- The file is a VeraCrypt container
- The password is alphanumeric (A-Z, a-z, 0-9), contains no special characters, and the first three characters are gUn.

# Solution
1. Guess the password.
  1. `cat /usr/share/dict/rockyou.txt | rg "^gUn` show only one result `gUnGNmZg6E6x0k1RgrkS`
2. mount the image with veracrypt using the password
``` shell
sudo mkdir /mnt/tmp
sudo veracrypt --text --password gUnGNmZg6E6x0k1RgrkS crack3 /mnt/tmp
# there is prompt asking PIM, keyfile, Protect hidden volume, just press enter 3 times
```
3. use `cat /mnt/tmp/flag.txt` to get flag

flag: `poctf{uwsp_qu4n717y_15_n07_4bund4nc3}`

# Clean up
```bash
sudo veracrypt --dismount /mnt/tmp
sudo rm /mnt/tmp
```
