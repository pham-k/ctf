import Crypto.Util.number as crypto

s = '104 85 69 354 344 50 149 65 187 420 77 127 385 318 133 72 206 236 206 83 342 206 370'
code = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'

print('picoCTF{' + ''.join([code[crypto.inverse(int(x) % 41, 41) - 1] for x in s.split(' ')]) + '}')
