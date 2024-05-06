from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from mapper.xpath import Xpath
from account.email import Email

class TesteAutomatizado():

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:8080")
        self.driver.maximize_window()
    

    #Evento de click
    def waitClick(self, xpath):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        sleep(.5)
        element.click()


    #Evento de entrada de dados 
    def waitInput(self, xpath, valor): 
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        sleep(.5)
        element.send_keys(valor)
    
    #Evento de seleção de dados
    def waitSelect(self, xpath):
        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        sleep(.5)
        return element.text

   
    def getCodeByEmail(self, USER):
        self.driver.execute_script("window.open('https://accounts.google.com', 'login')")
        self.driver.switch_to.window(self.driver.window_handles[1])

        self.waitInput(Xpath.INPUT_EMAIL['USUARIO'] , USER['EMAIL'])
        self.waitClick(Xpath.BTN_EMAIL['AVANSAR'])
        self.waitInput(Xpath.INPUT_EMAIL['SENHA'], Email.SENHA[USER['APELIDO']])
        self.waitClick(Xpath.BTN_EMAIL['LOGAR'])
        
        sleep(2)

        self.driver.execute_script("window.open('https://mail.google.com/mail/u/0/#inbox', 'email')")
        self.driver.switch_to.window(self.driver.window_handles[2])
        self.waitInput(Xpath.INPUT_EMAIL['PESQUISA'], 'Code vBook')
        self.waitClick(Xpath.BTN_EMAIL['PESQUISA'])
        self.waitClick(Xpath.BTN_EMAIL['EMAIL'])
        
        sleep(2)

        codigoEmail = self.waitSelect(Xpath.ELEMENT_EMAIL['CODIGO']).replace(' ', '').split('-')
        
        self.waitClick(Xpath.BTN_EMAIL['LIXEIRA'])
        
        sleep(2)
        
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        return codigoEmail


    def cadastroUsuario(self, USER):
        self.waitClick(Xpath.BTN['USUARIO'])
        self.waitClick(Xpath.BTN['CADASTRAR_SE'])
        self.waitInput(Xpath.INPUT['CADASTRO_APELIDO'], USER['APELIDO'])
        self.waitInput(Xpath.INPUT['CADASTRO_NOME_COMPLETO'], USER['NOME_COMPLETO'])
        self.waitInput(Xpath.INPUT['CADASTRO_EMAIL'], USER['EMAIL'])
        self.waitInput(Xpath.INPUT['CADASTRO_CELULAR'], USER['CELULAR'])
        self.waitInput(Xpath.INPUT['CADASTRO_SENHA'], USER['SENHA'])
        self.waitInput(Xpath.INPUT['CADASTRO_CONFIRMAR_SENHA'], USER['SENHA'])
        self.waitClick(Xpath.BTN['ENVIAR_CADASTRO_USUARIO'])
        
        codigoEmail = self.getCodeByEmail(USER)

        for i in range(len(codigoEmail)):
            self.waitInput(Xpath.INPUT['CADASTRO_CODIGO'][i] , codigoEmail[i])

        self.waitClick(Xpath.BTN['CONFIRMAR_CODIGO'])


    def deletarUsuario(self, USER):
        self.longin(USER)
        self.waitClick(Xpath.BTN['USUARIO'])
        self.waitClick(Xpath.BTN['GERENCIAR'])
        self.waitClick(Xpath.BTN['MINHA_CONTA'])
        self.waitClick(Xpath.BTN['CANCELAR_CONTA'])
        self.waitInput(Xpath.INPUT['CANCELAR_CONTA'], USER['SENHA'])
        self.waitClick(Xpath.BTN['CONFIRMAR_CANCELAR_CONTA'])


    def longin(self, USER):
        self.waitClick(Xpath.BTN['USUARIO'])
        self.waitInput(Xpath.INPUT['ENTRAR_USUARIO'], USER['APELIDO'])
        self.waitInput(Xpath.INPUT['ENTRAR_SENHA'], USER['SENHA'])
        self.waitClick(Xpath.BTN['ENTRAR'])
    

    def getGerenciar(self):
        self.waitClick(Xpath.BTN['USUARIO'])
        self.waitClick(Xpath.BTN['GERENCIAR'])


    ################################## Trabalhando ##################################
    def cadastroLivro(self, LIVRO):
        self.getGerenciar()
        self.waitClick(Xpath.BTN['CRIAR'])
        self.waitInput(Xpath.INPUT['CRIAR_TITULO'], LIVRO['TITULO'])


    
    

