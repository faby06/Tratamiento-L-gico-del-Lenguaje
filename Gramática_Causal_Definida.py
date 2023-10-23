# Gram�tica Causal Definida
# Ejemplo de una gram�tica causal definida en Python

# Definici�n de una regla causal
def causal_rule(condition, effect):
    if condition:
        effect()

# Ejemplo de uso de una regla causal
def condition_met():
    print("La condici�n se ha cumplido.")

def effect_action():
    print("Se ha producido un efecto.")

causal_rule(True, effect_action)  # Cumple la condici�n y produce el efecto
causal_rule(False, effect_action)  # No cumple la condici�n y no produce el efecto

