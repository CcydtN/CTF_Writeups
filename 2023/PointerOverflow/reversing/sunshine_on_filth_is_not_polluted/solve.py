from pwn import *

bin = ELF("re3.bin")
context.binary = bin

def main():
    io = bin.process()
    # io = remote('34.123.210.162',20231)
    io.recv()
    io.sendline(b'2')
    io.recvuntil(b"is: ")
    code = u16(io.recv(2))
    print(code)
    io.recv()
    io.sendline(b'1')
    io.recv()
    io.sendline(b'admin')
    io.recv()
    io.sendline(b'3')
    io.recv()
    io.sendline(str(code).encode())
    io.interactive()

if __name__ == "__main__":
    main()
