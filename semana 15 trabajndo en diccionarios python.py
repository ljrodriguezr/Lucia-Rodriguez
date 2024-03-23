
informacion_personal ={
    'nombre' : 'Lucia',
    'edad' : 28,
    'ciudad' : 'Lago Agrio',
    'provincia':'Sucumbios',
}
print('----------------------')
print('Diccionario Original')
print('----------------------')
for clave, valor in informacion_personal.items():
    print(f'{clave}:{valor}')

# Clave "ciudad" y modificarlo con una cuidad diferente.
informacion_personal['ciudad']= 'El Eno'
informacion_personal['provincia']= 'Lago Agrio'

# Nueva clave-valor al diccionario "profesion"
informacion_personal['profesion'] = 'Ama de Casa'

# Verifica si la clave "telefono" existe
if 'telefono' not in informacion_personal:
    informacion_personal['telefono'] = '0968847138'

# Elimina la clave "edad" del diccionario
# del informacion_personal['edad']
informacion_personal.pop('edad')
print('----------------------')
print('Diccionario Modificado')
print('----------------------')
for clave, valor in informacion_personal.items():
    print(f'{clave}:{valor}')