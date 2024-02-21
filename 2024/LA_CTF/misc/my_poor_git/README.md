# my poor git

## Problem
if we try to `git clone https://poor-git.chall.lac.tf/flag.git`, it fails.
We can try add `--depth [n]`, but can't clone with `n` > 2.
When `n`<=2, commit message and files didn't contain any flag.

My only assumption is that the flag is hidden in files or commit where `n` > 2, but 

So the problem is:
- Getting all commit and file without `git clone`

## Solve
According to git document, git support four protocol.

For this problem, we are using [http(s) protocol](https://www.git-scm.com/docs/http-protocol).

### Solve manually
``` bash
# clone the repo
git clone https://poor-git.chall.lac.tf/flag.git --depth 2

# look at the content of each file
# https://www.git-scm.com/book/en/v2/Git-Internals-Git-Objects
cd flag/.git/objects
git cat-file -p [hash]
git cat-file -p 741fa59ac9ec45f978d799bd88b7290bc304abdd

# Download the missing object with http(s).
# Some object fails, but that's expected. Otherwise, we can download the whole repo without any issue.
# Just continue with the next hash.
# Example:
mkdir 74
curl https://poor-git.chall.lac.tf/flag.git/objects/74/1fa59ac9ec45f978d799bd88b7290bc304abdd --output 74/1fa59ac9ec45f978d799bd88b7290bc304abdd

# Use `git cat-file` again for the content.
```

# Solve by script
[solve.py](./solve.py)