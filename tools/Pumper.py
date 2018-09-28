import sqlite3

class Pumper:
    def __init__(self, database_file = "refinery.db",archivo_entrada = None):
        self.database_file = database_file
        self.conn = sqlite3.connect(self.database_file)
        self.cursor = self.conn.cursor()
        self.archivo_entrada = archivo_entrada

    def extraer_datos(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS login (id TEXT PRIMARY KEY, email text NOT NULL, password TEXT NOT NULL, icloud NUMERIC NOT NULL, logMail NUMERIC NOT NULL, checkedMail NUMERIC NOT NULL, checkedIcloud NUMERIC NOT NULL)")
        inputArch = open(self.archivo_entrada, 'r')
        lineas = inputArch.readlines()
        for linea in lineas:
            linea = linea.replace("\n",'')
            linea = linea.split(',')
            email = linea[0]
            contras = linea[1:]
            try:
                if len(contras) > 1:
                    if linea[1] not in linea[2:]:
                        for contra in contras:
                            self.insertar_dato(email,contra,0,0,0,0)
                    else:
                        contra = linea[1]
                        self.insertar_dato(email,contra,0,0,0,0)
                elif len(contras) == 1:
                    contra = linea[1]
                    self.insertar_dato(email,contra,0,0,0,0)
            except Exception as e:
                pass
        self.conn.commit()
    
    def select_datos_all(self):
        self.cursor.execute("SELECT * FROM login")
        return self.cursor.fetchall()
    
    def select_datos_checked_icloud(self,check):
        self.cursor.execute("SELECT * FROM login WHERE checkedIcloud="+str(check))
        return self.cursor.fetchall()
    
    def select_datos_checked_mail(self,check):
        self.cursor.execute("SELECT * FROM login WHERE checkedMail="+str(check))
        return self.cursor.fetchall()
    
    def select_datos_logmail(self,check):
        self.cursor.execute("SELECT * FROM login WHERE logmail="+str(check))
        return self.cursor.fetchall()
    
    def select_datos_icloud(self,check):
        self.cursor.execute("SELECT * FROM login WHERE icloud="+str(check))
        return self.cursor.fetchall()

    def insertar_dato(self,email,contra,icloud,logmail,checked,checkedIcloud):
        icloud = str(icloud)
        logmail = str(logmail)
        checked = str(checked)
        checkedIcloud = str(checkedIcloud)
        self.cursor.execute("INSERT INTO login (id, email, password, icloud, logmail,checkedMail,checkedIcloud) VALUES ('"+email+contra+"','"+email+"','"+contra+"',"+icloud+","+logmail+","+checked+","+checkedIcloud+")")

if __name__ == "__main__":
    pump = Pumper(archivo_entrada="correosCandidatos2.txt")
    pump.extraer_datos()
    print(pump.select_datos_all())