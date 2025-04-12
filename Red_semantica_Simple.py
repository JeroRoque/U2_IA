
red_semantica = {
    "Animal": {
        "relaciones": ["es un Ser Vivo"],
        "atributos": {"respira": "sí", "se_mueve": "sí"}
    },
    "Mamifero": {
        "relaciones": ["es un tipo de Animal"],
        "atributos": {"tiene_pelo": "sí", "amamanta": "sí"}
    },
    "Ave": {
        "relaciones": ["es un tipo de Animal"],
        "atributos": {"vuela": "sí", "pone_huevos": "sí"}
    },
    "Perro": {
        "relaciones": ["es un tipo de Mamifero", "es una Mascota"],
        "atributos": {"sonido": "Ladrido"}
    },
    "Pinguino": {
        "relaciones": ["es un tipo de Ave"],
        "atributos": {"vuela": "no"}  
    },
    "Gato": {
        "relaciones": ["es un tipo de Mamifero"],
        "atributos": {"sonido": "Maullido"}
    }
}

def agregar_relacion(nodo, relacion):
    if nodo in red_semantica:
        red_semantica[nodo]["relaciones"].append(relacion)
    else:
        red_semantica[nodo] = {"relaciones": [relacion], "atributos": {}}

def consultar_relaciones(nodo):
    if nodo in red_semantica:
        return ", ".join(red_semantica[nodo]["relaciones"])
    return "Nodo no encontrado"

def obtener_atributos(nodo):
    if nodo not in red_semantica:
        return {}
    
    atributos = red_semantica[nodo]["atributos"].copy()
    
    for relacion in red_semantica[nodo]["relaciones"]:
        if "es un tipo de" in relacion:
            clase_padre = relacion.split()[-1]
            atributos_padre = obtener_atributos(clase_padre)
            for k, v in atributos_padre.items():
                if k not in atributos:  
                    atributos[k] = v
    
    return atributos


print("═"*40)
print("RELACIONES:")
print(f"Perro: {consultar_relaciones('Perro')}")
print(f"Gato: {consultar_relaciones('Gato')}")
print(f"Pingüino: {consultar_relaciones('Pinguino')}")

print("\nATRIBUTOS:")
print("Perro:")
for k, v in obtener_atributos("Perro").items():
    print(f"- {k}: {v}")

print("\nPingüino:")
for k, v in obtener_atributos("Pinguino").items():
    print(f"- {k}: {v}")