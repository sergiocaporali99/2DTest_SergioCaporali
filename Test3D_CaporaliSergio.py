"""
Autor: Sergio Caporali Ramirez
Fecha: 03/Febrero/2021
Evaluación 3D

"""
import matplotlib.pyplot as plt 
import numpy as np
from math import sqrt 
import sys
import keyboard as k


#___Arreglo

x=[30,40,80,10,40]
y=[10,60,60,10,75]
z=[-10,10,10,0,0]

#Ploteo de la figura

def plotPlaneLine(xg,yg,zg,bandera,ABase,A1,A2):

    #Tamaño del grid
    #Nombre
    plt.title('Test3D')

    plt.axis([0,150,100,0])
    plt.axis('on')
    plt.grid(True)
    plt.xlabel('Eje x')
    plt.ylabel('Eje y')

    #__BASE
    plt.plot([x[0],x[1]],[y[0],y[1]],color='k')
    plt.plot([x[1],x[2]],[y[1],y[2]],color='k')
    plt.plot([x[2],x[0]],[y[2],y[0]],color='k')

    #__Lados del triangulo

    plt.plot([x[0],x[3]],[y[0],y[3]],linestyle=':',color='r')
    plt.plot([x[3],x[1]],[y[3],y[1]],linestyle=':',color='k')
    plt.plot([x[3],x[2]],[y[3],y[2]],linestyle=':',color='b')

    #__Linea de intersección

    plt.plot([x[3],x[4]],[y[3],y[4]],color='k')

    if(bandera==True):
        plt.text(100,60,'Dentro del plano')
    else:
        plt.text(100,60,'Fuera del plano')

    ABase = int(ABase)
    A1 = int(A1)
    A2 = int(A2)

    plt.text(100,25,'Area base=')
    plt.text(125,25,ABase)
    plt.text(100,35,'Area 1=')
    plt.text(120,35,A1)
    plt.text(100,40,'Area 2=')
    plt.text(120,40,A2)
    plt.text(100,50,'Area1 + Area2=')
    plt.text(135,50,A1+A2)
    plt.show()

def hitpoint(x,y,z):

    #Base del triangulo

    #Distancia (0,1)
    a=x[1]-x[0]
    b=y[1]-y[0]
    c=z[1]-z[0]
    D01=sqrt(a*a+b*b+c*c) 
    
    #Distancia (1,2)
    a=x[2]-x[1]
    b=y[2]-y[1]
    c=z[2]-z[1]
    D12=sqrt(a*a+b*b+c*c) 

    #Distancia (0,2)

    a=x[2]-x[0]
    b=y[2]-y[0]
    c=z[2]-z[0]
    D02=sqrt(a*a+b*b+c*c)

    #Formula de Heron

    s=(D01+D12+D02)/2
    ABase=sqrt(s*(s-D01)*(s-D12)*(s-D02))
        
    #Triangulo 1

    #Distancia (0,1)
    a=x[1]-x[0]
    b=y[1]-y[0]
    c=z[1]-z[0]
    D01=sqrt(a*a+b*b+c*c)

    #Distancia (0,2)
    a=x[3]-x[1]
    b=y[3]-y[1]
    c=z[3]-z[1]
    D13=sqrt(a*a+b*b+c*c) 

    #Distancia (0,3)
    a=x[3]-x[0]
    b=y[3]-y[0]
    c=z[3]-z[0]
    D03=sqrt(a*a+b*b+c*c)

    #__Área con formula de Heron

    s=(D01+D13+D03)/2
    A1=sqrt(s*(s-D01)*(s-D13)*(s-D03))

    #Triangulo 2
    
    #Distancia (0,2)

    a=x[2]-x[0]
    b=y[2]-y[0]
    c=z[2]-z[0]
    D02=sqrt(a*a+b*b+c*c) 

    #Distancia (2,3)
    a=x[3]-x[2]
    b=y[3]-y[2]
    c=z[3]-z[2]
    D23=sqrt(a*a+b*b+c*c) 

    #Distancia (0,3)

    a=x[3]-x[0]
    b=y[3]-y[0]
    c=z[3]-z[0]
    D03=sqrt(a*a+b*b+c*c)

    #__Área con formula de Heron
    s=(D02+D23+D03)/2
    A2=sqrt(s*(s-D02)*(s-D23)*(s-D03))

    #__Hitpoint

    sumaAreas = A1+A2
    bandera = True
    if(ABase>sumaAreas):
        bandera = True
    else:
        bandera = False
    
    #Plotear figuras
    #Etiquetas
    plotPlaneLine(x,y,z,bandera,ABase,A1,A2)

#Dátos
#Hitpoint


print("Enter para continuar o esc para salir")

while True:
    
    if keyboard.is_pressed('esc'):
        sys.exit(0)
    if keyboard.is_pressed('Enter'):
        tecla=input('-----')
        hx=input("punto X :")
        hy=input("punto Y :")

        #Arreglos
        x[3]=int(hx)
        y[3]=int(hy)
        hitpoint(x,y,z)
        print("Enter para continuar o ESC para salir")