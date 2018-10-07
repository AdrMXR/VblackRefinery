from tools.Console import Console
import sys
import signal

salida = False

def salir(signum, frame):
    global salida
    salida = True
    sys.exit()
 
signal.signal(signal.SIGINT, salir)

if __name__ == "__main__":
    consola = Console()
    consola.evaluar_argumentos()
    