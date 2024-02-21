# aplet321
> Unlike Aplet123, Aplet321 might give you the flag if you beg him enough.
> 
> `nc chall.lac.tf 31321`

## Problem
With cutter and ghidra, we can have the follow main function:
```c
undefined8 main(void)
{
    int32_t iVar1;
    uint64_t uVar2;
    int64_t iVar3;
    int64_t *piVar4;
    int32_t iVar5;
    int32_t iVar6;
    char *s1;
    int64_t var_238h;
    
    // [14] -r-x section size 553 named .text
    setbuf(_stdout, 0);
    puts("hi, i\'m aplet321. how can i help?");
    fgets(&var_238h, 0x200, _stdin);
    uVar2 = strlen(&var_238h);
    if (5 < uVar2) {
        iVar5 = 0;
        iVar6 = 0;
        piVar4 = &var_238h;
        do {
            iVar1 = strncmp(piVar4, "pretty", 6);
            iVar6 = iVar6 + (uint32_t)(iVar1 == 0);
            iVar1 = strncmp(piVar4, "please", 6);
            iVar5 = iVar5 + (uint32_t)(iVar1 == 0);
            piVar4 = (int64_t *)((int64_t)piVar4 + 1);
        } while (piVar4 != (int64_t *)((int64_t)&var_238h + (uint64_t)((int32_t)uVar2 - 6) + 1));
        if (iVar5 != 0) {
            iVar3 = strstr(&var_238h, "flag");
            if (iVar3 == 0) {
                puts("sorry, i didn\'t understand what you mean");
                return 0;
            }
            if ((iVar6 + iVar5 == 0x36) && (iVar6 - iVar5 == -0x18)) {
                puts("ok here\'s your flag");
                system("cat flag.txt");
                return 0;
            }
            puts("sorry, i\'m not allowed to do that");
            return 0;
        }
    }
    puts("so rude");
    return 0;
}
```

The code can be view as two session:
- do-while loop
- variable checking

### do-while loop
```c
do {
    iVar1 = strncmp(piVar4, "pretty", 6);
    iVar6 = iVar6 + (uint32_t)(iVar1 == 0);
    iVar1 = strncmp(piVar4, "please", 6);
    iVar5 = iVar5 + (uint32_t)(iVar1 == 0);
    piVar4 = (int64_t *)((int64_t)piVar4 + 1);
} while (piVar4 != (int64_t *)((int64_t)&var_238h + (uint64_t)((int32_t)uVar2 - 6) + 1));
```
This part scan the string, and count the number of substring that match `pretty` or `please`.

Storing count of `pretty` in iVar6, and `please` in iVar5.

### value checking
```c
if (iVar5 != 0) {
    iVar3 = strstr(&var_238h, "flag");
    if (iVar3 == 0) {
        puts("sorry, i didn\'t understand what you mean");
        return 0;
    }
    if ((iVar6 + iVar5 == 0x36) && (iVar6 - iVar5 == -0x18)) {
        puts("ok here\'s your flag");
        system("cat flag.txt");
        return 0;
    }
    puts("sorry, i\'m not allowed to do that");
    return 0;
}
```
This part check the value of `iVar5`, `iVar6` and `var_238h`(the input buffer). Here are the required value/content in order to print the flag:
- iVar5 !=0
- iVar6 + iVar5 == 0x36
- iVar6 - iVar5 == -0x18
- iVar3 != 0 
  - a.k.a. `var_238h`(input) contain substring `flag`


# Solve
The thing we need to do is generate the required string for input.

Here is a python script for that:
```python
from pwn import *

bin = ELF("aplet321")
context.binary = bin

def main():
    io = bin.process()
    io = remote('chall.lac.tf',31321)
    print(io.recv())
    io.sendline(b'flag' +b'pretty'*15 + b'please'*39)
    print(io.recv())
    print(io.recv()) # flag

if __name__ == "__main__":
    main()
```
