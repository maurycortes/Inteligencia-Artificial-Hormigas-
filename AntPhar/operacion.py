"""Clase vacia Operacion
representacion de las operaciones de una tarea
utilizar solo con los siguientes atributos

string idtrabajo
Identificador del trabajo al que pertenece la operacion

string id
Nombre identificador de la operacion

int tiempo
Tiempo restante para terminar la operacion

int dependencia
Entero indicando las dependencias restantes antes de poder ejecutar la operacion. Una
operacion se puede ejecutar si y solo si su grado de dependencia es 0. Cada vez
que se termina una operacion de un tarea, se resta 1 a todas las operaciones de la
misma tarea.

maquina maquina
Maquina donde se debe realizar la operacion"""

class Operacion:
	pass
