# lock the lock
level: Medium

> You can create the environment your own. Here are the two package you needed:
> `pycryptodome decompyle3`
> In the repository, I use `nix` to set up, but others tools should be able to do the same thing.

## 1. Decompile pyc
This problem contain a `pyc` file, and required a bit reverse engineering.
By executing `decompyle3 -o ./ ./files/chall.pyc`, we can get the source code`chall.py`.

## 2. Analysis
The code can be separate into few parts, non-interactive UI, interactive UI, a simple self-balancing tree, and some other code.

If we get rid of the non-interactive UI and self-balance tree, we can have the follow code:
> Unable to run, but enough to explain the logic

```python
turn = 0
random.seed(199)

def main():
    class Node:
        # Node class for self-balance tree
    class lendis:
        # The self-balance tree
        def check(self, state, root, n, x):
            # state is useless
            # 'n' need to be a string form by '0','1', '0' means left, '1' means right
            # return True if 'n' equal to the path from 'root' to 'x'

    def decrypt(key, plain):
        # self explanatory

    def initialization():
        # initialization the tree
        # insert init in order

    def submit(root):
        global turn
        u = input()
        if not tr.check(0, root, u, target[turn]):
            turn = 0
            validatedkey.clear()
        else:
            validatedkey.append(u)
            turn += 1
        if turn == len(target):
            print(decrypt(validatedkey, FLAG))


    num = [i for i in range(1, 1001)]
    init = num.copy()
    random.shuffle(init)
    random.shuffle(init)
    random.shuffle(init)

    FLAG = [90,19,95,...]

    validatedkey = []
    tr, troot = initialization() # put init into tree

    target = init.copy()
    target.remove(troot.data)
    random.shuffle(target)

    while true:
        submit(troot)

if __name__ == '__main__':
    main()
```

## Solving the problem
Because random use a fixed seed, `init` and `target` have the same order for each run.
-> `initialize` always form the same tree.

To solve the puzzle, we need to have the correct `validatedkey`
-> achieve by enter the encoded path of `target[turn]` for `turn` form 0 to 999
-> can get by writing a new function, dfs over the tree
```python
answer = {}
def solve(root, val = ""):
    global answer
    answer[root.data] = val
    if root.l is not None:
        solve(root.l, val + "0")
    if root.r is not None:
        solve(root.r, val + "1")
```

## Putting piece together
By putting the `solve` function and modify the `submit` function.
The flag finally be obtained.
> The code is in `solution.py`
