1. ¿Cuántas veces se ejecuta `validar_nombre()`?
>5 veces
2. ¿Cuántas veces se ejecuta el `if`?
>5 veces
3. ¿Qué parte cambia en cada iteración?
>el número
4. ¿Qué parte permanece igual?
>ingrese el nombre


# Indicador de calidad
>Determina el resultado antes de ejecutarlo en Python.
 
 calidad =17/20x100

 17/20=0,85

 0,85x100=85,0



# Reto integrador DataLab


¿Cuántos registros desea procesar? 10


El programa debe procesar los diez registros mediante un ciclo.

## Preguntas de reflexión


# ¿Qué problema resuelve un ciclo?
>Evita la duplicación manual de código (copiar y pegar) cuando se necesita ejecutar una misma secuencia de instrucciones múltiples veces sobre distintos datos.   ¿Por qué range(5) produce cinco iteraciones?Porque genera una secuencia de 5 números enteros comenzando en 0 hasta 4 (0, 1, 2, 3, 4), completando un total de 5 pasos.  
# ¿Qué diferencia existe entre una función y un ciclo?
>Una función encapsula y reutiliza un bloque de código lógica específico cuando es invocada, mientras que un ciclo repite la ejecución de un bloque de código consecutivamente un número determinado de veces.  
# ¿Por qué una validación debería ser una función reutilizable?
>Para asegurar la consistencia de las reglas de negocio en todo el programa, evitar errores al modificar lógica en múltiples lugares y mantener un código limpio (principio DRY: Don't Repeat Yourself). 
#  ¿Por qué separar las validaciones en un módulo?
>Para aplicar el principio de separación de responsabilidades, facilitando la mantenibilidad, escalabilidad, legibilidad y realización de pruebas unitarias sobre el código.   
# ¿Qué función cumplen los contadores?
>Almacenan y acumulan la cantidad de ocurrencias de un evento específico (por ejemplo, número de registros válidos o inválidos) a lo largo del flujo del ciclo. 
#  ¿Qué diferencia existe entre procesar un registro y procesar muchos registros?
>Procesar un registro ejecuta la lógica linealmente una vez. Procesar muchos registros requiere control de estructuras iterativas (ciclos), acumulación de estados/métricas globales e indicadores agregados de calidad de datos.  
# ¿Qué ocurre si cambia una regla de validación?
>Si está modulada en una función dentro de validaciones.py, solo se modifica esa función en un solo lugar y todo el sistema que la utiliza adopta el cambio inmediatamente sin alterar la lógica de los ciclos.  
# ¿Por qué no conviene copiar y pegar una validación?
>Porque genera duplicación de código, aumenta la probabilidad de introducir inconsistencias o errores y dificulta el mantenimiento cuando la regla necesite actualizarse.  
# ¿Cómo contribuye esta arquitectura al crecimiento de DataLab?
>Permite escalar la aplicación desde scripts básicos hasta flujos de datos complejos (ETL/pipelines) mediante un diseño modular donde cada componente tiene una responsabilidad bien definida.   