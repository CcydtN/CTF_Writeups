# zipzipzip
level: simple

## 1. Analysis
Try to unzip the file for few times using the string in `password.txt`
It easy to figure out it's a recursive zip file with descending number.
To solve the problem, we need to write a program to automate it.

## 2. Solve
```bash
#!env /bin/bash
set -euxo pipefail

function solve(){
  for ((i = 25000; i >= 0; i--))
  do
    unzip -o -P $(strings ./$i/password.txt) -d ./$(expr $i - 1) ./$i/zip-$i.zip
    rm -rf ./$(expr $i + 1)
  done
}

solve
```

To solve it, I write a simple bash script.
I assume the last zip have number 0 and write a for loop to solve it.
I am removing zip files at the end of the loop because the zips may occupy too much space.
The number `i+1` was pick, because I want to make sure there is at least one copy that can be unzipped, in case of any interrupt.