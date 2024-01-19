# Solution
```
####
# TODO: use strong password
# Canadian_Soap_Opera
###
```
This comment give us the password alreadly

Just run the script and enter `Canadian_Soap_Opera`
I created a Dockerfile for this purpose
To use the dockerfile:
```
docker build -t mypowershellscript .
docker run -it --rm mypowershellscript
```

```
(Case Sensitive) Please Enter User Password: Canadian_Soap_Opera
Encrypted Password is: TTpgx3Ve2kkHaFNfixbAJfwLqTGQdk9dkmWJ6/t0UCBH2pGyJP/XDrXpFlejfw9d

Testing Decryption of Username / Password...

Decrypted Password is: poctf{uwsp_4d_v1c70r14m_w4573l4nd3r}
```
