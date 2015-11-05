import random

__author__ = 'Przemysław Zamorski'
__description__ = 'Pierwsze zadanie suma parzystości bodajże '

file = ''

# wczytanie pliku do wersji binarnej i zliczenie bitów
with open('test.txt', 'rb') as f1:
    while True:
        bytes = f1.read(1024)
        if bytes:
            for byte in bytes:
                file = ''.join((file, bin(byte)))
        else:
            break
print('plik bez parzystosci', file)

#funkcja parzystości
def parzystosc(plik):
    counter = 0
    parz = 0
    for x in plik:
            if x == '1':
                counter += 1
    if (counter % 2 == 0):
        parz = '0'
    else:
        parz = '1'
    return parz

#random funkcja zamienic na replece i zabezpieczyc sie przed b
def moj_random(plik):
    # for petla in range(0,2): #petla dla zmiany 2 znakow
    for petla in range(random.randint(0, 20)): #petla dla randowowej liczby znakow
        pos = random.randint(0, len(plik) - 1)
        print('pos-',pos)
        if plik[pos] == '1':
            plik = plik[:pos] + "0" + plik[pos + 1:]
        else:
            plik = plik[:pos] + "1" + plik[pos + 1:]
    return plik

#zliczenie 1 parzystosci
file+=parzystosc(file)
print('plik  z  parzystosci', file)
second_file = open('pierwsza_parzystosc.txt', 'w')
second_file.write(file)
second_file.close()

#wykonanie randoma
file = moj_random(file)
print('plik  po   losowaniu', file)
random_file = open('random.txt', 'w')
random_file.write(file)
random_file.close()


if parzystosc(file[:len(file)-1]) == file[len(file)-1:]:
    print('jest ok')
else:
    print('Nope - nie sa takie same')













