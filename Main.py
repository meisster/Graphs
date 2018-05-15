import random
import time
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from Graph import *

isCreated = False


def createMatrix(size, g):
    g.verticesMatrix = [0] * size
    for i in range(size):
        g.verticesMatrix[i] = [0] * size


grafN = Graph(1)
grafS = Graph(0)
#if g.isEven():
    #print(g.EulerMSAS(g.getVertex(1), s))

'''gr.addEdge(1,3)
gr.addEdge(3,2)
gr.addEdge(2,1)
gr.addEdge(2,5)
gr.addEdge(5,4)
gr.addEdge(4,2)
s = []
if gr.isInOut():
    s = gr.EulerLNAS(1, s)
    s.reverse()
    print(s)'''


def displayGraph():
    global isCreated, grafN, grafS
    if v1.get() == 2:
        grafN.displayMatrix()
    else:
        print("Nie stworzono grafu!")


def start():
    global grafN, grafS
    grafN = Graph(1)
    grafS = Graph(0)
    lista = vertexes.get().split(';')
    j = 0
    for i in lista:
        lista[j] = lista[j].split()
        j += 1
    max = 0
    for i in lista:
        if int(i[0]) > max:
            max = int(i[0])
        if int(i[1]) > max:
            max = int(i[1])
    createMatrix(max, grafN)
    for i in lista:
        grafS.addEdge(int(i[0]), int(i[1]))
        grafN.addEdge(int(i[0]), int(i[1]))

    opVar = v2.get()
    stack = []
    if v1.get() == 1:
        if opVar == 2:
            start = time.clock()
            s = grafS.EulerLNAS(1, stack)
            #s.reverse()
            print(s)
            print("Czas działania EulerLNAS:", time.clock()-start)
            stack = []
        else:
            start = time.clock()
            print(grafS.HamiltonLNAS(1, stack))
            print("Czas działania HamiltonLNAS:", time.clock() - start)
            stack = []
    else:
        if opVar == 2:
            start = time.clock()
            print(grafN.EulerMSAS(grafN.getVertex(1), stack))
            print("Czas działania EulerMSAS:", time.clock() - start)
            stack = []
        else:
            start = time.clock()
            print(grafN.HamiltonMSAS(1, stack))
            print("Czas działania HamiltonMSAS:", time.clock() - start)
            stack = []
#1 3; 3 2;2 1;2 5;5 4;4 2;4 6;6 1
#========================================

window = tk.Tk()
window.title("Algorytmy grafowe")
window.geometry("340x130")
window.resizable(False, False)

#========================================

ustawienia = ttk.LabelFrame(window, text=' Ustawienia ',height=50)
#ustawienia.place(x=10,y=10)
ustawienia.pack()

ttk.Label(ustawienia, text="Pary wierzchołków:").grid(column=0, row=0)
vertexes = tk.StringVar()
liczba_wier = ttk.Entry(ustawienia, width=30, textvariable=vertexes)
liczba_wier.grid(column=0, row=1)

#========================================

v1 = tk.IntVar()

ttk.Radiobutton(ustawienia, text="Skierowany", variable=v1, value=1).grid(column=0, row=3)
ttk.Radiobutton(ustawienia, text="Nieskierowany", variable=v1, value=2).grid(column=0, row=4)

v2 = tk.IntVar()

ttk.Radiobutton(ustawienia, text="Cykl Hamiltona", variable=v2, value=1).grid(column=1, row=3)
ttk.Radiobutton(ustawienia, text="Cykl Eulera", variable=v2, value=2).grid(column=1, row=4)

start_button = ttk.Button(ustawienia, text="START", comman=start)
start_button.grid(column=0,row=10)

dispGraph = ttk.Button(ustawienia, text="Wyświetl graf", comman=displayGraph)
dispGraph.grid(column=1, row=10)

#========================================

window.mainloop()

#========================================

