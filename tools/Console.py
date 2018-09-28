import sys
import argparse
from tools.refinery import refinery
import threading
class Console:
    def __init__(self):
        self.parser = parser = argparse.ArgumentParser()
        self.parser.add_argument('-s',"--source", help="archivo de entrada .csv")
        self.parser.add_argument("-o","--out",help="archivo de salida .db",default="refinery.db")
        self.parser.add_argument("--email",action="store_true", help="introduce si se va a revisar email")
        self.parser.add_argument("--icloud",action="store_true",help="introduce si se va a revisar icloud")
        self.parser.add_argument("--out-text-email",action="store_true",help="Crea salida de contraseñas validas email en .txt")
        self.args = parser.parse_args()
    
    def evaluar_argumentos(self):
        refineria = refinery(database_file = self.args.out)
        if self.args.source != None:
            refineria.pumper.archivo_entrada = self.args.source
            refineria.pumper.extraer_datos()
            if self.args.out_text_email == True:
                refineria.recuperar_email_validos()
        if self.args.email == True and self.args.icloud == True:
            hilo_email = threading.Thread(target=refineria.checar_emails_login)
            hilo_icloud = threading.Thread(target=refineria.checar_icloud_login)
            hilo_email.start()
            hilo_icloud.start()
            hilo_email.join()
            hilo_icloud.join()
        elif self.args.email == True:
            refineria.checar_emails_login()
            if self.args.out_text_email == True:
                refineria.recuperar_email_validos()
        elif self.args.icloud == True:
            refineria.checar_icloud_login()
        

        