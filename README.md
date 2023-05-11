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

├── backend
│   ├── app.py               # Arquivo principal da aplicação
│   ├── requirements.txt     # Lista de dependências do projeto
│   ├── src                  # Código-fonte do projeto
│   │   ├── __init__.py
│   │   ├── controllers      # Lógica de negócios e manipulação de dados
│   │   ├── error_handling   # Manipulação de erros e exceções
│   │   ├── infra            # Camada de infraestrutura (ex. banco de dados, serviços externos)
│   │   ├── validators       # Validação de dados e entrada do usuário
│   │   └── views            # Camada de apresentação e interação com o usuário (ex. API, templates)
