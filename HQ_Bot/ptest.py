s = 'sfdsf\nsdfnsk'
print('\n' in s)
s = s.replace('\n', ' ')
print (s)
a= hex(0xfb01)
print (a)


# 
# import binascii
# 
# x = b'test'
# x = binascii.hexlify(x)
# y = str(x,'ascii')
# 
# print(x) # Outputs b'74657374' (hex encoding of "test")
# print(y) # Outputs 74657374
# 
# x_unhexed = binascii.unhexlify(0xfb01)
# print(x_unhexed) # Outputs b'test'
# 
# x_ascii = str(x_unhexed,'ascii')
# print(x_ascii) # Outputs test






BAD_READ_HEX_CHARS_REPLACE_D = {'fb01': 'fi'}

print('fb01' in BAD_READ_HEX_CHARS_REPLACE_D.keys())




