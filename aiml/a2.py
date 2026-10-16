# Program to implement Propositional Logic using AND, OR, and NOT
def AND(p, q):
    return p and q
def OR(p, q):
    return p or q
def NOT(p):
    return not p
# Define truth values for variables P and Q
p = True
q = False
print("--- Propositional Logic Operations ---")
print(f"P = {P}, Q = {Q}\n")
# Evaluating basic logical operators
print(f"1. NOT P  : {NOT(P)}")
print(f"2. P AND Q: {AND(P, Q)}")
print(f"3. P OR Q : {OR(P, Q)}")
# Evaluating a compound logical expression: (P AND Q) OR (NOT P)
expression_result = OR(AND(P, Q), NOT(P))
print(f"\nEvaluating expression: (P AND Q) OR (NOT P)")
print(f"Final Result: {expression_result}")