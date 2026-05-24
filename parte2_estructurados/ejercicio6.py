# ==============================================================================
# EJERCICIO 6: CADENAS DE TEXTO
# Asignado a: José Mendoza
# ==============================================================================

def main():
    print("--- EJERCICIO 6: CADENAS DE TEXTO ---")

#Desarrollar un programa que solicite una frase al usuario y muestre la cantidad de caracteres 

frase = input("Ingrese una frase: ") 

cantidad_caracteres = len(frase) 

usuario_frase = f"La cantidad de caracteres en la frase es: {cantidad_caracteres}" 

print(usuario_frase) 

print(usuario_frase.upper()) 

print(usuario_frase.lower()) 

print(usuario_frase[::-1]) 
    
if __name__ == "__main__":
    main()
