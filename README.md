# API BARCODES
Este projeto foi feito durante a NLW Expert da Rocketseat na trilha com foco em back end com Python

Ele consiste em uma API para autmoatizar o processo de criação de código de barras, que possui a rota HTTP de:
- Criar uma um código de barras (POST: /create_tag)

## Tecnologias usadas
- **Python 3**:
Python é uma linguagem de programação de alto nível conhecida por sua sintaxe clara e legibilidade. Python 3 é a versão mais recente da linguagem, trazendo melhorias em relação às versões anteriores.

- **Flask**:
Flask é um framework leve e flexível para construção de aplicativos web em Python. Ele fornece ferramentas e bibliotecas para ajudar na criação de aplicativos web rápidos e eficientes, seguindo o paradigma de arquitetura MVC (Model-View-Controller) e é amplamente utilizado para criar APIs RESTful e pequenos projetos web.

- **Pylint**:
Pylint é uma ferramenta de análise estática de código para Python que verifica o código em busca de erros, inconsistências e padrões de codificação não conformes. Ele fornece feedback sobre a qualidade do código, ajudando os desenvolvedores a escrever código mais limpo e legível.

- **Pre-commit**:
Pre-commit é uma ferramenta que automatiza a execução de verificações de código e formatação antes de um commit ser feito em um repositório Git. Ele permite configurar ganchos de pré-commit para executar tarefas como linting, verificação de estilo e execução de testes automatizados, ajudando a manter a qualidade do código em um projeto.

- **Python-barcode**:
Python-barcode é uma biblioteca Python que permite a geração de códigos de barras em vários formatos de imagem, como PNG, JPEG, SVG, entre outros. Ele fornece uma interface simples para criar e personalizar códigos de barras em diferentes tipos de aplicações, desde sistemas de inventário até sistemas de gerenciamento de produção.

- **Pillow**:
Pillow é uma biblioteca Python de processamento de imagem que oferece suporte a uma ampla variedade de formatos de imagem e fornece funcionalidades para manipulação de imagens, como redimensionamento, rotação, aplicação de filtros, entre outros. É uma ferramenta poderosa para processamento de imagens em aplicações Python.

- **Pytest**:
Pytest é uma estrutura de teste em Python que simplifica a escrita e execução de testes automatizados. Ele fornece uma sintaxe simples e intuitiva para escrever testes e suporta a execução de testes unitários, testes de integração e testes de aceitação.

- **Cerberus**:
Cerberus é uma biblioteca de validação de dados em Python, projetada para validar estruturas de dados complexas, como dicionários aninhados. Ele fornece uma maneira flexível e expressiva de definir esquemas de validação e aplicá-los aos dados de entrada, garantindo que estejam em conformidade com os requisitos especificados.

- **Virtualenv**:
Virtualenv é uma ferramenta Python que permite criar ambientes virtuais isolados, nos quais você pode instalar pacotes Python específicos para um projeto sem interferir com os pacotes instalados globalmente no sistema. Isso é útil para garantir a compatibilidade das dependências do projeto e facilitar a portabilidade do código entre diferentes ambientes de desenvolvimento.

## Execução
- 1 Dá um fork neste repositório
- 2 Clone ou baixe o seu repositório fork
- 3 Abra seu terminal e navegue até a pasta do projeto
- 4 Inicie o ambiente virtual com python
- 5 Baixe os dependências de requirements.txt:
Cerberus, Pillow, Pytest, Pyton-barcode, Pre-commit, Pylint e Flask
- Rode o comando `phyton run.py` parar iniciar o servidor flask
