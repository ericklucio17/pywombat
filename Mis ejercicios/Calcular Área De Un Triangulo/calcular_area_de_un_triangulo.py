def calcular_area_de_triangulo(base, altura):
    return (base * altura) / 2

base = int(input("Ingrese la base:"))
altura = int(input("Ingrese la altura:"))

resultado = calcular_area_de_triangulo(base, altura)

print(f"El área del triangulo es: {resultado}")

