# FuerzaBrutaEmail 0.3
Programa para hacer ataque de fuerza bruta a servidores de correo (SMTP y IMAP)
- programado por Valdr Stiglitz @ValdrST

### instrucciones de uso

- tener un archivo csv o txt con el siguiente formato.

debe ser el correo con la contraseña separada de una coma puede ser una o varias
 
 ```
 correo@hotmail.com,contrasenya
 correo2@gmail.com,contraseña2
 correo3@yahoo.com,contraseña3
 correo4@outlook.es,contraseña77,password2
 correo2@empresaMS.com,password54,12341231,admin
 ```
 
 - para correrlo se debe iniciar el archivo 
 
 `$ python fuerzaBrutaEmail.py [nombre_del_archivo.csv|txt]`
 
Va a dar como salida un archivo llamado claves.txt con los correos y contaseñas validas por los servidores de correo

### Caracteristicas del programa

- Elimina los correos y contraseñas repetidas
- Compatible con los servidores de correo microsoft, yahoo y google(gmail)
- uso del protocolo imap y smtp(solo gmail)
- guardar progreso para procesar listas extensas
