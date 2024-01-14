#!env /bin/bash
set -euxo pipefail

function solve(){
  for ((i = 25000; i >= 0; i--))
  do
    unzip -o -P $(strings ./$i/password.txt) -d ./$(expr $i - 1) ./$i/zip-$i.zip
    rm -rf $(expr $i + 1)
  done
}

mkdir -p 25000
cp -r ./files/* ./25000/
solve
