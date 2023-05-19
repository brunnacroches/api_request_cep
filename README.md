Exercício N°10:

- Monte uma API utilizando a framework Flask que requisite a outra API em anexo presente
(request_module):

- Crie uma rota que, ao ser chamada, utilize a biblioteca Requests para chamar a API em
anexo e retorne as informações coletadas em POST “/request”. Tal rota deve tratar o caso de
resposta Ok (200) e Erro (500)

- Observações importantes!

- O projeto deve ser salvo e armazenado em um repositório no GitHub

- Deixe os arquivos necessários (.sql) no projeto se necessário
- O projeto deve possuir interação HTTP em Flask.

## Estrutura do Projeto

├── README.md
├── __init__.py
├── run.py
├── src
│   ├── __init__.py
│   ├── controllers
│   │   ├── __init__.py
│   │   ├── user_registration_controller.py
│   │   ├── cpf_verification_controller.py
│   │   └── cep_verification_controller.py
│   ├── data
│   │   ├── __init__.py
│   │   └── interfaces
│   │       ├── __init__.py
│   │       ├── cpf_api_consumer.py
│   │       └── cep_api_consumer.py
│   ├── error_handling
│   │   ├── __init__.py
│   │   ├── http_request_error.py
│   │   ├── validation_error.py
│   │   ├── validation_error_controller.py
│   │   └── validation_error_view.py
│   ├── infra
│   │   ├── __init__.py
│   │   ├── configs
│   │   │   ├── __init__.py
│   │   │   ├── configs.py
│   │   │   └── connection.py
│   │   ├── entities
│   │   │   ├── __init__.py
│   │   │   ├── user_entity.py
│   │   ├── repository
│   │   │   └── user_repository.py
│   │   └── requests
│   │       ├── __init__.py
│   │       ├── cpf_api_consumer.py
│   │       ├── cep_api_consumer.py
│   │       └── test_api_consumers.py
│   ├── main
│   │   ├── __init__.py
│   │   ├── composer
│   │   │   ├── __init__.py
│   │   │   ├── user_registration_composer.py
│   │   │   ├── cpf_verification_composer.py
│   │   │   └── cep_verification_composer.py
│   │   └── server
│   │       ├── __init__.py
│   │       ├── routes.py
│   │       └── server.py
│   ├── validations
│   │   ├── __init__.py
│   │   ├── validate_user_registration.py
│   │   ├── validate_cpf_verification.py
│   │   └── validate_cep_verification.py
│   └── view
│       ├── __init__.py
│       ├── user_registration_view.py
│       ├── cpf_verification_view.py
│       └── cep_verification_view.py

PROMPT:
Seguindo essa estrutura vou criar um projeto de cadastro de usuário que consume duas apis externas, são duas apis diferentes, uma é para verificar se o CPF digitado do usuário é válido e oura se  CEP existe se ele vai auto completar nos campos, então  ela vai ter duas rotas, rota de autenticar o CPF e rota pra atenticar o CEP durante o cadastro do usuário
