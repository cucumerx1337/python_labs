col=int(input())
k = 0
for n in range(col):
    name,lastname, age, form = map(str, input().split())
    if form=='True':
        k+=1
print(k, col-k)