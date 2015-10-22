import binascii

__author__ = 'Przemysław Zamorski'
__description__ = 'Pierwsze zadanie suma parzystości bodajże '
binary=[]
counter=0
text = open('test.txt', 'r').read()
binary=(' '.join(format(ord(x), 'b') for x in text))


for bin in binary:
    if (bin==1):
        counter+=1
print(binary)
if counter%2:
    open('pierwsza_parzystosc', 'w').write("1")
else:
    open('pierwsza_parzystosc', 'w').write("0")

counter=0

# random function
binary_randomized=0

for bin in binary_randomize:
    if (bin==1):
        counter+=1

open('random.txt','w').write(binary_randomized)

if counter%2:
    open('druga_parzystosc.txt', 'w').write("1")
else:
    open('druga_parzystosc.txt', 'w').write("0")





with open('pierwsza_parzystosc.txt', 'r') as first:
    print(first)

with open('random.txt', 'r') as randomized:
    print(randomized)

with open('druga_parzystosc.txt', 'r') as second:
    print(second)


if ((second==first) and (randomized==binary)):
    print('pliki sa takie same')
else
    print('rozne pliki')





print(binary)






# 1 wczytaj binarnie
# 2 zapisz do listy
# 3 zsumuj 1 i zapisz jak jest parzysta 1 a jak nie 0
# 4 na tej liście zrób random change
# 5 wynik po randomie sumuje parzystość i sprawdzasz