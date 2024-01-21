# Problem
Here's a password protected archive. Problem is that I seem to have forgotten das Passwort. All I have is this post-it note on my monitor that says "crack2 = 4bd939ed2e01ed1e8540ed137763d73cd8590323"

# Hint
There are two hint in the password
- crack2 = 4bd939ed2e01ed1e8540ed137763d73cd8590323
- "dat Passwort" which is german

# Solution
1. download this [word list](https://gist.github.com/MarvinJWendt/2f4f4154b8ae218600eb091a5706b5f4)
2. solve it using hashcat. `hashcat -m 100 -a 0 4bd939ed2e01ed1e8540ed137763d73cd8590323 ./wordlist-german.txt`
3. The password is `zwischen`. unzip with `7za x crack2.7z`
3. The zip contain 2023 folder. here is a diagram of `tree`/`exa --tree 2023`
```shell
> exa --tree
└── p
   └── o
      └── c
         └── t
            └── f
               └── {uwsp_
                  └── c
                     └── 4
                        └── 1
                           └── 1
                              └── f
                                 └── 0
                                    └── 2
                                       └── n
                                          └── 1
                                             └── 4_
                                                └── d
                                                   └── 2
                                                      └── 3
                                                         └── 4
                                                            └── m
                                                               └── 1
                                                                  └── n
                                                                     └── 9
                                                                        └── }
```
flag is `poctf{uwsp_c411f02n14_d234m1n9}`
