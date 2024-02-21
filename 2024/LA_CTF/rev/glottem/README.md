# Glottem
> Haha glottem good!
> 
> Note: The correct flag is 34 characters long.

## Problem
### Shell
The code is as follow:
```sh
#!/bin/sh
1<<4201337
1//1,"""
exit=process.exit;argv=process.argv.slice(1)/*
4201337
read -p "flag? " flag
node $0 "$flag" && python3 $0 "$flag" && echo correct || echo incorrect
1<<4201337
*///""";from sys import argv
e = ['Note. a huge 3d array, please view it from source code']
alpha="abcdefghijklmnopqrstuvwxyz_"
d=0;s=argv[1];1//1;"""
/*"""
#*/for (let i = 0; i < s.length; i ++) {/*
for i in range(6,len(s)-2):
    #*/d=(d*31+s.charCodeAt(i))%93097/*
    d+=e[i-6][alpha.index(s[i])][alpha.index(s[i+1])]#*/}
exit(+(d!=260,[d!=61343])[0])
4201337
```
> It seem like markdown have the correct syntax highlighting.
> 
> The tools I use, like `vscode`,`helix`,`bat`, didn't highlight code correctly.

Start with the first line, the shebang state that the file is suppose to run as shell script.

Run with `bash -x glottem`, You will see it only run two lines.
```sh
read -p "flag? " flag
node $0 "$flag" && python3 $0 "$flag" && echo correct || echo incorrect
```
As `$0` means the same file. We know the same file is going to be pass in to `node` and `python3`.

Then copy and rename the file with extension `.js` and `.py`. Open them on a editor with syntax highlighting. You should see the following code.
> I rename them

After removing all the comment and unused code:
```js
exit = process.exit
argv = process.argv.slice(1)
d = 0
s = argv[1]
for (let i = 0; i < s.length; i++) {
    d = (d * 31 + s.charCodeAt(i)) % 93097
}
exit(+[d != 61343][0])
```
> To understand the last line, please check out [Comma operator]()
```py
from sys import argv
e = ['Note. a huge 3d array, please view it from source code']
alpha="abcdefghijklmnopqrstuvwxyz_"
d=0
s=argv[1]
for i in range(6,len(s)-2):
    d+=e[i-6][alpha.index(s[i])][alpha.index(s[i+1])]
exit(d!=260)
```
### The Goal
- make `node $0 $flag` exit with 0where `d == 61343`
- make the `python $0 $flag` exit with 0, where `d == 260`
- Given:
  - length of`flag` is 34

## Solve
To solve this problem, we need to start at `python` part.

### Python
The for loop count from [6, 32], length is 26.
```py
d, s =0, argv[1]
for i in range(6,len(s)-2):
    d+=e[i-6][alpha.index(s[i])][alpha.index(s[i+1])]
```

After that I start inspecting `e` and `alpha`
```python
print(len(e))           # 26
print(len(e[0]))        # 27
print(len(e[0][0]))     # 27

print(len(alpha))       # 27

for x in e:
    for y in x:
        for z in y:
            assert z >= 10
```
Cause every number in `e` is greater than 10.

In Order to make `d == 260`, `e[i][j][k]`  must equal to 10 with the correct flag.

Then, I worte a script to automate that.
```py
curr = {c:[c] for c in alpha}
next = {c:[] for c in alpha}
for i in range(26):
    for j in range(27):
        for k in range(27):
            if e[i][j][k] != 10:
                continue
            head, tail = alpha[j], alpha[k]
            next[tail].extend([ s+tail for s in curr[head]])
    curr = next
    next = {c:[] for c in alpha}

canidates = [ f"lactf{{{s}}}" for _,value in curr.items() for s in value ]
print(len(canidates))    # 42436
```
So there is `43436` canidates, to reduce the count, we need to start looking at JS part.

### Javascript
I rewrite the javascipt check in python and then apply filter to `canidates`
```py 
def js_check(s):
    assert len(s) == 34
    d = 0
    for c in s:
        d = (d*31 + ord(c)) % 93097
    return d == 61343

result = list(filter(js_check, canidates))
print(result) # ['lactf{solve_one_get_two_free_deal}']
```

There is only one result and thats the answer.

