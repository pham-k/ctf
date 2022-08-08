code = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'
s = "91 322 57 124 40 406 272 147 239 285 353 272 77 110 296 262 299 323 255 337 150 102"
print('picoCTF{' + ''.join([code[int(x) % 37] for x in s.split(" ")]) + '}')
