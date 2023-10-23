# Gramáticas: Jerarquía de Chomsky
# Ejemplo de gramáticas generativas de diferentes clases

# Gramática Tipo 0
type_0_grammar = "S -> aSb | ε"
# Gramática Contexto-Sensible
context_sensitive_grammar = "AB -> BA | A | B | ε"
# Gramática Contexto-Libre
context_free_grammar = "S -> NP VP | Det N V | The cat | chased | a dog"
# Gramática Regular
regular_grammar = "S -> 0S | 1"

print("Gramática Tipo 0:", type_0_grammar)
print("Gramática Contexto-Sensible:", context_sensitive_grammar)
print("Gramática Contexto-Libre:", context_free_grammar)
print("Gramática Regular:", regular_grammar)

