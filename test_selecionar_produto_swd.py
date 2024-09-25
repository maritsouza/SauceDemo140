# 1 - Bibliotecas
from selenium import webdriver
from selenium.webdriver.common.by import By

# 2 - Classe (Opcional) o python não exige que você crie uma classe, mas é uma boa prática.
class Teste_Produtos(): 
    
    # 2.1 Atributos
    url = "https://www.saucedemo.com"                    # URL do site a ser testado
    
    # 2.2 Funções e Métodos (Método simples não precisa ter retorno, função é obrigada ter retorno, precisa devolver o resultado)

    def setup_method(self, method):                      # Método de inicialização dos testes
        self.driver = webdriver.Edge()                   # Instanciar o objeto do Selenium WebDriver como Edge
        self.driver.implicitly_wait(10)                  # Define o tempo de espera padrão por elementos de 10 segundos
        
    def teardown_method(self, method):                   # Método de finalização dos testes
        self.driver.quit()                               # Encerra / destrói o objeto do Selenium WebDriver da memória
        
    def test_selecionar_produto(self):                   # Método de teste
        self.driver.get(self.url)                        # Abre o navegador e acessa a URL
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")               # Escreve no campo de usuário
        self.driver.find_element(By.NAME, "password").send_keys("secret_sauce")               # Escreve no campo de senha
        self.driver.find_element(By.CSS_SELECTOR, "input.submit-button.btn_action").click()   # Clique no botão de login
        
        # Transição para a página de produtos

        assert self.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"               # Confirma se o elemento é "Products"
        assert self.driver.find_element(By.ID, "item_4_title_link").text == "Sauce Labs Backpack"   # Confirma se o elemento é a mochila
        # Confirma o preço da mochila
        assert self.driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(1) .inventory_item_price").text == "$29.99"