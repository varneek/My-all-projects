import random 

lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punc= '''!#$%&'()*+,-./:;<=>?@[]"^_`{|}~'''
num = '0123456789'

pass_gen = []

for i in range(3):
    pass_gen.extend(lowercase)
    pass_gen.extend(uppercase)
    pass_gen.extend(punc)
    pass_gen.extend(num)

random.shuffle(pass_gen)

print('your secure password is:-', end=' ')
for i in range(20):
    print(pass_gen[i],end='')
