# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")
#     print(fruit)
# print(fruits)



student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
#print(student_heights)

pesos = 0
for peso in student_heights:
    pesos += peso
print(pesos)

estudiantes = 0
for estudiante in student_heights:
    estudiantes += 1
print(estudiantes)

resultado = round(pesos/estudiantes)
print(f"El resultado de coso es: {resultado}")



















