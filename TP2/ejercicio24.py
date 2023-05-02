from pila import Pila

class personajes:
    def __init__(self, nombre, peliculas):
        self.nombre = nombre
        self.peliculas = peliculas


stack = Pila()

def cargar_pila():
    stack.push(personajes("Iron Man", 3))
    stack.push(personajes("Capitán América", 4))
    stack.push(personajes("Thor", 4))
    stack.push(personajes("Hulk", 3))
    stack.push(personajes("Black Widow", 7))
    stack.push(personajes("Hawkeye", 4))
    stack.push(personajes("Spider-Man", 2))
    stack.push(personajes("Doctor Strange", 2))
    stack.push(personajes("Black Panther", 2))
    stack.push(personajes("Ant-Man", 2))
    stack.push(personajes("Vision", 2))
    stack.push(personajes("Scarlet Witch", 3))
    stack.push(personajes("Falcon", 3))
    stack.push(personajes("War Machine", 4))
    stack.push(personajes("Winter Soldier", 3))
    stack.push(personajes("Guardians of the Galaxy", 2))
    stack.push(personajes("Rocket Raccoon", 5))
    stack.push(personajes("Groot", 5))
    stack.push(personajes("Thanos", 3))
    stack.push(personajes("Loki", 6))
    
cargar_pila()

def posicion(stack):
    posiciongroot =0
    posicionrocket =0
    for i in range(stack.size()):
        if stack.on_top().nombre=="Rocket Racoon":
            posicionrocket = i
        
        if stack.on_top().nombre == "Groot":
            posiciongroot= i
        stack.pop()
    return posicionrocket, posiciongroot

a,b=posicion(stack)

def cantidad_de_peliculas(stack):
    personajes5= []
    cantidad=[]
    for i in range(stack.size()):
        if stack.on_top().peliculas > 5:
            personajes5.append(stack.on_top().nombre)
            cantidad.append(stack.on_top().peliculas)

        stack.pop()   
    return personajes5,cantidad

cargar_pila()
npc, cant = cantidad_de_peliculas(stack)

cargar_pila()

def viuda_negra(stack):
    for i in range(stack.size()):
        if stack.on_top().nombre=="Black Widow":
            cantidad_viuda = stack.on_top().peliculas
        
        stack.pop()
    return cantidad_viuda

cant_pel_viuda=viuda_negra(stack)


cargar_pila()
def nombres_personajes(stack,iniciales):
    lista_personajes=[]
    for i in range(stack.size()):
        for j in iniciales:
            if stack.on_top().nombre.startswith(j) == True:
                lista_personajes.append(stack.on_top().nombre)
        stack.pop()
    return lista_personajes
iniciales=["C","D","G"]

for i in range(len(npc)):
    print(f'{npc[i]} aparece en {cant[i]} peliculas')
print(f"Black Widow aparece en {cant_pel_viuda} peliculas")
print("Los personajes que empiezan con C,D,G son: ")
for i in nombres_personajes(stack,iniciales):
    print(f"{i} empieza con: {i[0]}")
    