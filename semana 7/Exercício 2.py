largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))




def show(altura,largura):
    
        


    for i in range(0,largura):
        print('#',end='')
    print()
    for j in range(0, altura - 2):
        print('#', end='')

        for k in range(0, largura - 2):
           print(' ',end='')
        
        print('#')
    
    for i in range(0, largura):
        print('#', end='')

    print()


show(altura,largura)
