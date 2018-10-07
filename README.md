# VblackRefinery 1.3
Programa para hacer ataque de fuerza bruta y refinacion de datos a servidores de correo (SMTP y IMAP) y apis de redes sociales
- programado por Valdr Stiglitz @ValdrST

### Para correrlo en modo GUI interfaz grafica

`$ python Bblack refineryRefinery.py --gui`


### instrucciones de uso
 
 ```
usage: VblackRefinery.py [-h] [-s SOURCE] [-o OUT] [--email] [--icloud]
                         [--out-text-email] [--gui]

optional arguments:
  -h, --help            show this help message and exit
  -s SOURCE, --source SOURCE
                        archivo de entrada .csv
  -o OUT, --out OUT     archivo de salida .db
  --email               introduce si se va a revisar email
  --icloud              introduce si se va a revisar icloud
  --out-text-email      Crea salida de contraseñas validas email en .txt
  --gui                 Abre el programa en modo GUI
 ```
 
 
- el archivo de entrada csv debe tener el siguiente formato

debe ser el correo con la contraseña separada de una coma puede ser una o varias
 
 ```
 correo@hotmail.com,contrasenya
 correo2@gmail.com,contraseña2
 correo3@yahoo.com,contraseña3
 correo4@outlook.es,contraseña77,password2
 correo2@empresaMS.com,password54,12341231,admin
 ```
 
 

### Caracteristicas del programa
- ¡Interfaz grafica añadida!
- Compatible con los servidores de correo microsoft, yahoo y google(gmail)
- uso del protocolo imap y smtp(solo gmail)
- guardar progreso para procesar listas extensas
- pruebas con icloud
