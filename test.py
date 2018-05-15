import random
import time
import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import ttk
from Graph import *

isCreated = False


def createMatrix(size, g, type):
    if type == 1:
        g.verticesMatrix = [0] * size
        for i in range(size):
            g.verticesMatrix[i] = [0] * size
    elif type == 2:
        g.graphMatrix = [0] * size
        for i in range(size):
            g.graphMatrix[i] = [0] * size
    else:
        print('Zły typ danych!')


grafS = Graph(1)
grafG = Graph(0)


def displayGraph():
    global isCreated, grafG, grafS
    pomG = {'Macierz sąsiedztwa': 1, 'Macierz grafu': 2}
    if isCreated:
        if pomG[graphChosen.get()] == 1:
            grafS.displayMatrix()
    else:
        print("Nie stworzono grafu!")


def cre8tGraph():
    global isCreated, whichCreated, grafG, grafS
    size = sizes.get()
    pomG = {'Macierz sąsiedztwa': 1, 'Macierz grafu': 2}
    if size == 0:
        print('Wprowadz wielkosc grafu!')


def operate():
    global isCreated, whichCreated, grafG, grafS
    poOp = {'DEL_msąsiedztwa': 0, 'DEL_mgrafu': 2, 'DFS_msąsiedztwa': 1, 'DFS_mgrafu': 3}
    opVar = poOp[operationChosen.get()]
    '''if opVar < 2:
        if opVar == 0:
            start = time.clock()
            grafS.DEL_msasiedztwa()
            print("Czas działania DEL_msasiedztwa:", time.clock()-start)
        else:
            start = time.clock()
            grafS.DFS_msasiedztwa()
            print("Czas działania DFS_msasiedztwa:", time.clock() - start)
    else:
        if opVar == 2:
            start = time.clock()
            grafG.DEL_mgrafu()
            print("Czas działania DEL_mgrafu:", time.clock() - start)
        else:
            start = time.clock()
            grafG.DFS_mgrafu()
            print("Czas działania DFS_mgrafu:", time.clock() - start)'''


win = tk.Tk()
win.title("Graph operations")
tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Grafy')
tabControl.pack(expand=1, fill='both')
tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text='Generowanie testów')
tabControl.pack(expand=1, fill='both')

python = ttk.LabelFrame(tab1, text='Complex Data Structures Operations')
python.grid(column=0, row=0, padx=8, pady=4)
sizes = tk.IntVar()
size_set = ttk.Entry(python, width=8, textvariable=sizes)
size_set.grid(column=0, row=4)

opButton = ttk.Button(python, text="Wykonaj operacje", comman=operate)
opButton.grid(column=1, row=1)
opButton.config(state="DISABLED")
createGraph = ttk.Button(python, text="Stwórz graf", comman=cre8tGraph)
createGraph.grid(column=1, row=2)
dispGraph = ttk.Button(python, text="Wyświetl graf", comman=displayGraph)
dispGraph.grid(column=2, row=2)

ttk.Label(python, text='Graf').grid(column=0, row=0, sticky=tk.S)
ttk.Label(python, text='Operacja').grid(column=1, row=0, sticky=tk.S)
ttk.Label(python, text='Rozmiar grafu').grid(column=0, row=3, sticky=tk.S)


operation = tk.StringVar()
operationChosen = ttk.Combobox(python, width=16, textvariable=operation, state='readonly')
operationChosen['values'] = ('DEL_msąsiedztwa', 'DEL_mgrafu', 'DFS_msąsiedztwa', 'DFS_mgrafu')
operationChosen.grid(column=0, row=1)
operationChosen.current(0)

graph = tk.StringVar()
graphChosen = ttk.Combobox(python, width=15, textvariable=graph, state='readonly')
graphChosen['values'] = ('Macierz sąsiedztwa', 'Macierz grafu')
graphChosen.grid(column=0, row=2)
graphChosen.current(0)

win.mainloop()