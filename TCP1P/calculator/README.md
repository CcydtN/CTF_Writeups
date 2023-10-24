# Calculator
The problem is almost identical to "Math jail" in monthly challenges from intigriti.

The author did a great write-up on his blog, I will skip explaining the problem.
[English Version](https://blog.huli.tw/2023/08/29/en/intigriti-0823-author-writeup/)
[Tranditional Chinese Version](https://blog.huli.tw/2023/08/29/intigriti-0823-author-writeup/#%E5%BE%97%E5%88%B0%E7%A9%BA%E5%AD%97%E4%B8%B2)

## Different from Intigriti's challenge
||"Math Jail"| This challenge|
|---|---|---|
| Environment | browser | deno server |
| Goal | execute alert | trigger read file and return payload|

## Environment
This challenge use `deno`, and the server add some code to solve the permission issue. `isolation.js` and `worker.js`, but the challenge is basically the same.

By reading the Dockerfile, a command can be found to set up the server `deno run -A --no-prompt --unstable main.js`

## Goal
This challenge has a different goal, but the exploit is the same. So modifying the payload should be enough to complete the challenge.
The payload I used:
```return Deno.readTextFileSync("/flag.txt")```
- `Deno.readTextFileSync` should be self-explainable.
- `return` is used, so the `eval` in server return the flag instead of none object.

## Solution
The full solution is saved as `./solution.js`, I add some new codes to send the request in the same file. It can be executed with the command `deno run -A --no-prompt --unstable solution.js`.

You can test the whole challenge in local with the following step:
1. unzip `dist.zip` and cd to the output folder
2. run server with `deno run -A --no-prompt --unstable main.js`
3. cd back to this folder run solution with `deno run -A --no-prompt --unstable solution.js`

