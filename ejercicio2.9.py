#Pago semanal por trabajador
horas_trabajadas_por_dia = int(input("Ingresa las horas trabajadas: "))
costo_hora = int(input("Ingresa el costo por hora: "))
horas_semanal = (horas_trabajadas_por_dia * 5)
costo_semanal = (horas_semanal * costo_hora)
print(f"El pago semanal es: {costo_semanal:,}")

