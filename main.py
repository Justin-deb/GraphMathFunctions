import math
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def J(x):
    suma = 0
    for n in range(1,6):
        numerador = (-1)**n * (x/2)**(2*n)
        denominador = (math.factorial(n))**2
        suma += numerador/denominador

    return 1 + suma

def listaIntervalos(salto,valorInicial,valorFinal):
    lista = []
    for n in np.arange(valorInicial,valorFinal+salto,salto):
        lista.append(float(n))
    return lista

def evaluarJ(listaIntervalos):
    lista = []
    for n in listaIntervalos:
        lista.append(J(n))
    return lista

def diferenciaProgresiva(x,h):
    numerador = J(x+h) - J(x)
    denominador = h
    return numerador/denominador

def diferenciaCentral(x,h):
    numerador = J(x+h) - J(x-h)
    denominador = 2*h
    return numerador/denominador

#Important

def listaProgresiva(listaIntervalos):
    lista = []
    for n in range(0,len(listaIntervalos)-1):
        lista.append(diferenciaProgresiva(listaIntervalos[n],(listaIntervalos[1] - listaIntervalos[0])))
    return lista

def listaCentral(listaIntervalos):
    lista = []
    for n in range(1,len(listaIntervalos)-1):
        lista.append(diferenciaCentral(listaIntervalos[n],(listaIntervalos[1] - listaIntervalos[0])))
    return lista

#Graph
def JExacta(x):
    suma = 0
    for n in range(1,6):
        numerador = (-1)**n
        denominador = (math.factorial(n))**2
        resto = n*(x/2)**(2*n-1)
        suma += numerador/denominador * resto

    return suma

def listaIntervalosExacta(salto,valorInicial,valorFinal):
    lista = []
    for n in np.arange(valorInicial,valorFinal+salto,salto):
        lista.append(float(n))
    return lista

def listaDerivadaExacta(listaIntervalosExacta):
    lista = []
    for n in listaIntervalosExacta:
        lista.append(JExacta(n))
    return lista

def crearFrame():
    fig, ax = plt.subplots()
    ax.set_title("Comparacion de las aproximaciones con la derivada exacta")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid(True)

    xExactaLista= listaIntervalosExacta(0.01,0,4)
    yExactaLista= listaDerivadaExacta(xExactaLista)

    xIntervalosSalto1 = listaIntervalos(0.1,0,4)
    xIntervalosSalto5 = listaIntervalos(0.5,0,4)

    yProgresiva1 = listaProgresiva(xIntervalosSalto1)
    yProgresiva5 = listaProgresiva(xIntervalosSalto5)
    yCentrada1 = listaCentral(xIntervalosSalto1)
    yCentrada5 = listaCentral(xIntervalosSalto5)

    xCentrada1 = listaIntervalos(0.1, 0, 4)[1:-1]
    xCentrada5 = listaIntervalos(0.5, 0, 4)[1:-1]

    xIntervalosSalto1 = xIntervalosSalto1[:-1]
    xIntervalosSalto5 = xIntervalosSalto5[:-1]
    
    ax.plot(xExactaLista,yExactaLista,label="Derivada Exacta",linestyle="-")
    ax.plot(xIntervalosSalto1,yProgresiva1,label="Progresiva con salto 0.1",linestyle="--",marker = "o", markersize = 4)
    ax.plot(xIntervalosSalto5,yProgresiva5,label="Progresiva con salto 0.5",linestyle="--",marker = ".", markersize = 4)
    ax.plot(xCentrada1,yCentrada1,label="Centrada con salto 0.1",linestyle="-.",marker = "s", markersize = 4)
    ax.plot(xCentrada5,yCentrada5,label="Centrada con salto 0.5",linestyle="-.",marker = "^", markersize = 4)

    all_y = (yExactaLista + yProgresiva1 + yProgresiva5+ yCentrada1 + yCentrada5)

    minY = min(all_y)
    maxY = max(all_y)

    ax.legend(loc="best")
    ax.set_xlim(0, 4)
    ax.set_ylim(minY-0.05, maxY+0.05)

    root = tk.Tk()
    root.title("Comparacion de las aproximaciones con la derivada exacta")
    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True)

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    root.mainloop()

if __name__ == '__main__':
    listaDerivadasProgresivas1 = listaProgresiva(listaIntervalos(0.1,0,4))
    listaDerivadasProgresivas5 = listaProgresiva(listaIntervalos(0.5, 0, 4))
    listaDerivadasCentrales1 = listaCentral(listaIntervalos(0.1, 0, 4))
    listaDerivadasCentrales5 = listaCentral(listaIntervalos(0.5, 0, 4))

    print("Lista de aproximaciones de tipo progresiva de J'(x) con salto de 0.1: ")
    print(listaDerivadasProgresivas1)


    print("Lista de aproximaciones de tipo progresiva de J'(x) con salto de 0.5: ")
    print(listaDerivadasProgresivas5)

    print("Lista de aproximaciones de tipo centradas de J'(x) con salto de 0.1: ")
    print(listaDerivadasCentrales1)

    print("Lista de aproximaciones de tipo centradas de J'(x) con salto de 0.5: ")
    print(listaDerivadasCentrales5)

    crearFrame()
