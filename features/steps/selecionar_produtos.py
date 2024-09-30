# 1 -Bibliotecas / Imports
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given(u'que entro no site Sauce Demo')
@given(u'que acesso o site Sauce Demo')
def step_impl(context):
    # Setup / Inicialização
    context.driver = webdriver.Edge()                   # Instanciar o objeto do Selenium WebDriver especializado para o Edge
    context.driver.maximize_window()                    # Maximiza a janela do navegador
    context.driver.implicitly_wait(10)                  # Define o tempo de espera padrão por elementos de 10 segundos
    # Passo em si
    context.driver.get("https://www.saucedemo.com")     # Abre o navegador e acessa a URL

#Preencher com usuário e senha  
@when(u'preencho os campos de login com usuario {usuario} e senha {senha}')
def step_impl(context, usuario, senha):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)
    context.driver.find_element(By.ID, "password").send_keys(senha)
    context.driver.find_element(By.ID, "login-button").click()
    
# Usuário em branco e preencher a senha
@when(u'preencho os campos de login com usuario  e senha {senha}')
def step_impl(context, senha):
    # Não preenche o usuário
    context.driver.find_element(By.ID, "password").send_keys(senha)
    context.driver.find_element(By.ID, "login-button").click()

# Preencher com usuário, mas deixar a senha em branco   
@when(u'preencho os campos de login com usuario {usuario} e senha ')
def step_impl(context, usuario):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)
    # Não preencho a senha
    context.driver.find_element(By.ID, "login-button").click()
    
# Clica no botão de login sem ter preencido os campos de usuário e senha
@when(u'preencho os campos de login com usuario  e senha ')
def step_impl(context):
    # Não preenche o usuário
    # Não preencho a senha
    context.driver.find_element(By.ID, "login-button").click()

@then(u'sou direcionado para pagina Home')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"
    # time.sleep(2)                                     # Aguarda 2 segundos para visualização - remover depois = alfinete
    
    # teardown / encerramento
    context.driver.quit()
    
@then(u'exibe a mensagem de erro no login')
def step_impl(context):
    # Validar a mensagem de erro
    assert context.driver.find_element(By.CSS_SELECTOR, "h3").text == "Epic sadface: Username and password do not match any user in this service"
    
    # teardown / encerramento
    context.driver.quit()


# Verifica a mensagem para o Scenario Outline
@then(u'exibe a {mensagem} de erro no login')
def step_impl(context, mensagem):
    # Validar a mensagem de erro
    assert context.driver.find_element(By.CSS_SELECTOR, "h3").text == mensagem
    
    # teardown / encerramento
    context.driver.quit()