# shattered-memories
> I swear I knew what the flag was but I can't seem to remember it anymore... can you dig it out from my inner psyche?

## Problem
With cutter and ghidra, and some adjust the variable type. I have the follow main function:
``` c
undefined8 main(void)
{
    int32_t iVar1;
    int32_t iVar2;
    int32_t iVar3;
    int32_t iVar4;
    int32_t iVar5;
    int64_t iVar6;
    undefined8 uVar7;
    char s1 [132];
    uint64_t var_ch;
    
    puts("What was the flag again?");
    fgets(s1, 0x80, _stdin);
    strip_newline(s1);
    iVar6 = strlen(s1);
    if (iVar6 == 0x28) {
        iVar1 = strncmp(s1 + 8, "t_what_f", 8);
        iVar2 = strncmp(s1 + 0x20, "t_means}", 8);
        iVar3 = strncmp(s1 + 0x18, "nd_forge", 8);
        iVar4 = strncmp(s1, "lactf{no", 8);
        iVar5 = strncmp(s1 + 0x10, "orgive_a", 8);

        switch((iVar1 == 0) + (iVar2 == 0) + (iVar3 == 0) + (iVar4 == 0) + (iVar5 == 0)) {
            // The only case that need to be cared is 5
            // where every substring equal to the target
        }
    } else {
        puts("No, I definitely remember it being a different length...");
        uVar7 = 1;
    }
    return uVar7;
    }
}
```
Goal:
- `strlen(s1) == 0x28 // (dec: 40)`
- `s1` contain certain substring.

## Solve
Just reorder the `strncmp` according to `s1 + [offset]`.
```c
iVar4 = strncmp(s1, "lactf{no", 8);
iVar1 = strncmp(s1 + 8, "t_what_f", 8);
iVar5 = strncmp(s1 + 0x10, "orgive_a", 8);
iVar3 = strncmp(s1 + 0x18, "nd_forge", 8);
iVar2 = strncmp(s1 + 0x20, "t_means}", 8);
```
Concat the string, and that's the flag.

The flag: `lactf{not_what_forgive_and_forget_means}`
