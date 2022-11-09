import matplotlib.pyplot as plt
import numpy as np
import time

# Creamos la funcion para guardar los datos
def savedatos():
    # Pedir la cantidad de datos
    numb = input('Cuantos datos vas a ingresar: ')
    numb = int(numb)
    # Creamos dos listas vacias con el fin de que almacenen la ubicacion en 'x' 'y'
    x = []
    y = []
    contx = 0
    conty = 0

    # crear la funcion para ir ingresando los valores de x
    time.sleep(1)
    for i in range(0, numb):
        contx += 1
        i = input('ingrese el ' + str(contx) + ' dato de la posicion x: ')
        i = int(i)
        x.append(i)
   
    # Para ver como quedo la lista
    print('Asi quedo los datos en x:')
    print(x)
    # un tiempo de espera
    time.sleep(1)

    # crear la funcion para ir ingresando los valores de y
    for i in range(0, numb):
        conty += 1
        i = input('ingrese el ' + str(conty) + ' dato de la posicion y: ')
        i = int(i)
        y.append(i)
        
    print('Asi quedo los datos en y:')
    print(y)
    
    
    # y = [lista * 1 for lista in x]
    # [float(i) for i in x]
    # [float(i) for i in y]


    # creamos el grafico de dispercion con plt de matplotlib
    plt.plot(x, y, marker='o', markerfacecolor='violet', markersize=15)
    # plt.axhline(color="black")

    # creamo la linea de tendencia
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plt.plot(x, p(x), color='blue', linewidth=3, linestyle="--", alpha=0.3)
    
    colorpersonafication = input(str('Quiere personificar el color del area bajo la curva(si o no): '))
    
    if colorpersonafication == 'si':
        choicecolor = input(str('Ingresa el color del area bajo la curva: '))
        plt.fill_between(x, y, color=choicecolor, alpha=0.1)
    else:
        plt.fill_between(x, y, color='green', alpha=0.1) 
    
    
    
    opcionpersonalitation = input(str('Desea personalisar el grafico (si o no): '))
    
    
    if opcionpersonalitation == 'si':
        titles = input(str('Agregar un titulo: '))
        xname = input(str('Agregar nombre de X: '))
        yname = input(str('Agregar nombre de Y: '))
        plt.title(titles)
        plt.xlabel(xname)
        plt.ylabel(yname)
        

    # mostramos el grafico
    print('CARGANDOOO........')
    time.sleep(1)
    plt.show()

    
    
def run():
    savedatos()


if __name__ == '__main__':
    run()
