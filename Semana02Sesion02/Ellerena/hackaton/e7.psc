Proceso e7
    Definir precio, descuento, total Como Real
    Definir tipo_membresia Como Caracter
    
    Escribir "Ingrese el precio del helado:"
    Leer precio
    
    Escribir "Ingrese el tipo de membresía (A, B o C):"
    Leer tipo_membresia
    
    Segun tipo_membresia Hacer
        "A":
            descuento = precio * 0.1
        "B":
            descuento = precio * 0.15
        "C":
            descuento = precio * 0.2
        De Otro Modo:
            Escribir "Tipo de membresía no válido."
    FinSegun
    
    total = precio - descuento
    
    Escribir "El precio con descuento es: $", total
    
FinProceso
