largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))




def show(altura,largura):

   for i in range(0,altura):
      for j in range(1,largura):
         print('#',end='')

      print('#')

show(altura,largura)
