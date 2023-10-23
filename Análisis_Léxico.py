# An�lisis L�xico
# Ejemplo de an�lisis l�xico simple para un lenguaje de n�meros

import re

# Definici�n de patrones para n�meros enteros y operadores
integer_pattern = r"[-+]?\d+"
operator_pattern = r"[+\-*/]"

# Ejemplo de entrada
input_text = "3 + 5 * 2 - 10"

# Tokenizaci�n utilizando expresiones regulares
tokens = re.findall(f"({integer_pattern}|{operator_pattern}|.)", input_text)

# Filtrar espacios en blanco
tokens = [token for token in tokens if not token.isspace()]

print("Tokens encontrados:", tokens)

