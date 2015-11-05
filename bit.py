import random

__author__ = 'Przemysław Zamorski'
__description__ = 'Pierwsze zadanie suma parzystości bodajże '

counter=0
file=''

#wczytanie pliku do wersji binarnej i zliczenie bitów

with open('test.txt', 'rb') as f1:
    while True:
        bytes = f1.read(1024)
        if bytes:
            for byte in bytes:
                file=''.join((file,bin(byte)))
        else:
            break

for x in file:
    if x== '1':
        counter+=1

print('plik bez parzystosci',file)


#sprawdzenie czy jest parzyste i dodanie oraz zapisanie w pliku
if (counter%2 == 0):
    file+='0';
else:
     file+='1';

print('plik  z  parzystosci',file)
second_file = open('pierwsza_parzystosc.txt', 'w')
second_file.write(file)
second_file.close()


#random funkcja zamienic na replece i zabezpieczyc sie przed b
def moj_random(plik):
    pos=random.randint(0,len(plik)-1)
    if plik[pos] == '1':
      plik=plik[:pos] +"0"+plik[pos+1:]
    else:
      plik=plik[:pos] +"1"+plik[pos+1:]
    return plik

#wykonanie randoma
file=moj_random(file)
print('plik  po   losowaniu', file)
random_file=open('random.txt', 'w')
random_file.write(file)
random_file.close()













# 1 wczytaj binarnie
# 2 zapisz do listy
# 3 zsumuj 1 i zapisz jak jest parzysta 1 a jak nie 0
# 4 na tej liście zrób random change
# 5 wynik po randomie sumuje parzystość i sprawdzasz

# #def get_random_noise():
#     # if random.randint(0, 100)==1:
#         pos = random.randint(0, 8)
#         return pos
#     # return 0
# tu masz losowanie pozycji a w komencie masz losowanie prawdopodobieństwa
# #
# # print(binary)