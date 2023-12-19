Problem
 - check extension if it equal to \[jpg, jpeg, png\]
 - check binary header if it equal to ...

Interesting point
 - `$filename = strtok($filename, chr(...))` which `chr(...)` is `$`

make a file with binary header of image format
jpg = "ff d8 ff e0"
rename it with "anytext.php$.jpg"

