import pandas as pd # type: ignore
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

#  1. Datos de entrenamiento (ejemplos de mensajes y sus etiquetas)
data = {
    'texto': [
        "Me encantó la película, fue increíble",
        "No me gustó para nada, fue aburrida",
        "El servicio del restaurante fue excelente",  
        "La comida estaba fría y sin sabor",
        "Un libro fascinante y bien escrito",
        "La trama del libro fue muy predecible"
    ],
    'etiqueta': ['positivo', 'negativo', 'positivo', 'negativo', 'positivo', 'negativo']  
}

df = pd.DataFrame(data)  # Convertimos en un DataFrame

#  2. Preparamos los datos para el modelo
X = df['texto']  # Mensajes
y = df['etiqueta']  # Etiquetas (positivo o negativo)

vectorizer = CountVectorizer()  # Convertimos texto a números
X_vec = vectorizer.fit_transform(X)  # Aplicamos la transformación

X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

#  3. Entrenamos el modelo Naive Bayes
modelo = MultinomialNB()
modelo.fit(X_train, y_train)

#  4. Evaluamos el modelo
y_pred = modelo.predict(X_test)
print(f'Precisión del modelo: {accuracy_score(y_test, y_pred)}')
print(classification_report(y_test, y_pred, zero_division=1))

#  5. Permitir que el usuario ingrese mensajes para clasificarlos
while True:
    mensaje_usuario = input("\n Ingresa un mensaje para clasificar (o escribe 'salir' para terminar): ")
    
    if mensaje_usuario.lower() == 'salir':
        print("Saliendo del programa...")
        break  # Termina el programa si el usuario escribe 'salir'
    
    mensaje_vec = vectorizer.transform([mensaje_usuario])  # Convertimos el mensaje a números
    categoria = modelo.predict(mensaje_vec)[0]  # Clasificamos el mensaje
    
    print(f" El mensaje '{mensaje_usuario}' es clasificado como: {categoria}")
