
def calcular_iva(subtotal, porcentaje_iva = 12):
    valor_iva = (subtotal * porcentaje_iva) / 100
    return valor_iva

monto_subtotal = 520
monto_iva =calcular_iva(monto_subtotal)
monto_total =monto_subtotal + monto_iva
print(f'Monto Total: {monto_total}')

monto_subtotal = 520
porcentaje_iva = 5
monto_iva =calcular_iva(monto_subtotal, porcentaje_iva)
monto_total =monto_subtotal + monto_iva
print (f'Monto Total: {monto_total}')

