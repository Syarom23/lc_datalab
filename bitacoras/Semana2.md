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

## Diseñar antes de programar
Define:

>Entrada
- ¿Qué dato recibe DataLab?
> Datalab recibe un número y lo compara con los límites establecidos


Reglas:
- ¿Qué condiciones debe evaluar?
> Si el número es menor que el límite inferior, está por debajo. Si se encuentra entre los dos limites, está dentro del rango. Si es mayor que el límite superior, está por encima.

Salidas:
- ¿Qué clasificación debe producir?
> Si el valor esta exactamente en uno de los límites, se considera dentro del rango.

## Pseudocódigo
INICIO

 Leer temperatura 

 Si temperatura esta por encima del límite máximo

     Clasificar como ALTO-RECALENTAMIENTO 

SINO Si temperatura esta por debajo del límite mínimo
      
      Clasificar como BAJO-MOTOR FRIO  
SINO 
       
       Clasificar como NORMAL
 Mostrar clasificación 

FIN

## Diagrama de flujo

    
                          INICIO
                            ↓
                     Leer temperatura
                            ↓
                ¿Temperatura > Límite máximo?
                /                           \
               Sí                           No
     Clasificar como          ¿Temperatura < Límite mínimo
              /                              \
    ALTO- RECALENTAMIENTO              Clasificar como     
                                                                            
                                               
                             ↓
                    Mostrar clasificación
                            ↓
                           FIN
          

 ## Implementar if, elif, else
 - Explica qué sucedería si:

- valor es menor que el límite
> Resultado: La variable clasificación toma el valor de "BAJO".
- valor es igual al límite.
>Resultado: La variable clasificación toma el valor de "NORMAL"
- valor está entre los límites.
> Resultado: La variable clasificación toma el valor de "NORMAL"
- valor supera el límite.
> Resultado: La variable clasificación toma el valor de "ALTO"


