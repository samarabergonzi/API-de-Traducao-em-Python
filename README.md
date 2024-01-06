# API de Tradução em Python

Este é um projeto simples que fornece uma API de tradução em Python usando Flask e a biblioteca googletrans para interagir com o Google Translate.

## Como Usar

### Pré-requisitos

- Certifique-se de ter o Python instalado em sua máquina. Você pode baixá-lo em [python.org](https://www.python.org/).

### Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/api-traducao-python.git

   # Acesse o diretório do projeto
   cd api-traducao-python

   # Instale as dependências
   pip install -r requirements.txt


# Execução
  python app.py

# Exemplo de Solicitação

  curl -X POST -H "Content-Type: application/json" -d '{"text": "Hello, world!", "target_lang": "pt"}' http://localhost:5000/translate

# Contribuições

Contribuições são bem-vindas! Abra issues ou envie pull requests.

# Licença

Este projeto é licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.
