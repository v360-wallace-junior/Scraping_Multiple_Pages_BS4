# WebScraping_02

Projeto em Python para **web crawling** e **web scraping**. O crawler percorre páginas e encontra links; o scraper extrai dados das páginas visitadas para análise ou armazenamento.

## Funcionalidades

- Acessar páginas web e localizar links.
- Percorrer páginas a partir de uma URL inicial.
- Extrair informações do HTML conforme as regras definidas no código.
- Preparar os resultados para análise ou exportação.

## Requisitos

- Python 3
- Dependências do projeto, se houver

## Instalação

Clone ou baixe o repositório. Se o projeto incluir `requirements.txt`, instale as dependências:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
pip install -r requirements.txt
```

No Windows, ative o ambiente virtual com:

```powershell
.venv\Scripts\activate
```

## Execução

Execute o script principal do projeto. Por exemplo, se o arquivo de entrada for `main.py`:

```bash
python main.py
```

Configure no código a URL inicial, os limites de navegação e os campos que deseja coletar, de acordo com a estrutura das páginas-alvo.

## Uso responsável

- Consulte os termos de uso e o arquivo `robots.txt` do site.
- Respeite limites de requisições e inclua intervalos entre acessos.
- Não tente contornar autenticação ou controles de acesso.
- Evite coletar ou armazenar dados pessoais sem autorização e base legal.

## Licença

Nenhuma licença foi especificada. Adicione uma licença ao projeto para definir os termos de uso e distribuição.
