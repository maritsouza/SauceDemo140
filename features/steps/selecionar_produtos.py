# 1 -Bibliotecas / Imports
import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given(u'que acesso o site Sauce Demo')
def step_impl(context):
    # Setup / Inicialização
    context.driver = webdriver.Edge()                   # Instanciar o objeto do Selenium WebDriver especializado para o Edge
    context.driver.maximize_window()                    # Maximiza a janela do navegador
    context.driver.implicitly_wait(10)                  # Define o tempo de espera padrão por elementos de 10 segundos
    # Passo em si
    context.driver.get("https://www.saucedemo.com")     # Abre o navegador e acessa a URL
    
@when(u'preencho os campos de login com usuario {usuario} e senha {senha}')
def step_impl(context, usuario, senha):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)
    context.driver.find_element(By.ID, "password").send_keys(senha)
    context.driver.find_element(By.ID, "login-button").click()

@then(u'sou direcionado para pagina Home')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".Title").text == "Products"
    # time.sleep(2)                                     # Aguarda 2 segundos para visualização - remover depois = alfinete
    
    #teardown / encerramento
    context.driver.quit()
    
    