# Inducci�n Gramatical
# Ejemplo de generaci�n de secuencias mediante reglas de producci�n

import random

# Reglas de producci�n para una gram�tica generativa simple
production_rules = {
    "S": ["NP VP"],
    "NP": ["Det N", "N"],
    "VP": ["V NP"],
    "Det": ["the", "a"],
    "N": ["cat", "dog"],
    "V": ["chased", "ate"]
}

def generate_sentence(grammar, start_symbol):
    if start_symbol not in grammar:
        return start_symbol
    production = random.choice(grammar[start_symbol])
    sentence = [generate_sentence(grammar, symbol) for symbol in production.split()]
    return " ".join(sentence)

# Generar una oraci�n aleatoria
random_sentence = generate_sentence(production_rules, "S")
print("Oraci�n generada:", random_sentence)

