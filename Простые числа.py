# Способ перебора
N=int(input('Введите число больше 2: '))
M=[i for i in range (2, N+1)]

for i in range (len(M)):
    count=0
    for j in range (2,10):
        if M[i]%j==0:
            count+=1
    if count==1:
        print('M[{}]={}'.format (M.index(M[i]), M[i]))

# Решето Эратосфена
n=int(input('Введите число больше 2: '))
M=[i for i in range (2, n+1)]

for num in M:
    if num!=0:
        for i in range (2 * num, n+1, num):
            M[i-2] = 0    
print(*list(filter(lambda x: x != 0, M)))
