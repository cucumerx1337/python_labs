col = int(input("in_1: "))
k = 0
idx = 2
for n in range(col):
    line = input(f"in_{idx}: ")
    idx += 1
    name, lastname, age, form = line.split()
    if form == 'True':
        k += 1
print(f'out: {k}, {col - k}')