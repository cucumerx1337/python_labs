fio = input('ФИО:')
lenf=len(fio)-fio.count(' ')+2
inic = ''
k=0
for i in range(len(fio)-1):
    if fio[i] == ' ' and fio[i+1] != ' ':
        inic+=fio[i+1]
        k+=1
if k==2:
    inic = fio[0]+inic
print(f"Длина (символов): {lenf}")
print(f"Инициалы: {inic}")