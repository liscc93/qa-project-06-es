<h2>Lisbeth Cuevas - Sprint 6 </h2>

<h1>Proyecto 6 - Comienzo de automatización de pruebas</h1>

<h2>Descripción del proyecto 6 </h2>

<h4>La finalidad principal de este proyecto radica en optimizar y simplificar el procedimiento de pruebas específicamente diseñado para el campo "name", mediante la implementación de herramientas de automatización. Este campo, caracterizado por su variabilidad en la cantidad de caracteres, así como la inclusión de caracteres especiales y numéricos, presenta un desafío considerable en términos de verificación manual. Por consiguiente, la automatización se convierte en un recurso esencial para agilizar este proceso y garantizar su precisión. Dependiendo de las necesidades particulares de cada caso, se establecerán criterios y protocolos para la validación exhaustiva de los datos ingresados en este campo, asegurando así la integridad y coherencia de la información. 

En este proyecto se llevarán a cabo tanto pruebas positivas como negativas para verificar el cumplimiento de las especificaciones y garantizar la exitosa creación del usuario, así como para evitar errores con entradas no válidas. La automatización de estas pruebas permite minimizar errores humanos y ahorrar tiempo de manera eficiente.

Este proyecto utiliza la documentación suministrada por ApiDoc como base para establecer las especificaciones de la funcionalidad y asegurar que estén alineadas con los requisitos del sistema.</h4>


<h2>Pasos para ejecutar las pruebas:</h2>

<h3>1. Necesitas tener instalados los paquetes pytest y request para ejecutar las pruebas.</h3>
<li> Primero, ve a la opción "Python Packages" que encuentras en la parte inferior izquierda de PyCharm </li>
<li> Segundo, busca en la sección de la lupa los paquetes. </li>
<li> Tercero, instala la versión más actualizada de los paquetes.</li>

<h3>2. Ejecuta las pruebas.</h3>
<li>Asegurate que la URL que se encuentra en el archivo configuration.py y está actualizada.</li>
<li>Ahora puedes correr las pruebas con el comando "pytest" seguido del nombre del archivo que contiene las pruebas.</li>


<h2>Comprobación</h2>

<table>

<tr>
<th> # </th> 
<th> Descripción </th>
<th> ER: </th>
</tr>

<tr>
<td>1</td>
<td> El número permitido de caracteres (1): </td>
<td> Código de respuesta: 201 </td>
</tr>

<tr>
<td>2</td>
<td> El número permitido de caracteres (511): </td>
<td> Código de respuesta: 201 </td>
</tr>

<tr>
<td>3</td>
<td> El número de caracteres es menor que la cantidad permitida (0): </td>
<td> Código de respuesta: 400 </td>
</tr>

<tr>
<td>4</td>
<td> El número de caracteres es mayor que la cantidad permitida (512): </td>
<td> Código de respuesta: 400 </td>
</tr>

<tr>
<td>5</td>
<td> Se permiten caracteres especiales: </td>
<td> Código de respuesta: 201 </td>
</tr>

<tr>
<td>6</td>
<td> Se permiten espacios: </td>
<td> Código de respuesta: 201 </td>
</tr>

<tr>
<td>7</td>
<td> Se permiten números: </td>
<td> Código de respuesta: 201 </td>
</tr>

<tr>
<td>8</td>
<td> El parámetro no se pasa en la solicitud: </td>
<td> Código de respuesta: 400 </td>
</tr>

<tr>
<td>9</td>
<td> Se ha pasado un tipo de parámetro diferente (número): </td>
<td> Código de respuesta: 400 </td>
</tr>

</table>


 

