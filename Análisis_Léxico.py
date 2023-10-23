# Análisis Léxico
# Ejemplo de análisis léxico simple para un lenguaje de números

import re

# Definición de patrones para números enteros y operadores
integer_pattern = r"[-+]?\d+"
operator_pattern = r"[+\-*/]"

# Ejemplo de entrada
input_text = "3 + 5 * 2 - 10"

# Tokenización utilizando expresiones regulares
tokens = re.findall(f"({integer_pattern}|{operator_pattern}|.)", input_text)

# Filtrar espacios en blanco
tokens = [token for token in tokens if not token.isspace()]

print("Tokens encontrados:", tokens)

