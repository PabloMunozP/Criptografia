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
    Browser.get("https://www.bbc.com/")
    time.sleep(3)

def login(username,password):#Inicia sesion en la pagina elegida
    if Browser.current_url == "https://www.bbc.com/":
        login= Browser.find_element_by_xpath("//*[@id='idcta-link']")
        Browser.execute_script("arguments[0].click();",login)
        time.sleep(2)
        
    user= WebDriverWait(Browser,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='user-identifier-input']")))
    user.send_keys(Keys.CONTROL + 'a')
    user.send_keys(Keys.DELETE)
    user.send_keys(username)
    time.sleep(3)

    pwd=WebDriverWait(Browser,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='password-input']")))
    pwd.send_keys(Keys.CONTROL + 'a')
    pwd.send_keys(Keys.DELETE)
    pwd.send_keys(password)
    pwd.send_keys(Keys.ENTER)
    time.sleep(3)

def resetPassword(username):
    login= Browser.find_element_by_xpath("//*[@id='idcta-link']")
    Browser.execute_script("arguments[0].click();",login)
    time.sleep(2)

    user= WebDriverWait(Browser,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='signin-page']/div[2]/div[2]/div[2]/div[1]/form/p/a")))
    Browser.execute_script("arguments[0].click();",user)
    time.sleep(1)
    
    user= WebDriverWait(Browser,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='container']/div/div/div/div[2]/div[2]/div[2]/div/ul/li[1]/a")))
    Browser.execute_script("arguments[0].click();",user)

    user= WebDriverWait(Browser,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='user-identifier-input']")))
    user.send_keys(username + Keys.ENTER)
    time.sleep(1)

def changePassword(username,password,newPassword):
    login(username,password)
    user = WebDriverWait(Browser,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='idcta-link']")))
    Browser.execute_script("arguments[0].click();",user)
    time.sleep(1)

    user = WebDriverWait(Browser,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='container']/div/div/div[1]/div[1]/div/div/div/div/nav/ul/li[2]/a")))
    Browser.execute_script("arguments[0].click();",user)
    time.sleep(1)

    #            A veces solicita reingresar la contraseña para confirmar la identidad.
    #user = WebDriverWait(Browser,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='password-input']")))
    #user.send_keys(password + Keys.ENTER)
    #time.sleep(1)

    user = WebDriverWait(Browser,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='Password-field']/div[2]/a")))
    Browser.execute_script("arguments[0].click();",user)
    time.sleep(1)

    user = WebDriverWait(Browser,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='current-password-input']")))
    user.send_keys(password)

    user = WebDriverWait(Browser,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='new-password-input']")))
    user.send_keys(newPassword)

    user = WebDriverWait(Browser,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='app-container']/div/div/div[2]/div[2]/div[2]/div/div[2]/form/div[3]/button")))
    Browser.execute_script("arguments[0].click();",user)
    time.sleep(1)

def createAcc(username,password,birth=[8,8,1990]):
    login= Browser.find_element_by_xpath("//*[@id='idcta-link']")
    Browser.execute_script("arguments[0].click();",login)
    time.sleep(2)

    
    user = WebDriverWait(Browser,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='signin-page']/div[2]/div[2]/div[2]/div[2]/a")))
    Browser.execute_script("arguments[0].click();",user)

    user = WebDriverWait(Browser,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='container']/div/div/div/div[2]/div[2]/div[2]/div/div[3]/fieldset/div[1]/a[2]")))
    Browser.execute_script("arguments[0].click();",user)

    user = WebDriverWait(Browser,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='day-input']")))
    user.send_keys(birth[0])

    user = WebDriverWait(Browser,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='month-input']")))
    user.send_keys(birth[1])

    user = WebDriverWait(Browser,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='year-input']")))
    user.send_keys(birth[2])
    user.send_keys(Keys.ENTER)

    user = WebDriverWait(Browser,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='user-identifier-input']")))
    user.send_keys(username)

    user = WebDriverWait(Browser,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='password-input']")))
    user.send_keys(password)
    user.send_keys(Keys.ENTER)

    user = WebDriverWait(Browser,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='optOut']")))
    Browser.execute_script("arguments[0].click();",user)

    user = WebDriverWait(Browser,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='submit-button']")))
    Browser.execute_script("arguments[0].click();",user)
    time.sleep(1)

def close():
    Browser.close()

def fuerzaBruta(email,base="abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789,",intentos=100,largoMin=8):
    chars=[]
    for char in base:
        chars.append(char)
    contador=0
    for tam in range(largoMin,len(chars)):
        for pwd in itertools.product(chars,repeat=tam):
            if contador <= intentos:
                print('Intento:',contador, 'clave:',pwd)
                login(email,pwd)
            else:
                break                
            time.sleep(2)
            contador += 1

if __name__=="__main__":
    setBrowser()
    #createAcc("pruebacripto2@yopmail.com","contra123.")
    #login("pruebacripto2@yopmail.com","contra123.")
    #changePassword("pruebacripto2@yopmail.com","contra123.","nuevaContra123.")
    #resetPassword("pruebacripto2@yopmail.com")
    #fuerzaBruta("pruebacripto2@yopmail.com")
    time.sleep(2)
    close()



    
