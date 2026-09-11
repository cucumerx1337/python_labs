stroka = input()
out = ''
k = 0
fin = 0
cs = 0
start = 0
for i in stroka:
    cs += 1
    if i == i.upper() and i.isalpha() and k != 1:
        out += i
        k += 1
        start = cs
for i in range(len(stroka) - 1):
    if stroka[i] in '0123456789':
        out += stroka[i + 1]
        fin = i
        break
step = (fin + 1) - (start - 1)
for n in range(fin + 1 + step, len(stroka), step):
    out += stroka[n]
    if stroka[n] == '.':
        break
print(out)


    
