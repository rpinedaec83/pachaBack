def cm_to_inch(cm):
    inch = cm / 2.54
    return inch

def lbs_to_kg(lbs):
    kg = lbs * 0.45359237
    return kg

# Ejemplo de uso
cm = 100
lbs = 150
inch = cm_to_inch(cm)
kg = lbs_to_kg(lbs)
print(f"{cm} centímetros son {inch:.2f} pulgadas")
print(f"{lbs} libras son {kg:.2f} kilogramos")
