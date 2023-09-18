salario = int(input("¿Cuanto es el salario diario del empleado? "))
dias = int(input("Dime la cantidad de días trabajado: "))
salario = salario * dias
salariorestao = salario * 0.25
salario_total = salario - salariorestao

print(f"El salario es: {salario_total}")