# Problem
Similar to `vigil_of_the_ceaseless_eyes`, get content from file `/.secret/flag.txt`

# Solution
1. Open terminal and enter the following code.
``` js
const response = await fetch("/Quantity/.secret/flag.txt");
// undefined
await response.text()
// 'poctf{uwsp_1_h4v3_70_1n5157}'
```
