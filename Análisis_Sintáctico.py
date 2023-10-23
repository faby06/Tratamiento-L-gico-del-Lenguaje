# An�lisis Sint�ctico
# Ejemplo de an�lisis sint�ctico simple para una gram�tica aritm�tica

# Definici�n de la gram�tica
grammar = {
    "<expresion>": ["<termino> + <expresion>", "<termino> - <expresion>", "<termino>"],
    "<termino>": ["<factor> * <termino>", "<factor> / <termino>", "<factor>"],
    "<factor>": ["<numero>", "( <expresion> )"],
    "<numero>": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
}

def parse(input_text, nonterminal):
    if input_text.startswith("<"):
        for production in grammar[nonterminal]:
            words = production.split()
            if all(parse(input_text, word) for word in words):
                return True
        return False
    else:
        return input_text.startswith(nonterminal)

# Ejemplo de entrada
input_text = "3 + 5 * (2 - 1)"

# Realizar an�lisis sint�ctico
if parse(input_text, "<expresion>") and not input_text:
    print("An�lisis sint�ctico exitoso.")
else:
    print("Error de sintaxis.")

