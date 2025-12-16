print('Bienvenido al sistema de juguetes')

preguntas = [
    ('nombre', 'Ingresa tu nombre: '),
    ('puesto_trabajo', 'Ingresa el puesto de trabajo: '),
    ('adjetivo1', 'Ingresa un adjetivo: '),
    ('adjetivo2', 'Ingresa otro adjetivo: '),
    ('comida', 'Ingresa una comida: '),
    ('emocion', 'Ingresa una emoción: '),
    ('curso', 'Ingresa un curso: ')
]

datos = {}
for clave, pregunta in preguntas:
    datos[clave] = input(pregunta)

print('\nGracias por usar el sistema de juguetes!')
print('Aquí está tu historia:')
print(f"Había una vez un estudiante llamado {datos['nombre']}, que se estaba formando como {datos['puesto_trabajo']}.")
print(f"Sus compañeros le parecieron muy {datos['adjetivo1']}, y su profesor era cuando menos {datos['adjetivo2']}.")
print(f"Para comer, comían {datos['comida']}, mientras repasaban sus notas y sentían {datos['emocion']}.")
print(f"A pesar de todo, estaban decididos a completar su curso de {datos['curso']}.")