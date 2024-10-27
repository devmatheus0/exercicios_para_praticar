#Dado n inteiro, escreva as seguintes condições
#  - se n é ímpar, imprima 'Weird'
#  - se n é par e está entre 2 e 5, imprima 'Not Weird'
#  - se n é par e está entre 6 e 20, imprima 'Weird'
#  - se n é par e maior que 20, imprima 'Not Weird'

n = int(input().strip())
if ((n+1) % 2) == 0:
    print('Weird')
elif (n % 2) == 0 and n in range(2,6):
    print('Not Weird')
elif (n % 2) == 0 and n in range(6,21):
    print('Weird')
elif (n % 2) == 0 and n > 20:
    print('Not Weird')

# #Dadas as entradas a e b, imprima 3 linha contendo: a soma de a e b, a diferença de a e b, 
# # o produto de a e b

a = int(input())
b = int(input())
sum = a+b
diff = a-b
prod = a * b

print(sum)
print(diff)
print(prod)

#Para n, imprima o quadrado de todos os números menores que n não negativos.
n = int(input())
list_of_n = [n-1 for n in range(n+1) if n>0]
print(list_of_n)
for i in list_of_n:
    square = i ** 2
    print(square)

# Definir se um ano é bissexto ou não

year = int(input('Insira um ano '))

def is_leap(year):
    leap = False
    
    if year % 4 == 0 and year % 100 == 0:
        if year % 400 == 0:
            leap = True
    elif year % 4 == 0:
        leap = True
    
    return leap

print(is_leap(year))