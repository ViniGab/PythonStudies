num1 = input('Digite um número: ')
num2 = input('Digite um número: ')

#isnumeric - isdigit - isdecimal

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
else:
    print('O simbolo/número que voce digitou não é válido.')

# num1 = int(num1)
# num2 = int(num2)

print(num1 + num2)