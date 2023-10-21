# Guess My Number
level: simple

## Decompile
Using ghidra, we can get the following code:
```c
void vuln(void)
{
  int iVar1;
  
  key = 0;
  srand(0x539); // set random seed
  iVar1 = rand();
  printf("Your Guess : ");
  fflush(stdout);
  __isoc99_scanf(&DAT_001020cb,&key); // scanf
  if ((key ^ iVar1 + 0x1467f3U) == 0xcafebabe) {
    puts("Correct! This is your flag :");
    system("cat flag.txt"); // print the flag
    exit(0);
  }
  puts("Wrong, Try again harder!");
  return;
}

undefined8 main(void)
{
  flag_handler(); // check if file exist
  banner(); // printf a banner
  vuln();
  return 0;
}
```
In order to print the flag, we need to input a correct `key`.

## Finding the key
To find the key, we need to know two things: the value of `iVar1`, and C Operator Precedence.

### Value of `iVar1`
Since the program calls `srand(0x539)`, `iVar1` always get the same value.

> You can try by running this code. (If you are not familiar with c, put it into https://godbolt.org/ and run.)
> ```c
>int main(){
>    srand(0x539);
>    printf("%x", rand());
>}
>```

### C Operator Precedence
https://en.cppreference.com/w/c/language/operator_precedence
From the link above, we can know that '+' execute first, then '^'.
So the condition can be rewritten as `key ^ (iVar1 + 0x1467f3U) == 0xcafebabe`.
Furthermore, `key == (0xcafebabe) ^ (iVar1 + 0x1467f3U)`

## Solution
```c
int main(){
    srand(0x539);
    int key = (0xcafebabe) ^ (rand() + 0x1467f3U);
    printf("%d", key); // -612639902
    printf("%u", key); // 3682327394
}
```

```
$ nc ctf.tcp1p.com 7331

=======              WELCOME TO GUESSING GAME               =======
======= IF YOU CAN GUESS MY NUMBER, I'LL GIVE YOU THE FLAG  =======

Your Guess : -612639902
TCP1P{r4nd0m_1s_n0t_th4t_r4nd0m_r19ht?_946f38f6ee18476e7a0bff1c1ed4b23b}
Correct! This is your flag :


$ nc ctf.tcp1p.com 7331

=======              WELCOME TO GUESSING GAME               =======
======= IF YOU CAN GUESS MY NUMBER, I'LL GIVE YOU THE FLAG  =======

Your Guess : 3682327394
TCP1P{r4nd0m_1s_n0t_th4t_r4nd0m_r19ht?_946f38f6ee18476e7a0bff1c1ed4b23b}
Correct! This is your flag :
```