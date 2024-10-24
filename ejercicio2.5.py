#area de un triangulo
base_triangulo = int(input("Ingresa la base del triangulo: "))
altura_triangulo = int(input("Ingresa la altura del triangulo: "))
area_triangulo = (base_triangulo * altura_triangulo) / 2
print(f"El área del triángulo es: {area_triangulo}")

#Area de un rectangulo
largo_rectangulo = int(input("Ingresa la base del rectángulo: "))
ancho_rectangulo = int(input("Ingresa la altura del rectángulo: "))
area_rectangulo = (largo_rectangulo * ancho_rectangulo)
print("el area de el rectangulo es: " + str(area_rectangulo))

#Area total
area_total = area_triangulo + area_rectangulo
print("El area total es: " + str(area_total))

