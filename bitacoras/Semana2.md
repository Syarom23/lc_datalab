# Bitacora semana 2 

## Concepto central
- ¿Qué significa una condición?
> Es una pregunta que el programa puede responder como verdadera o falsa. 
> Ejemplo: edad >= 18.
- ¿Qué ocurre cuando es verdadera?
> El programa ejecuta las instrucciones que corresponden a esa condición 
- ¿Qué ocurre cuando es falsa?
> El programa para a revisar otra condición (elif) o ejecuta else si ninguna cumple.
- ¿Por qué puede haber varias alternativas?
> Porque un problema puede tener mas de dos posibles resultados. Por ejemplo, un numero puede estar por debajo, dentro o por encima del rango.
## Actividad Feynman
> Explica esta situación sin utilizar código:
DataLab recibe un valor y debe determinar si está por debajo, dentro o por encima de un rango esperado.
Explícalo como si la persona que te escucha nunca hubiera programado.
- ¿Cuántos caminos existen?
>Datalab recibe un número y lo compara con los límites establecidos. Si el numero es menor que el limite inferior, esta por debajo. Si se encuentra entre los dos limites, esta dentro del rango. Si es mayor que el limite superior, esta por encima. Para tomar estas decisiones se utilizan varias conficiones.
> La lógica seria 
> Valor < límite inferior = por debajo
> Valor entre los limites = Dentro
> Valor > limite superior = por encima


- ¿Qué condición permite seleccionar cada camino?
> Se compara el valor con los límites del rango. Si es menor que el limite inferior, va por el primer camino, si esta dentro del rango, va por el segundo, y si es mayor que el limite superior, va por el tercero
- ¿Qué ocurre si el valor está exactamente en el límite?
> Si el valor esta exactamente en uno de los límites, se considera dentro del rango, siempre que los límites estén incluidos
