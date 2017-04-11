a = 3
b = 4
c = 5

if a>(b+c) or b>(a+c) or c>(a+b):
    print("Ingrese un traingulo valido.")
elif a==b and b==c:
    print("Triangulo equilatero.")
elif a==b or b==c or a==c:
    print("Triangulo isoceles.")
else:
    print("Triangulo escaleno.")
