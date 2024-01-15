# Problem
 - check extension if it equal to \[jpg, jpeg, png\]
 - check binary header if it is allow

Interesting point
 - `$filename = strtok($filename, chr(...))` which `chr(...)` is `$`
 - This line will change the saved name

# Solution
1. Create a php file, which will return a flag

2. Insert image binary signture at the begining of the file
> jpg = "ff d8 ff e0"

3. Rename it so the saved name ends with `.php`, but the upload name ends with `.jpg`

Check out `hack.php$.jpg`


