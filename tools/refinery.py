import sqlite3

class refinery:
    def __init__(self):
        self.database_file = "refinery.db"
        self.conn = sqlite3.connect(self.database_file)
        self.archivo_entrada = None

    def refinar_datos(self):
        self.conn.execute("CREATE TABLE IF NOT EXISTS login (id INTEGER PRIMARY, email text NOT NULL, password TEXT NOT NULL, icloud NUMERIC NOT NULL, logMail NUMERIC NOT NULL)")
        inputArch = open(self.archivo_entrada, 'r')
        for inputArch in  
        self.conn.execute("INSERT INTO login")