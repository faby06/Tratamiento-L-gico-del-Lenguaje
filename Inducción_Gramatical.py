# Inducción Gramatical
# Ejemplo de generación de secuencias mediante reglas de producción

import random

# Reglas de producción para una gramática generativa simple
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

# Generar una oración aleatoria
random_sentence = generate_sentence(production_rules, "S")
print("Oración generada:", random_sentence)

