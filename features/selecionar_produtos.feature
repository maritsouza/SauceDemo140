Feature: Selecionar Produto

    Scenario: Selecionar produto "Sauce Labs Backpack"
        Given que acesso o site Sauce Demo 
        When preencho os campos de login com usuario standard_user e senha secret_sauce
        Then sou direcionado para pagina Home
        
    Scenario: Login com a senha invalida
        Given que entro no site Sauce Demo
        When preencho os campos de login com usuario standard_user e senha abacate123
        Then exibe a mensagem de erro no login

    Scenario Outline: Login negativo
            Given que entro no site Sauce Demo
            When preencho os campos de login com usuario <usuario> e senha <senha>
            Then exibe a <mensagem> de erro no login

            Examples:
            
            | id | usuario       | senha        | mensagem                                                                  |
            | 01 | standard_user | abacate123   | Epic sadface: Username and password do not match any user in this service |
            | 02 | standard_user |              | Epic sadface: Password is required                                        |
            | 03 |               | secret_sauce | Epic sadface: Username is required                                        |
            | 04 | kira          | secret_sauce | Epic sadface: Username and password do not match any user in this service |
            | 05 | kira          | abacate123   | Epic sadface: Username and password do not match any user in this service |
            | 06 | kira          |              | Epic sadface: Password is required                                        |
            | 07 |               |              | Epic sadface: Username is required                                        |
            | 08 |               | abacate123   | Epic sadface: Username is required                                        |

