# Sentencias
temperatura = int(input("Ingresa la temperatura actual: "))

if temperatura > 28:
    print("Hace calor")
else:
    print("Hace frio")
    
    
if temperatura > 28:
    print("Hace calor")
elif temperatura > 20:
    print("Es un dia agradable")
elif temperatura > 10:
    print("Hace un poco de frio")
else:
    print("Hace frio, brrr")
    
print("Proceso concluido")