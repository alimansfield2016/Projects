import string

print('Please input string to encrypt / decrypt')
#rawinput(input_str)
input_str = input()
#print(input_str)
key = 0
while key == 0:
    print('Please input key.')
    print('To decrpyt, preceed with ''-''.')
    try:
        key = int(input())
    except ValueError:
        key = 0
#print(key)
if key < 0:
    key += 26
input_str = str.lower(input_str)
output_str = ''
for c in input_str:
    c = ord(c)
    #print(c)
    c += key
    if c > (96+26):
        c -= 26
    output_str = output_str + chr(c)
    #print(c)
    #print(chr(c))
    #print()
print(output_str)
