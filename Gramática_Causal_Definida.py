# Gramática Causal Definida
# Ejemplo de una gramática causal definida en Python

# Definición de una regla causal
def causal_rule(condition, effect):
    if condition:
        effect()

# Ejemplo de uso de una regla causal
def condition_met():
    print("La condición se ha cumplido.")

def effect_action():
    print("Se ha producido un efecto.")

causal_rule(True, effect_action)  # Cumple la condición y produce el efecto
causal_rule(False, effect_action)  # No cumple la condición y no produce el efecto

