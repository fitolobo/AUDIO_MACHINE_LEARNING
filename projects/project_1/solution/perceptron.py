import numpy as np
import logging
from typing import Optional

# Configure logging at the start of your script
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')



class Perceptron:
    """Perceptron
        Clase escrita en numpy para construir un perceptrón utilizando 
        la regla de actualización de pesos basada en álgebra lineal.
        Contiene 4 métodos: 
            1 - forward: transformación del vector de entrada a través del modelo y = sigma(Wx + b)
            2 - backward: cálculo del error producido por el modelo
            3 - train: entrenamiento del modelo. 
            4 - evaluate: cálculo del accuracy del modelo. 
    """
    def __init__(self, num_features: int, learning_rate=0.01):
        ### Variables que inicializan el modelo
        ### Numero de características incluyendo el bias
        self.weights = np.zeros(num_features + 1)  
        ### Hiperparámetro para controlar la velocidad de cambio en el aprendizaje
        self.learning_rate = learning_rate

    def forward(self, x):
        """forward pass
            Aplica una transformación lineal a la entrada: y = W x + b
        Args:
            x (np.array): vector de entrada de la red.

        Retorna:
            np.array : vector de salida de la red
        """
        return np.dot(x, self.weights[1:]) + self.weights[0]

    def backward(self, x, y, output):
        """backward pass

        Args:
            x (np.array): vector de entrada de la red.
            y (np.array): salida esperada del modelo.
            output (np.array): salida del modelo lineal
        Retorna:
            np.array : vector de salida con el error cometido.
        """        
        ### Calculo del error
        error = y - output
        ### Actualizacion de los pesos
        self.weights[1:] += self.learning_rate * error * x
        self.weights[0] += self.learning_rate * error

    def train(self, training_data, labels, epochs):
        """Training the perceptron"""
        for epoch in range(epochs):
            for x, y in zip(training_data, labels):
                output = self.predict(x)
                self.backward(x, y, output)

    def evaluate(self, test_data, test_labels):
        """evaluacion a traves de accuracy

        Args:
            test_data (np.array): vector de entrada para el modelo desde un conjunto de test.
            test_labels (np.array): salida esperada del modelo para el ejemplo de entrada.

        Retorna:
            np.float: valor de accuracy alcanzado por el modelo.
        """
        predictions = [self.predict(x) > 0 for x in test_data]
        accuracy = np.mean(predictions == test_labels)
        return accuracy

    def predict(self, x):
        """Realizar la predicción sobre un nuevo ejemplo"""
        return 1 if self.forward(x) > 0 else 0
    