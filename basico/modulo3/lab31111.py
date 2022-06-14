income = float(input("Introduce el ingreso anual:"))
#
# Escribe tu código aquí.
if income <= 85528:
    tax = income*0.18 - 556.02
elif income > 85528:
    tax = 14839.02 + (income-85528)*0.32

tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")
