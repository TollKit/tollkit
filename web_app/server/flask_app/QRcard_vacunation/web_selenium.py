from dataclasses import dataclass
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from time import sleep
import unittest

def main():
    website='https://carnetvacunacion.minsa.gob.pe/#/verify-qr/enable'
    #Determinar la ruta, path es la ruta
    
    path='D:/Jhomar/IoT Challege/chromedriver.exe'
    #Definir variable, abrir automáticamente
    driver=webdriver.Chrome(path)
    #Abrir la página
    driver.get(website)
    time.sleep(15)
    nombre=driver.find_element(by='xpath',value="/html/body/app-root/app-verify-qr/div/div/app-result/div/div/div[2]/div/div/div[1]/div[1]/div[3]/span")
    # print("--")
    # print(type(nombre.text))
    # print(nombre.text)
    dosis=driver.find_element(by='xpath',value="/html/body/app-root/app-verify-qr/div/div/app-result/div/div/div[2]/div/div/div[1]/div[1]/div[5]/h3[2]")
    # print(type(dosis.text))
    # print(dosis.text)
    edad=driver.find_element(by='xpath', value="/html/body/app-root/app-verify-qr/div/div/app-result/div/div/div[2]/div/div/div[1]/div[1]/div[4]/span[2]")
    lista_edad=edad.text.split(' ')
    probar_edad=int(lista_edad[1])
    # print(int(probar_edad))
    #if(dosis.text!='CON TERCERA DOSIS'):
        
    data=[nombre.text,dosis.text,probar_edad]
    return data
main() 