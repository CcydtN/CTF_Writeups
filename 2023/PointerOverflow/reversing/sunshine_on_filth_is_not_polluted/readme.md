# Problem
A binary files

# Hint
> Here's a hint, but you'll need to work for it a bit. Two hashed words: f704f57ea420275ad51bf55b7dec2c96 87cd8b8808600624d8c590cfc2e6e94b

To solve this hint, first download wordlist from [https://github.com/dwyl/english-words/blob/master/words.txt]
Then, execute the following command:
```bash
# https://hashcat.net/wiki/doku.php?id=rule_based_attack
echo ":\nc" > capitalize.rule # creating two rule, one do nothing, one capitalize

hashcat -a 0 -m 0 f704f57ea420275ad51bf55b7dec2c96 -r capitalize.rule words.txt
hashcat -a 0 -m 0 87cd8b8808600624d8c590cfc2e6e94b -r capitalize.rule words.txt
# f704f57ea420275ad51bf55b7dec2c96:Uninitialized
# 87cd8b8808600624d8c590cfc2e6e94b:variables
```
Hint is `Uninitialized variables`

# Solution
1. Starting from main
```c
undefined8 main(void)
{
    init();
    generate_code();
    configure_username();
    login();
    return 0;
}
```
2. Then, we can saw the following function with its disassembly
```c
// with jsdec
void generate_code(void)
{
    int64_t var_18h;
    int64_t var_14h;
    int64_t var_10h;
    int32_t var_ch;
    eax = rand ();
    var_ch = eax;
    var_10h = 0x2710;
    var_14h = 0x7b;
    edx = var_ch;
    eax = var_14h;
    eax += edx;
    edx:eax = (int64_t) eax;
    ax = dx:ax / var_10h;
    dx = dx:ax % var_10h;
    var_18h = edx;
    eax = edx;
    *(auth_code) = eax;
    return eax;
}
```
```c
// with Ghidra
void configure_username(void)
{
    int32_t iVar1;
    char *src;
    
    while( true ) {
        printf("Options: (1) Enter username, (2) Confirm username, (3) Done: ");
        iVar1 = get_int();
        if (iVar1 == 3) break;
        if (iVar1 < 4) {
            if (iVar1 == 1) {
                printf("Username: ");
                __isoc99_scanf("%15s", &src);
                strncpy(auth_username, &src, 0x10);
            } else if (iVar1 == 2) {RetDec
                printf("Current username is: %s\n", &src);
            }
        }
    }
    return;
}
```
```
generate_code();
; var int64_t var_18h @ stack - 0x18
; var int64_t var_14h @ stack - 0x14
; var int64_t var_10h @ stack - 0x10
; var int var_ch @ stack -     int32_t iVar1;
```
```
configure_username();
; var const char *src @ stack - 0x18
```
3. With all those information, we can figure `var_18h`(in `generate_code()`) and `src`(in `configure_username()`) is using the same address.

```c
    var_18h = edx;
    eax = edx;
    *(auth_code) = eax;
```
4. Because of these few line, we know `var_18h` is equal to `auth_code`
5. So we can print `auth_code` by Option 2.

Full code
```python
from pwn import *

bin = ELF("re3.bin")
context.binary = bin

def main():
    io = bin.process()
    # io = remote('34.123.210.162',20231)
    io.recv()
    io.sendline(b'2')
    io.recvuntil(b"is: ")
    code = u16(io.recv(2))
    print(code)
    io.recv()
    io.sendline(b'1')
    io.recv()
    io.sendline(b'admin')
    io.recv()
    io.sendline(b'3')
    io.recv()
    io.sendline(str(code).encode())
    io.interactive()

if __name__ == "__main__":
    main()
```