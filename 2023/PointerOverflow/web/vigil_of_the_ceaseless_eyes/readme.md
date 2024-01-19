# Problem
Load a `/secret/flag.pdf`

If we tried html injection, e.g. `<iframe src="https://nvstgt.com/ManyKin/secret/flag.pdf">`
It show error, "Failed to load PDF document".

# Solution
The error means that the file exist, but the content may be corrupted.
So just download it and see whats wrong
`wget https://nvstgt.com/ManyKin/secret/flag.pdf`
