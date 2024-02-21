from pwn import *

bin = ELF("aplet321")
context.binary = bin

def main():
    io = bin.process()
    io = remote('chall.lac.tf',31321)
    print(io.recv())
    io.sendline( b'pretty'*15 + b'please'*39+ b'flag')
    print(io.recv())
    print(io.recv()) # flag

if __name__ == "__main__":
    main()
