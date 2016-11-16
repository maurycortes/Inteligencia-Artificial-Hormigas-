from operacion import *
from maquina import *
from trabajo import *
from vecino import *
from functions import *
import sys
import copy
import random
import pdb

print "nombre caso"
print "nmaquinas"
print "ntrabajos"
print "maxoperaciones"
print "maxmtiempo"

archivocaso = open(raw_input(), 'w')

nmaquinas = int(raw_input())
ntrabajos = int(raw_input())
maxoperaciones = int(raw_input())
maxtiempo = int(raw_input())

idmaquinas = "m0"
for i in range(1, nmaquinas):
	idmaquina = "m"+str(i)
	idmaquinas = idmaquinas + "," + idmaquina

maquinas = idmaquinas.split(",")

idmaquinas = idmaquinas + "\n"

archivocaso.write(idmaquinas)
archivocaso.write(str(ntrabajos) + "\n")

for i in range(0, ntrabajos):
	idtrabajo = "j"+str(i)
	archivocaso.write(idtrabajo + "\n")
	noperaciones = random.randrange(1, maxoperaciones+1)
	archivocaso.write(str(noperaciones) + "\n")
	for j in range(0, noperaciones):
		idoperacion = "O" + str(i) + str(j) + "\n"
		archivocaso.write(idoperacion)
		tiempo = str(random.randrange(0, maxtiempo + 1)) + "\n"
		archivocaso.write(tiempo)
		dependencia = str(j) + "\n"
		archivocaso.write(dependencia)
		maqrand = random.randrange(0, nmaquinas)
		maquina = maquinas[maqrand] + "\n"
		archivocaso.write(maquina)
