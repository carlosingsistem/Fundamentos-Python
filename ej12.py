#Diccionarios - Almacena a pares clave -> valor
mi_diccionario = {
    'nombre': 'Bruno Dias',
    'edad': 25,
    'ciudad': 'La Paz'
}

print(mi_diccionario)

#Acceder a un valor
print(mi_diccionario['nombre'])
print(mi_diccionario['ciudad'])
#Agregar un valor a un diccionario
mi_diccionario['profesion'] = 'Ingeniero'
print(mi_diccionario)

#Obtener claves del diccionario
print(mi_diccionario.keys())

#Obtener los valores del diccionario
print(mi_diccionario.values())

#Verificar si una clave existe en un diccionario
if 'ciudad' in mi_diccionario:
    print("Ciudad encontrada")

#Recorrido de un diccionario
for clave, valor in mi_diccionario.items():
    print("[Clave:]" , clave , "[Valor:]" , valor)