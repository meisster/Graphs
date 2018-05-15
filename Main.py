import random
import time
import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import ttk
from Graph import *

isCreated = False


def createMatrix(size, g):
    g.verticesMatrix = [0] * size
    for i in range(size):
        g.verticesMatrix[i] = [0] * size


g = Graph(1)
gr = Graph(1)
createMatrix(5, g)
g.addEdge(1,3)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(2,4)
g.addEdge(4,5)
g.addEdge(5,2)
g.displayMatrix()
s = []
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
createMatrix(5, gr)
gr.addEdge(1,2)
gr.addEdge(1,5)
gr.addEdge(1,4)
gr.addEdge(2,3)
gr.addEdge(3,5)
gr.addEdge(3,4)
gr.displayMatrix()

print(gr.HamiltonMSAS(1, stack=s))
