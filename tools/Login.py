import smtplib
import imaplib
from pyicloud import PyiCloudService
class Login:
    def __init__(self):
        self.email = "valdr.stiglitz@gmail.com"
        self.password = "012345678"
        self.icloud = False
        self.logMail = False
        self.servidores = {"gmail":["@gmail.com"],"yahoo":["@yahoo.com","@yahoo.com.mx"],"outlook":["@hotmail.com","@outlook.com","@hotmail"]}
        self.servidor = "outlook"
    
    def definirServidorMail(self):
        if "@"+self.email.split("@")[1] in self.servidores["gmail"]:
            self.servidor = "gmail"
        elif "@"+self.email.split("@")[1] in self.servidores["yahoo"]:
            self.servidor = "yahoo"
        elif "@"+self.email.split("@")[1] in self.servidores["outlook"]:
            self.servidor = "outlook"
    
    def checkLoginGmail(self):
        smtpserver = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtpserver.ehlo()
        try:
            smtpserver.login(self.email, self.password)
            self.logMail = True
        except Exception as e:
            codigo = str(e)[1:].split(',')[0]
            if codigo == '534' and len(str(e)[1:].split(',')[1]) > 200:
                self.logMail = True
            else:
                self.logMail = False

    def checkLoginYahoo(self):
        server = imaplib.IMAP4_SSL("imap.mail.yahoo.com", 993)
        try:
            server.login(self.email, self.password)
            self.logMail = True
        except:
            self.logMail = False

    def checkLoginMS(self):
        server = imaplib.IMAP4_SSL("imap-mail.outlook.com", 993)
        try:
            server.login(self.email, self.password)
            self.logMail = True
        except:
            self.logMail = False

    def checkLoginiCloud(self):
        try:
            icloud = PyiCloudService(email,contra)
            self.icloud = True
        except:
            self.icloud = False