lst = []
 
newl = []

while True:
    n = int(input("Digite um número: "))
    
    if n == 0:
        break

    lst.append(n) 

for i in range(1, len(lst) + 1):
    newl.append(lst[len(lst) - i])

for i in newl:
    print(i)
