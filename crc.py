import random

__author__ = 'Przemysław Zamorski'
__description__ = 'Pierwsze zadanie suma modulo'
##SUMA MODULO##
print('CRC')


#funkcja xor
def xor(x,y):
    wynik=str(int(x)^int(y))

    return wynik

# #funkcja xor
def add_crc(file,crc):

    for bit in range(len(file)-3):
        if file[bit] == '1':
            file = file[:bit]+ xor(file[bit],crc[0])+ file[bit+1:]
            file = file[:bit+1]+ xor(file[bit+1],crc[1])+ file[bit+2:]
            file = file[:bit+2]+ xor(file[bit+2],crc[2])+ file[bit+3:]
            file = file[:bit+3]+ xor(file[bit+3],crc[3])+ file[bit+4:]
            # print(file)
        else:
            continue
    return file

def get_crc(file):
     correct_crc=file[len(file)-3:]
     return correct_crc

def append_crc(binary,crc):
    binary=binary[:-3]
    binary+=crc
    return binary

def moj_random(plik):
    for petla in range(random.randint(0, 6)): #petla dla zmiany 2 znakow
    # for petla in range(random.randint(0, 20)): #petla dla randowowej liczby znakow
        pos = random.randint(0, len(plik) - 1)
        if plik[pos] == '1':
            plik = plik[:pos] + "0" + plik[pos + 1:]
        elif plik[pos] == '0':
            plik = plik[:pos] + "1" + plik[pos + 1:]
        else:
            pass
    return plik



#############################
#definicja wielomianu CRC
wielmian='1011'
print('wielomian crc' ,wielmian)

#wczytanie pliku binarneg
binary_file=''
with open('test.txt', 'rb') as f1:
    while True:
        bytes = f1.read(1024)
        if bytes:
            for byte in bytes:
                binary_file = ''.join((binary_file, bin(byte)))
        else:
            break
binary_file=binary_file.replace("b","")



##Główny blok programu
print('plik binarny', binary_file)
binary_file_crc=binary_file+'000' ##dodaje do pliku 000
crc_file=add_crc(binary_file_crc,wielmian)  ##generuje z danymi wejściowymi +000 aby otrzymac ciag danych z konowka crc
crc=get_crc(crc_file)  ##wyciagam crc do zmiennej
print('Crc =',crc)

#funkcja losujaca

binary_file=moj_random(binary_file)
print('bin po trans',binary_file)

binary_file=append_crc(binary_file,crc)## dodanie crc do pliku binarnego


finish=add_crc(binary_file,wielmian)
print('wynik', finish)












