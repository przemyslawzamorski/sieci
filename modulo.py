import random

__author__ = 'Przemysław Zamorski'
__description__ = 'Pierwsze zadanie suma modulo'
##SUMA MODULO##
print('SUMA MODULO')

#funkcja robiacu sume modul
def suma_modulo(plik):
    summary=0
    for bytes in plik:
        summary+=bytes
    summary=summary % 134
    return summary

#funkca losujaca
def transfer(plik):
    pos = random.randint(0, len(plik) - 1)
    byte=plik[pos]
    print('wylosowany bajt decymalnie ',byte)
    byte_binary=bin(byte)

    pos2=random.randint(0, len(byte_binary) - 1)
    if byte_binary[pos2] == '1':
            byte_binary = byte_binary[:pos2] + "0" + byte_binary[pos2 + 1:]
    elif byte_binary[pos] == '0':
            byte_binary = byte_binary[:pos2] + "1" + byte_binary[pos2 + 1:]
    else:
            pass
    changed_bit=int(byte_binary,2)
    print('wylosowany bajt decymalnie po transferze',changed_bit)
    plik[pos]=changed_bit
    print('plik po zmianach',plik)
    return plik





##glowny program
#wczytanie pliku do listy
file=[]
with open('test.txt', 'rb') as f1:
    while True:
        bytes = f1.read(1024)
        if bytes:
              for byte in bytes:
                file.append(byte)
        else:
            break
print('wczytany plik ', file)


suma_mod1=suma_modulo(file)
file =transfer(file)
suma_mod2=suma_modulo(file)
print('suma modulo przed przesylem ',suma_mod1)
print('suma modulo po   przeslaniu ',suma_mod2)

if suma_mod1 == suma_mod2:
    print('pliki po transferze zgadzaja sie')
else:
    print('pliki po transferze nie zgadzaja sie')







