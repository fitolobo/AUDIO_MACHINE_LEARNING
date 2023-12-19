#IgnacioSaavedra 
import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split

class MiPerceptron():  # Se crea la clase
    def __init__(self, num_features=2):
        self.num_features=num_features
        self.thetas=np.zeros(num_features)
        self.bias=0
        self.alpha=0.001

    def forward(self,x): # El metodo calcula los producto punto 
        neuron=np.dot(x,self.thetas) + self.bias
        y_pred=np.where(neuron>0,1,0)
        return y_pred
            
    def backward(self,x,y,y_pred,index,alpha=0.001): #Una vez realizado los producto punto, este recalcula los pesos
        delta=self.alpha*(y[index]-y_pred) 
        self.thetas+=delta*x 
        self.bias+=delta

    def train(self,epochs,x,y): # Se utilizan los metodos anteriores para repetir la cantidad de veces necesarias
        for i in range(epochs):
            for index ,vector in enumerate(x):
                y_pred=self.forward(vector)
                self.backward(vector,y,y_pred,index)

    def evaluate(self, x,y): #
        value=[]
        y_values=[]
        for index,vector in enumerate(x):
            neuron=np.dot(vector,self.thetas) + self.bias
            y_pred=np.where(neuron>0,1,0)
            #print(y_pred[0])
            y_values.append(y_pred)
            if y_pred==y[index]:
                value.append(1)
            # elif y_pred!=y[index]:
            #     value.append(0)
            else:
                value.append(0)
                
        print(y)
        print(y_values)


        # Porcentaje de exito
        accuracy=value.count(1)/len(value)*100
        return print("La precision es del %",accuracy,)
    
    def vector_weights(self): #Metodo para printear los valores de los pesos 
        print(self.thetas)

#Ahora se prepara los datos a partir del csv con la dimension reducida de los audios 
#Se crea una matriz 

def read_csv_as_matrix_pandas(file_path):
    df = pd.read_csv(file_path, header=None)
    matrix = df.values
    return matrix

csv_file_path = 'audio_2d.csv'
matrix = read_csv_as_matrix_pandas(csv_file_path)

#Con la matriz se adaptan los valores a vectores numpy
x=[]
y=[]
for i in range(1,len(matrix)):
    p=[]
    p.append(matrix[i][1])
    p.append(matrix[i][2])
    x.append(p)

    j=[]
    j.append(matrix[i][3])
    y.append(j)

x_array=np.array(x,dtype=np.float64)
y_array=np.array(y,dtype=np.float64)

#Se distribuyen los valores en grupos de entrenamiento y de prueba
x_train , x_test , y_train , y_test = train_test_split(x_array,y_array,test_size=0.1, random_state=42)

#Se instancia la clase y se llaman los metodos correspondientes
p = MiPerceptron()
p.train(100,x_train,y_train)
p.vector_weights() 
p.evaluate(x_test,y_test)