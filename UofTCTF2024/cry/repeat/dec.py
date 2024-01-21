from pwn import *

f = bytes.fromhex(open("flag.enc", "r").read().split(" ")[1])
key = xor(b'uoftctf{', f[0:8])
flag = bytes([f[i] ^ key[i % 8] for i in range(len(f))])
print(flag.decode())