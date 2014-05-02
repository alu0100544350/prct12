#!/usr/bin/python
#!encoding: UTF-8
import sys
import time
import modulo12
     


argumentos=sys.argv[1:]
if(len(argumentos)==8):
    n=int(argumentos[0])
    aproxima=int(argumentos[1])
    umbral=[]
    for i in range(2,7):
      umbral.append(float(argumentos[i]))
    nombre_fichero=argumentos[7]
else:
    print"Introduzca el nº de intervalos (n>0) : "
    n=int(raw_input())
    print"introduzca el nº de aproximaciones : "
    aproxima=int(raw_input())
    print"introduzca los 5 umbrales de error:"
    umbral=[]
    for i in range(5):
      print"introduzca el umbral",i,":"
      umbral.append(float(raw_input()));
    print"introduzca el nombre del fichero para almacenar los resultados:"
    nombre_fichero=raw_input();
    
if(n>0):
  
  try:
    fichero=open(nombre_fichero,"a")
  except:
    fichero=open(nombre_fichero,"w")
  fichero.write("Nº de intevalos: %d\n" %(aproxima))
  for i in range(5):
    start=time.time()
    porcentaje=modulo12.error(n,aproxima,umbral[i])
    finish=time.time()-start
    fichero.write("%2.2f%% de fallos para el umbral %2.5f\n" %(porcentaje,umbral[i]))
    fichero.write(str(finish))
  fichero.close()
   




 