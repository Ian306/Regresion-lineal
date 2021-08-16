import matplotlib.pyplot as plt
def read_file():
    nombre_archivo = "fuel.csv"
    with open(nombre_archivo, "r") as archivo:
        #next(archivo, None)
        x = []
        y = []
        for linea in archivo:
            # Remover salto de línea
            linea = linea.rstrip()
            # Ahora convertimos la línea a arreglo con split
            lista = linea.split(",")
            x.append(float(lista[0]))
            y.append(float(lista[1]))
    return x, y

def evaluar(x, expre):      #Funcion que evalua la funcion ingresada
    try:
        return eval(expre)
    except:
        return None

def sum (values):
    sum = 0
    for i in values:
        sum = sum + i
    return sum

def sum_squares (values):
    sum = 0
    for i in values:
        sum = sum + i**2
    return sum

def sum_product (x, y):
    sum = 0
    for i in range(len(x)):
        sum = sum + x[i]*y[i]
    return sum

def mean (values):
    mean = sum(values) / len(values)
    return mean


x, y = read_file()
s_xy = sum_product(x, y) - (sum(x) * sum(y)) / len(x)
s_xx = sum_squares(x) - sum(x)**2 / len(x)

beta = s_xy / s_xx

alpha = mean(y) - beta * mean(x)
expresion = str(beta) + "*x + " + str(alpha)

print(expresion)
plt.plot(x,y,'o',label='Datos')
plt.plot(x, [evaluar(i, str(expresion)) for i in x], label = "Linea de tendencia")
#plt.plot(x,alpha*x + beta,label='Ajuste')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Regresion')
plt.grid()
plt.legend(loc=4)
plt.show()


          





   

   

  


  
    
        


    
