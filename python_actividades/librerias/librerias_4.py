import numpy as np
import calendar

# Definir los nombres de los días de la semana
nombres_dias_semana = list(calendar.day_name)

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

for mes in meses:
    print(f"{mes}:")
    
    # Obtener el número de días en el mes y el día de la semana en que comienza
    num_dias_mes = calendar.monthrange(2023, meses.index(mes) + 1)[1]
    dia_semana_inicio = calendar.monthrange(2023, meses.index(mes) + 1)[0]
    
    dias_mes = [str(dia) for dia in range(1, num_dias_mes + 1)]
    semanas = [dias_mes[i:i + 7] for i in range(0, len(dias_mes), 7)]
    
    for num_semana, semana in enumerate(semanas, start=1):
        dias_semana = " ".join(semana)
        print(f"Semana {num_semana}: {dias_semana}")
    print()
